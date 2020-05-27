import json
import logging
import re
from swagger_server.api import APIUtils
from swagger_server.models.search_data_linkset import SearchDataLinkset, SearchDataLinksetLinks
from swagger_server.models.index_schema_description import IndexSchemaDescription
from swagger_server.models.search_data import SearchData
from swagger_server.models.search_data_search_result import SearchDataSearchResult
from swagger_server.services.grid_search.project_index_attributes import ProjectIndexAttributes
from swagger_server.services.grid_search.sample_index_attributes import SampleIndexAttributes

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s: %(filename)s:%(funcName)s:%(lineno)d: %(message)s"
)

logger = logging.getLogger(__name__)

PROJECT_INDEX = 'projects'
SAMPLE_INDEX = 'samples'
SEARCH_ATTRIBUTES_PATTERN = re.compile("[a-zA-Z0-9]*:")


class GenericSearch:
    """
    service class to handle all the rest api controller calls
    """

    def __init__(self):
        self.api = APIUtils()
        self.project_Indexed_terms = self.get_index_search_attribute_list(PROJECT_INDEX)
        self.sample_Indexed_terms = self.get_index_search_attribute_list(SAMPLE_INDEX)

    def generic_search(self, index_name, dsl_query):
        """
        Generic Search on index if found any search associated runs/projects
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

            elif index_name == SAMPLE_INDEX:
                index_descp = IndexSchemaDescription(
                    id=index_name,
                    es_id='samples',
                    name='Epigenomics Samples and Runs',
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
                        result.search_result.append(self.generate_sample_result(each_hit))
                return result

        except KeyError as err:
            logger.error("KeyError: generic_search() hits")
            logger.exception(err)

    def generate_generic_dsl(self, index_name, generic_search):
        """

        :param generic_search: generic search string provided by user
        :param index_name: elastic search index to be used
        :return: generate elastic search dsl query
        """
        # escape special characters in search query
        generic_search = generic_search.replace('/', '//')
        search_attrib_list = re.findall(SEARCH_ATTRIBUTES_PATTERN, generic_search)

        for term in search_attrib_list:
            logger.info('term: %s' % term)
            temp = term[:-1]
            logger.info('temp %s' % temp)
            if index_name == PROJECT_INDEX:
                search_index_dict = self.project_Indexed_terms
            elif index_name == SAMPLE_INDEX:
                search_index_dict = self.sample_Indexed_terms
            else:
                search_index_dict = None
                logger.error('Error: Index not matched')
            if temp in search_index_dict:
                abs_path = '__' + search_index_dict[temp]
                generic_search = generic_search.replace(temp, abs_path)

        if index_name == PROJECT_INDEX:
            generic_search = generic_search.replace('__', '')
            dsl_json = {
                "query": {
                    "query_string": {
                        "query": generic_search,
                        "default_operator": "AND",
                        "fuzziness": "AUTO",
                        "fuzzy_prefix_length": 0
                    }
                }
            }
        elif index_name == SAMPLE_INDEX:
            bool_condition = "must"
            subquery = generic_search.split('__')
            nested = ''
            non_nested = ''
            for item in subquery:
                if 'SampleEntries' in item:
                    nested = nested + item + ' '
                else:
                    non_nested = non_nested + item + ' '

            # cleanups
            nested = nested.strip()
            non_nested = non_nested.strip()
            if non_nested == '':
                non_nested = '*'
            if nested == '':
                nested = non_nested
                bool_condition = "should"

            dsl_json = {
                "query": {
                    "bool": {
                        bool_condition : [
                            {
                                "query_string": {
                                    "query": non_nested.strip(),
                                    "default_operator": "AND",
                                    "fuzziness": "AUTO",
                                    "fuzzy_prefix_length": 0
                                }
                            },
                            {
                                "nested": {
                                    "path": ["SampleEntries"],
                                    "query": {
                                        "query_string": {
                                            "query": nested.strip(),
                                            "default_operator": "AND",
                                            "fuzziness": "AUTO",
                                            "fuzzy_prefix_length": 0
                                        }
                                    }
                                }
                            }

                        ]
                    }
                }
            }
        else:
            dsl_json = {}
        return dsl_json

    @staticmethod
    def get_index_search_attribute_list(index_name):
        search_attributes = None
        search_attribute_dict = {}
        if index_name == PROJECT_INDEX:
            search_attributes = ProjectIndexAttributes().search_attributes()
        elif index_name == SAMPLE_INDEX:
            search_attributes = SampleIndexAttributes().search_attributes()
        if search_attributes is not None:
            attributes = search_attributes.attributes
            for entry in attributes:
                search_attribute_dict[entry.attrib_name] = entry.attrib_path
            return search_attribute_dict
        else:
            return None

    def generate_project_result(self, data):
        if len(data) > 0:
            project_app = data["_source"].setdefault("ProjectApplication", None)
            project_info = project_app.setdefault("ProjectInformation", None)
            project_sci_justification = project_app.setdefault("ScientificJustification", None)
            project_id = project_info.setdefault("ProjectID", None)
            project_title = project_info.setdefault("ProjectTitle", None)
            project_hyp = project_sci_justification.setdefault("Hypothesis", None)

            title = project_id
            subtitle = project_title
            url_link = self.api.search_properties['project.url.prefix'] + '/' + project_id
            content_text = project_hyp

            # search related sample runs
            links = []
            sub_links = []
            if project_id is not None:
                logger.info('========links sample run search===================-')
                search_query = "ProjectID: " + project_id
                logger.info("SearchQuery: " + search_query)
                sub_es_dsl = self.generate_generic_dsl(index_name=SAMPLE_INDEX, generic_search=search_query)
                logger.info('Search DSL: ' + str(sub_es_dsl))
                link_sample_result = self.generic_search(SAMPLE_INDEX, sub_es_dsl)

                if len(link_sample_result.search_result) > 0:
                    for entry in link_sample_result.search_result:
                        links.append(SearchDataLinksetLinks(
                            link_text=entry.title,
                            link_url=entry.url_link))

                sub_links = SearchDataLinkset(
                    linkset_title="Sequenced Runs",
                    linkset_description="Epigenomics Core sequenced sample datasets associated to project",
                    links=links)
            else:
                logger.info('ProjectID is none. Skipping sub sample result')
            return SearchDataSearchResult(
                title=title,
                subtitle=subtitle,
                url_link=url_link,
                content_text=content_text,
                links=sub_links)

    @staticmethod
    def generate_linked_sample_result(data):
        if len(data) > 0:
            links = []
            sample_data = data["_source"]

    @staticmethod
    def generate_sample_result(data):
        if len(data) > 0:
            sample_data = data["_source"]

            title = sample_data["RunId"]
            subtitle = 'Data commons run folder'
            url_link = sample_data.setdefault("Url", None)
            if url_link is None:
                url_link = sample_data.setdefault("Url", None)
            content_text = ''
            if sample_data['LibrariesPreparedBy'] != '':
                content_text = content_text + '<b>Library prepared by: </b>' + sample_data['LibrariesPreparedBy'] + '<br>'
            if sample_data['PiName'] != '':
                content_text = content_text + '<b>Principal investigator: </b>' + sample_data['PiName'] + '<br>'
            if sample_data['SeqSystem'] != '':
                content_text = content_text + ' <b>Sequencing system: </b>' + sample_data['SeqSystem'] + '<br>'

            sample_entries = sample_data['SampleEntries']
            links = []
            if len(sample_entries) > 0:
                for entry in sample_entries:
                    link_url = entry.setdefault("Url", None)
                    if link_url is None:
                        link_url = entry.setdefault("Url", None)
                    links.append(SearchDataLinksetLinks(
                        link_text=entry.setdefault("SampleName", None),
                        link_url=link_url
                    ))

            sublinks = SearchDataLinkset(
                linkset_title="Related sample fastq files",
                linkset_description="Samples associated to run",
                links=links)
            return SearchDataSearchResult(title=title, subtitle=subtitle,
                                          url_link=url_link, content_text=content_text, links=sublinks)
