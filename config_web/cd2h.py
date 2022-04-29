from config_local import ES_PRIVATE_HOST, ES_HTTP_AUTH
import copy
from biothings.web.settings.default import (ANNOTATION_KWARGS, QUERY_KWARGS)


# *****************************************************************************
# Elasticsearch Settings
# *****************************************************************************

ES_HOST = ES_PRIVATE_HOST
ES_ARGS = {
    "http_auth": ES_HTTP_AUTH
}

ES_INDICES = {
    None: "cd2h*,csbsc*,outbreak_*_clone,cckp-computational-tools-20220401-2,nlpsandbox-computational-tools-20220401-2"
    }   
    #"outbreak": "outbreak_*_clone",
    #"cd2h": "cd2h-*",
    #"csbc": "csbc-*",
    #"comp-tools":"*nlpsandbox-computational-tools-20220401-2, *cckp-computational-tools-20220401-2" 
#}

# *****************************************************************************
# Web Application
# *****************************************************************************

API_PREFIX = 'api'
API_VERSION = ''


# *****************************************************************************
# Elasticsearch Query Pipeline and Customizations
# *****************************************************************************

SOURCE_TYPEDEF={
     'post_filter': {
        'type': list,
        'default': ['all'],
        'strict': False,
        'max': 1000
     }
}

ES_DOC_TYPE = 'doc'
ANNOTATION_DEFAULT_SCOPES = ["_id"]

ANNOTATION_KWARGS = copy.deepcopy(ANNOTATION_KWARGS)
ANNOTATION_KWARGS['*'].update(SOURCE_TYPEDEF)

QUERY_KWARGS = copy.deepcopy(QUERY_KWARGS)
QUERY_KWARGS['*'].update(SOURCE_TYPEDEF)

ES_QUERY_BUILDER = "web.pipeline.RDPQueryBuilder"
