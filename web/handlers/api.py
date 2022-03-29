from biothings.web.handlers import QueryHandler

class PostFilterHandler(QueryHandler):
    def prepare(self):
        super().prepare()