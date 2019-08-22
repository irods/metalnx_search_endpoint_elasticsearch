import logging

from swagger_server.services.grid_search.epigenomics_search_adapter import EpigenomicsSearchAdapter
from swagger_server.models.indexes import Indexes  # noqa: E501
from swagger_server.models.search_attributes import SearchAttributes  # noqa: E501
from swagger_server.services.grid_search.project_index_attributes import ProjectIndexAttributes
from swagger_server.services.grid_search.sample_index_attributes import SampleIndexAttributes
from werkzeug.exceptions import BadRequest

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s: %(filename)s:%(funcName)s:%(lineno)d: %(message)s"
)

logger = logging.getLogger(__name__)


def get_indexes():  # noqa: E501
    """Find index types supported by this api

    Returns a summary list of the search indexes available at this endpoint # noqa: E501


    :rtype: Indexes
    """
    logger.debug('info_controller: get_indexes()')
    adapter = EpigenomicsSearchAdapter()
    return adapter.describe_index()


def get_index_search_attributes(index_name):  # noqa: E501
    """Find search attribute terms for a specific index

    Returns a list of search attribute terms available for specified index # noqa: E501

    :param index_name:
    :type index_name: str

    :rtype: SearchAttributes
    """
    logger.debug('info_controller: get_index_search_attributes()')
    logger.debug('args: \n index: %s' % index_name)

    if index_name == 'projects':
        search_attributes = ProjectIndexAttributes()

        return search_attributes.search_attributes()
    elif index_name == 'samples':
        search_attributes = SampleIndexAttributes()
        return search_attributes.search_attributes()
    else:
        raise BadRequest('Error: Index not found')
