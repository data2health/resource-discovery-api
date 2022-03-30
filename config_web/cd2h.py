from config_local import ES_PRIVATE_HOST, ES_HTTP_AUTH
import copy
from biothings.web.settings.default import (ANNOTATION_KWARGS, QUERY_KWARGS, APP_LIST)


# *****************************************************************************
# Elasticsearch Settings
# *****************************************************************************
ES_HOST = ES_PRIVATE_HOST
ES_ARGS = {
    "http_auth": ES_HTTP_AUTH
}

ES_INDICES = {
    None: "cd2h*,csbsc*,outbreak_*_clone",   # all indices excluding internal ones
    "outbreak": "outbreak_*_clone",
    "cd2h": "cd2h-*",
    "csbc": "csbc-*"
}

# *****************************************************************************
# Web Application
# *****************************************************************************

API_PREFIX = 'api'
API_VERSION = ''


# *****************************************************************************
# Elasticsearch Query Pipeline and Customizations
# *****************************************************************************

SOURCE_TYPEDEF = {
    'post_filter': {
        'type': str,
        'default': None,
        'max': 1000,
    }
}

ES_DOC_TYPE = 'doc'
ANNOTATION_DEFAULT_SCOPES = ["_id"]

ANNOTATION_KWARGS = copy.deepcopy(ANNOTATION_KWARGS)
ANNOTATION_KWARGS['*'].update(SOURCE_TYPEDEF)

QUERY_KWARGS = copy.deepcopy(QUERY_KWARGS)
QUERY_KWARGS['*'].update(SOURCE_TYPEDEF)
#QUERY_KWARGS['*']['_source']['default'] = [ '_id']
#QUERY_KWARGS['POST']['scopes']['default'] = [ '_id', 'name']

ES_QUERY_BUILDER = "web.pipeline.RDPQueryBuilder"
