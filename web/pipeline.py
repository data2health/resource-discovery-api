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

            if len(pf_arg) == 1: # single parameter passed
                pf_key,pf_val=pf_arg[0].split(":")[0],pf_arg[0].split(":")[1]
                search = search.post_filter("term", **{pf_key: pf_val} )
                
            elif len (pf_arg) > 1: # multiple parameters passed
                args_dict={} 
                for val in pf_arg:
                    pf_key,pf_val=val.split(":")[0],val.split(":")[1]
                    if pf_key not in args_dict:
                        args_dict[pf_key]=[pf_val]
                    else:
                        args_dict[pf_key].append(pf_val)
                # setup the multi-term search
                bool_search=[{"terms": {_key:_val}} for _key,_val in args_dict.items()]
                search = search.post_filter("bool", must=bool_search)
            
        return super().apply_extras(search, options)

    