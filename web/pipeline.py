#from biothings.web.query import ESResultFormatter
from biothings.web.query import ESQueryBuilder#,  AsyncESQueryPipeline
from elasticsearch_dsl import Search


class RDPQueryBuilder(ESQueryBuilder):
    def apply_extras(self, search, options):
        search = Search().query(
            "function_score",
            query=search.query,
           )
        if options.aggs and options.post_filter:
            pf_arg=options['post_filter']
            pf_key,pf_val=pf_arg.split(":")[0],pf_arg.split(":")[1]
            search = search.post_filter("term", **{pf_key: pf_val})
        return super().apply_extras(search, options)

    #############################################################################
    #############################################################################

    