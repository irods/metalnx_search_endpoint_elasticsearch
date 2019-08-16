import requests
import sys
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s: %(filename)s:%(funcName)s:%(lineno)d: %(message)s"
)

logger = logging.getLogger(__name__)


class APIUtils:
    """
    util class to handle all API calls
    """
    def __init__(self):
        self.baseurl = 'http://localhost:9200'
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
