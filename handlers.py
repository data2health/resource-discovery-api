from biothings.web.handlers import BaseAPIHandler

# declare a new route
class EchoHandler(BaseAPIHandler):

    def get(self, text):
        self.write({
            "status": "ok",
            "result": text
       })