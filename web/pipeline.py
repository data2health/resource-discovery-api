from biothings.web.query import ESResultFormatter
from biothings.web.query import ESQueryBuilder, AsyncESQueryPipeline
from elasticsearch_dsl import Search


class RDPQueryBuilder(ESQueryBuilder):
    def apply_extras(self, search, options):
        search = Search().query(
            "function_score",
            query=search.query,
           )
        if options.aggs and options.post_filter:
            search = search.post_filter("term", type=options.post_filter)
        return super().apply_extras(search, options)

    #############################################################################
    #############################################################################