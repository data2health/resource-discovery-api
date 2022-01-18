import os
from biothings.web.settings.default import QUERY_KWARGS
from web.handlers import EXTRA_HANDLERS


ES_HOST = "localhost:9200" # es server
ES_INDICES = {"es_query": "v1"} # document type URL templating
ANNOTATION_DEFAULT_SCOPES = ["_id", "symbol"] # setting to specify id fields 
# if we want to limit output --
#QUERY_KWARGS['*']['_source']['default'] = ['name', 'symbol', 'taxid', 'entrezgene']
ES_RESULT_TRANSFORM = "pipeline.MyFormatter" # format the output
ES_QUERY_BUILDER = "pipeline.MyQueryBuilder" # increase search result relevancy 
ES_QUERY_PIPELINE = "pipeline.MyQueryPipeline" #overwrites Pipeline class

# Declare a new route
from biothings.web.settings.default import APP_LIST
APP_LIST=EXTRA_HANDLERS
APP_LIST = [
    *APP_LIST, # keep the original ones
    (r"/{ver}/es_query/(.+)", "handlers.EchoHandler"),
]
