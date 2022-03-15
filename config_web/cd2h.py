from config_local import ES_PRIVATE_HOST, ES_HTTP_AUTH

# *****************************************************************************
# Elasticsearch Settings
# *****************************************************************************
ES_HOST = ES_PRIVATE_HOST
ES_ARGS = {
    "http_auth": ES_HTTP_AUTH
}

ES_INDICES = {
    None: "c*,o*",   # all indices excluding internal ones
    "outbreak": "outbreak_*_clone",
    "cd2h": "cd2h-*",
    "csbc": "csbc-*"
}
ES_DOC_TYPE = 'doc'
ANNOTATION_DEFAULT_SCOPES = ["_id"]


# *****************************************************************************
# Web Application
# *****************************************************************************
API_PREFIX = 'api'
API_VERSION = ''
