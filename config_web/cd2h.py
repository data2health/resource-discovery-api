import os
from biothings.web.settings.default import QUERY_KWARGS
from web.handlers import EXTRA_HANDLERS
from biothings.web.settings.default import APP_LIST


ES_HOST= 'http://search.cd2h.org:9200/
ES_INDICES = {"es_query": "v1"} # document type URL templating
ANNOTATION_DEFAULT_SCOPES = ["_id", "symbol"] # setting to specify id fields 
#ES_INDEX=''
#ES_DOC_TYPE

API_PREFIX='cd2h'
API_VERSION=''
# Declare a new route
#APP_LIST = [
 #   *APP_LIST, # keep the original ones
 #   (r"/{ver}/es_query/(.+)", "web.handlers.EchoHandler"),
#]

ES_RESULT_TRANSFORM = "web.pipeline.MyFormatter" # format the output
ES_QUERY_BUILDER = "web.pipeline.MyQueryBuilder" # increase search result relevancy 
ES_QUERY_PIPELINE = "web.pipeline.MyQueryPipeline" #overwrites Pipeline class

