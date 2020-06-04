import os

import requests
import sys
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s: %(filename)s:%(funcName)s:%(lineno)d: %(message)s"
)

logger = logging.getLogger(__name__)


class APIUtils:

    search_properties_env_variable = "SEARCH_PROPERTIES_FILE"

    """
    util class to handle all API calls
    """
    def __init__(self):

        """
        Inspect for a SEARCH_PROPERTIES_FILE environment variable and error if not found. This props file
        contains the information necessary to connect to Elasticsearch and to handle JWT security.

        See the sample_search_properties.properties file for expected settings
        """
        self.search_properties = load_props()
        self.baseurl = self.search_properties["es.baseurl"]
        self.session = requests.Session()

    def setup(self, base_url):
        self.baseurl = base_url

    # Functions to Access REST Endpoints

    # GET wrapper function
    def get(self, url):
        return self._createHTTPRequest(url)

    # POST wrapper function
    def post(self, url, json_obj):
        return self._createHTTPRequest(url, 'POST', json_obj)

    # PUT wrapper function
    def put(self, url, json_obj):
        return self._createHTTPRequest(url, 'PUT', json_obj)

    # DELETE wrapper function
    def delete(self, url, json_obj):
        return self._createHTTPRequest(url, 'DELETE', json_obj)

    # Create a Standard API HTTP request
    def _createHTTPRequest(self, url, http_method_type='GET', json_obj=None):
        logger.debug('HTTP REQUEST TYPE :: %s' % http_method_type)
        response = ''
        try:
            if http_method_type == 'GET':
                response = self.session.get(url)
                if response.status_code == 200:
                    logger.debug('Get request success!')
                else:
                    response.raise_for_status()
            elif http_method_type == 'POST':
                body = json_obj
                response = self.session.post(url, json=body)
                if response.status_code == 201:
                    logger.debug('Post request success!')
                else:
                    response.raise_for_status()
            elif http_method_type == 'PUT':
                body = json_obj
                response = self.session.put(url, json=body)
                if response.status_code == 200:
                    logger.debug('Put request success!')
                else:
                    response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            # Whoops it wasn't a 200
            logger.error('ERROR: API call returned HTTP Error')
            logger.error(url)
            logger.exception(e)
        except requests.exceptions.RequestException as e:
            logger.error('ERROR: Bad Request Error')
            logger.exception(e)
            sys.exit()
        return response

    # create index mapping
    def create_index_with_mapping(self, index_name, json_data):
        url = self.baseurl + '/' + index_name
        response = self.put(url, json_data)
        return response

    # index doc: adds or updates a typed JSON document in a specific index
    def add_index_doc(self, index_name, id, json_obj):

        url = self.baseurl + '/' + index_name + '/_doc/' + id
        response = self.post(url, json_obj)
        return response


def load_props():
    """return a dictionary of properties file values specfied by the SEARCH_PROPERTIES_FILE environment variable"""
    logging.info("dict_from_props()")

    filename = os.environ[APIUtils.search_properties_env_variable]
    logging.info("filename: %s" % filename)

    myprops = {}
    try:
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()  # removes trailing whitespace and '\n' chars

                if "=" not in line: continue  # skips blanks and comments w/o =
                if line.startswith("#"): continue  # skips comments which contain =

                k, v = line.split("=", 1)
                myprops[k] = v
            return myprops
    except Exception:
        logging.error("cannot find properties file indicated by SEARCH_PROPERTIES_FILE")
        raise ConfigurationError


class ConfigurationError(Exception):
    """Raised when the configuration properties are unavailable"""
    pass



