import connexion
import six
import logging

from swagger_server.models.search_data import SearchData  # noqa: E501
from swagger_server import util

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s: %(filename)s:%(funcName)s:%(lineno)d: %(message)s"
)

logger = logging.getLogger(__name__)


def generic_search(index_name, search_query):  # noqa: E501
    """Generic search on one or all available indexes

    Returns result hits with associated fields and values # noqa: E501

    :param index_name:
    :type index_name: str
    :param search_query:
    :type search_query: str

    :rtype: SearchData
    """
    logger.debug('search_controller: generic_search()')
    logger.debug('args: \n index_name: %s \n search_query: %s' % (index_name, search_query))
    result = SearchData()
    return result
