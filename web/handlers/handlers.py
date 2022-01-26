from biothings.web.handlers import BaseAPIHandler, BaseQueryHandler
# declare a new route
class EchoHandler(BaseAPIHandler):

    def get(self, text):
        self.write({
            "status": "ok",
            "result": text
       })

#class TestQueryHandler(BaseQueryHandler):
