import json
import logging
import re
from swagger_server.api import APIUtils
from swagger_server.models.search_data_linkset import SearchDataLinkset, SearchDataLinksetLinks
from swagger_server.models.result_properties import ResultProperties, ResultPropertiesPropertySet
from swagger_server.models.index_schema_description import IndexSchemaDescription
from swagger_server.models.search_data import SearchData
from swagger_server.models.search_data_search_result import SearchDataSearchResult
from swagger_server.services.grid_search.metadata_index_attributes import MetadataIndexAttributes

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s: %(filename)s:%(funcName)s:%(lineno)d: %(message)s"
)

logger = logging.getLogger(__name__)

METADATA_INDEX = 'metadata'
SEARCH_ATTRIBUTES_PATTERN = re.compile("[a-zA-Z0-9]*:")


class GenericSearch:
    """
    service class to handle all the rest api controller calls
    """

    def __init__(self):
        self.api = APIUtils()
        self.metadata_Indexed_terms = self.get_index_search_attribute_list(METADATA_INDEX)

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
            if index_name == METADATA_INDEX:
                logger.info('Search index :: %s' % index_name)
                index_descp = IndexSchemaDescription(
                    id=index_name,
                    es_id='metadata',
                    name='Metadata ElasticSearch Indexes',
                    version='date_indexed_version'
                )
                result = SearchData(index_schema_description=index_descp, search_result=[])
                hits = es_json.pop("hits")
                try:
                    total_hits = hits.get('total', {}).get('value')  # ES7+
                except AttributeError:
                    total_hits = hits.get('total')                   # ES6
                if total_hits > 0:
                    logger.info("Total number of hits:: %d" % total_hits)
                    hits_list = hits.pop("hits")
                    for each_hit in hits_list:
                        logger.debug('each_hit::_____________\n')
                        logger.debug(each_hit)
                        result.search_result.append(self.generate_metadata_search_result(each_hit))
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
        terms_with_abs_path = []

        for term in search_attrib_list:
            logger.info('term: %s' % term)
            temp = term[:-1]
            if index_name == METADATA_INDEX:
                search_index_dict = self.metadata_Indexed_terms
                logger.info('search_index_dict:')
                logger.info(search_index_dict)
            else:
                search_index_dict = None
                logger.error('Error: Index not matched')
            if temp in search_index_dict:
                abs_path = '__' + search_index_dict[temp]
                if temp not in terms_with_abs_path:
                    generic_search = generic_search.replace(temp, abs_path)
                    terms_with_abs_path.append(temp)
                else:
                    logger.info('Absolute path already added for term: %s' % temp)
        logger.info('updated generic search: %s' % generic_search)

        if index_name == METADATA_INDEX:
            bool_condition = "must"
            subquery = generic_search.split('__')
            nested = ''
            non_nested = ''
            for item in subquery:
                if 'metadataEntries' in item:
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
            logger.info('non_nested query: %s' % non_nested)
            logger.info('nested query: %s' % nested)
            logger.info('boolean condition: %s' % bool_condition)

            dsl_json = {
                "query": {
                    "bool": {
                        bool_condition: [
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
                                    "path": ["metadataEntries"],
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
        if index_name == METADATA_INDEX:
            search_attributes = MetadataIndexAttributes().search_attributes()
        if search_attributes is not None:
            attributes = search_attributes.attributes
            for entry in attributes:
                search_attribute_dict[entry.attrib_name] = entry.attrib_path
            return search_attribute_dict
        else:
            return None

    @staticmethod
    def generate_metadata_search_result(data):
        if len(data) > 0:
            logger.info(data)
            metadata_data = data["_source"]

            title = metadata_data["fileName"]
            subtitle = 'Data from Epigenomics core'
            url_link = metadata_data.setdefault("url", None)
            zone_name = metadata_data['zoneName']
            abs_path = metadata_data.setdefault('absolutePath', None)
            parent_path = metadata_data.setdefault('parentPath', None)
            size = metadata_data.setdefault('dataSize', None)
            isFile = metadata_data.setdefault('isFile', None)
            mime_type = metadata_data.setdefault('mimeType', None)
            last_mod_date = metadata_data.setdefault('lastModifiedDate', None)

            if url_link is None:
                url_link = metadata_data.setdefault("url", None)

            content_text = ''
            if not isFile:
                content_text += '<b>Collection: </b>' + parent_path + '<br>'

            if zone_name is not None:
                content_text += '<b>Zone: </b>' + zone_name + '<br>'
            if mime_type is not None:
                content_text += '<b>MimeType: </b>' + mime_type + '<br>'
            if last_mod_date is not None:
                content_text += '<b>Modified: </b>' + str(last_mod_date) + '<br>'
            if size is not None:
                content_text += '<b>Size: </b>' + str(size) + 'kB <br>'

            result_properties = [
                ResultPropertiesPropertySet(name='zoneName', value=zone_name),
                ResultPropertiesPropertySet(name='absolutePath', value=abs_path),
                ResultPropertiesPropertySet(name='parentPath', value=parent_path),
                ResultPropertiesPropertySet(name='dataSize', value=size),
                ResultPropertiesPropertySet(name='isFile', value=isFile),
                ResultPropertiesPropertySet(name='mimeType', value=mime_type),
                ResultPropertiesPropertySet(name='lastModifiedDate', value=last_mod_date)
            ]

            property_set = ResultProperties(propertyset_title='file system properties',
                                            propertyset_description='file properties extracted from iRODS catalog',
                                            property_set=result_properties)

            metadata_entries = metadata_data['metadataEntries']
            links = []
            if len(metadata_entries) > 0:
                # add metadata avu's logic here!
                logger.info(metadata_entries)

            sublinks = SearchDataLinkset(
                linkset_title="Related sub-links",
                linkset_description="Similar associated data",
                links=links)
            return SearchDataSearchResult(title=title, subtitle=subtitle,
                                          url_link=url_link, links=sublinks, properties=property_set,
                                          content_text=content_text)
