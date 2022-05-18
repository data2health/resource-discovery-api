#from biothings.web.query import ESResultFormatter
from biothings.web.query import ESQueryBuilder#,  AsyncESQueryPipeline
from elasticsearch_dsl import Search


class RDPQueryBuilder(ESQueryBuilder):
    def apply_extras(self, search, options):
        search = Search().query(
            "function_score",
            query=search.query,
           )

        # post_filter 
        if options.aggs and options.post_filter:
            args_str = ' '.join(options['post_filter']) # set arguments as a string for query format
            search = search.post_filter("query_string", query = args_str)
            
        return super().apply_extras(search, options)

    