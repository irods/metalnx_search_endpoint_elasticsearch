import json
import logging

from swagger_server.api import APIUtils
from swagger_server.models.search_data_linkset import SearchDataLinkset, SearchDataLinksetLinks
from swagger_server.models.index_schema_description import IndexSchemaDescription
from swagger_server.models.search_data import SearchData
from swagger_server.models.search_data_search_result import SearchDataSearchResult
from swagger_server.services.grid_search.project_index_attributes import ProjectIndexAttributes
from swagger_server.services.grid_search.sample_index_attributes import SampleIndexAttributes

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s: %(filename)s:%(funcName)s:%(lineno)d: %(message)s"
)

logger = logging.getLogger(__name__)

PROJECT_INDEX = 'projects'
SAMPLE_INDEX = 'samples'


class GenericSearch:
    """
    service class to handle all the rest api controller calls
    """

    def __init__(self):
        self.api = APIUtils()
        self.project_Indexed_terms = self.get_index_serach_attribute_list(PROJECT_INDEX)
        self.sample_Indexed_terms = self.get_index_serach_attribute_list(SAMPLE_INDEX)

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
                    id=index_name,
                    es_id='projects',
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
                        result.search_result.append(self.generate_project_result(each_hit))
                return result

        except KeyError as err:
            logger.error("KeyError: generic_search() hits")
            logger.exception(err)

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
    def get_index_serach_attribute_list(index_name):
        search_attributes = None
        search_attribute_list = []
        if index_name == PROJECT_INDEX:
            search_attributes = ProjectIndexAttributes().search_attributes()

        elif index_name == SAMPLE_INDEX:
            search_attributes = SampleIndexAttributes().search_attributes()
        if search_attributes is not None:
            attributes = search_attributes.attributes
            for entry in attributes:
                search_attribute_list.append(entry.attrib_name)
            return search_attribute_list
        else:
            return None

    @staticmethod
    def generate_project_result(data):
        if len(data) > 0:
            project_details = data["_source"]

            if project_details["ProjectID"] is not None:
                title = project_details["ProjectID"]
            else:
                title = None

            if project_details["ProjectTitle"] is not None:
                subtitle = project_details["ProjectTitle"]
            else:
                subtitle = None

            if project_details["url"] is not None:
                url_link = project_details["url"]
            else:
                url_link = None

            content_text = project_details["Hypothesis"]

            links = []
            links.append(SearchDataLinksetLinks(
                link_text="NS00045",
                link_url="http://example.com/NS00045"))
            links.append(SearchDataLinksetLinks(
                link_text="NS00000",
                link_url="http://example.com/NS00000"))

            sublinks = SearchDataLinkset(
                linkset_title="Sequenced Runs",
                linkset_description="Epigenomics Core sequenced sample datasets associated to project",
                links=links)

            return SearchDataSearchResult(title=title, subtitle=subtitle,
                                          url_link=url_link, content_text=content_text, links=sublinks)
