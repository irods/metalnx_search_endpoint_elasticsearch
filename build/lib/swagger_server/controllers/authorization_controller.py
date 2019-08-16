import logging

from swagger_server.services.auth.grid_auth_util import GridAuthUtil

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s: %(filename)s:%(funcName)s:%(lineno)d: %(message)s"
)

logger = logging.getLogger(__name__)

"""
controller generated to handled auth operation described at:
https://connexion.readthedocs.io/en/latest/security.html
"""


def check_bearer_auth(token):
    logger.debug('authorization_controller: check_bearer_auth()')
    logger.debug('args: \n token %s' % token)
    grid_auth_util = GridAuthUtil()
    return grid_auth_util.check_bearer_auth(token)
