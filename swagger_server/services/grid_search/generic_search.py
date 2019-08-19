import json
import logging

from swagger_server.api import APIUtils
from swagger_server.models.index_schema_description import IndexSchemaDescription
from swagger_server.models.search_data import SearchData
from swagger_server.models.search_data_search_result import SearchDataSearchResult

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s: %(filename)s:%(funcName)s:%(lineno)d: %(message)s"
)

logger = logging.getLogger(__name__)

PROJECT_INDEX = 'projects'
SAMPLE_INDEX = 'samples'

# ToDo: get this terms dynamically by making api call to ES
PROJECT_INDEXED_TERMS = ['ProjectID', 'ASPNumber', 'IRBNumber', 'ProjectNumber', 'ProjectTitle']


class GenericSearch:
    """
    service class to handle all the rest api controller calls
    """

    def __init__(self):
        self.api = APIUtils()

    @staticmethod
    def generate_generic_dsl(generic_search):
        """

        :param generic_search: generic search string provided by user
        :return: generate elastic search dsl query
        """
        dsl_json = {
            "query": {
                "query_string": {
                    "query": generic_search
                }
            }
        }
        return dsl_json

    @staticmethod
    def extract_project_data(data):
        if len(data) > 0:
            project_details = data["_source"]
            if project_details["ProjectTitle"] is not None:
                title = project_details["ProjectTitle"]
            else:
                title = None
            if project_details["url"] is not None:
                url_link = project_details["url"]
            else:
                url_link = None

            content_text = ''
            for term in PROJECT_INDEXED_TERMS:
                if project_details[term] is not None:
                    content_text = content_text + term + ': ' + project_details[term] + ', '
            content_text = content_text.rstrip(', ')
            return SearchDataSearchResult(title=title, url_link=url_link, content_text=content_text)

    def generic_search(self, index_name, dsl_query):
        """
        Generic Search on project index if found any search associated runs
        :param dsl_query: elastic search query dsl
        :param index_name: name of index on which search is to be performed
        :return: result data if any hits
        """
        url = self.api.baseurl + '/' + index_name + '/_search?size=50'
        response = self.api.post(url, dsl_query)
        es_json = json.loads(response.text)
        logger.debug('Result: \n\n')
        logger.debug(es_json)
        try:
            if index_name == PROJECT_INDEX:
                index_descp = IndexSchemaDescription(
                    id='Projects',
                    name='Epigenomics Projects',
                    info='Search of project request information, hypothesis, purpose, etc. as entered during the '
                         'project approval phase',
                    version='date_indexed_version'
                )

                result = SearchData(index_schema_description=index_descp, search_result=[])
                hits = es_json.pop("hits")
                total_hits = hits.get('total', {}).get('value')
                if total_hits > 0:
                    logger.info("Total number of hits:: %d" % total_hits)
                    hits_list = hits.pop("hits")
                    for each_hit in hits_list:
                        logger.debug('each_hit::_____________\n')
                        logger.debug(each_hit)
                        result.search_result.append(self.extract_project_data(each_hit))
                return result
        except KeyError as err:
            logger.error("KeyError: generic_search() hits")
            logger.exception(err)
