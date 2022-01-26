from biothings.web.handlers import BaseAPIHandler

# declare a new route --from
class EchoHandler(BaseAPIHandler):

    def get(self, text):
        self.write({
            "status": "ok",
            "result": text
       })

