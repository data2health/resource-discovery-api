from biothings.web.handlers import BaseAPIHandler, BaseQueryHandler
from biothings.web.query import ESQueryBuilder
from elasticsearch_dsl import Search


# declare a new route --from
class EchoHandler(BaseAPIHandler):

    def get(self, text):
        self.write({
            "status": "ok",
            "result": text
       })


class TestQueryHandler(BaseAPIHandler):

    def get(self, search_text):
        self.write({
            "status": "ok",
            "result": search_text
            
       })
       
    #def apply_extras(self, search, options):
     #   
        #search = Search().query(
      #      "function_score",
       #     query=search.query,
        #    )

        #eturn super().apply_extras(search, options)