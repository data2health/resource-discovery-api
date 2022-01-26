import os
from biothings.web.settings.default import QUERY_KWARGS
from web.handlers import EXTRA_HANDLERS
from biothings.web.settings.default import APP_LIST
from .config_local import Credentials

# *****************************************************************************
# Elasticsearch Settings
# *****************************************************************************
ES_HOST = 'http://search.cd2h.org:9200/'
ES_ARGS=Credentials.credentials
ES_INDICES = {"cd2h_test": "cd2h-clic-education"}
ES_INDEX = 'cd2h-clic-education'
ES_DOC_TYPE = 'doc'
ANNOTATION_DEFAULT_SCOPES = ["_id"]


# *****************************************************************************
# Web Application
# *****************************************************************************

API_VERSION = 'v1'
API_PREFIX='cd2h'
#APP_LIST += [
 #   (r"/<ver>/<pre>/test/(.+)", "web.handlers.handlers.TestQueryHandler"),
#]

# *****************************************************************************
# Elasticsearch Query Pipeline
# *****************************************************************************
#ES_RESULT_TRANSFORM = "web.pipeline.MyFormatter" # format the output
ES_QUERY_BUILDER = "web.pipeline.TestQueryBuilder" # increase search result relevancy 
#ES_QUERY_PIPELINE = "web.pipeline.MyQueryPipeline" #overwrites Pipeline class
#AVAILABLE_FIELDS_EXCLUDED = ['all', 'accession_agg', 'refseq_agg']
