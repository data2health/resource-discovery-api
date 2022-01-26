from config_local import ES_PRIVATE_HOST, ES_HTTP_AUTH

# *****************************************************************************
# Elasticsearch Settings
# *****************************************************************************
ES_HOST = ES_PRIVATE_HOST
ES_ARGS={
    "http_auth": ES_HTTP_AUTH
}

ES_INDICES = {"cd2h-outbreak": "outbreak_*"}
ES_DOC_TYPE = 'doc'
ANNOTATION_DEFAULT_SCOPES = ["_id"]


# *****************************************************************************
# Web Application
# *****************************************************************************
API_PREFIX='cd2h-outbreak'
API_VERSION = 'v1'

