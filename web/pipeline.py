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
            pf_args=options['post_filter']
            pf_args=list(map(lambda x: x.lower(), pf_args))

            if len(pf_args) == 1: # single parameter passed
                pf_key,pf_val=pf_args[0].split(":")[0],pf_args[0].split(":")[1]
                search = search.post_filter("term", **{pf_key: pf_val})
                
            elif len (pf_args) > 1: # multiple parameters passed
                args_dict={} 
                if "and" in pf_args: # AND clause case
                    args_dict={} 
                    for _str in pf_args:
                         # loop through arguments 
                        # separate the arguments passed in and
                        # set the _key and _property values
                        if ":" in _str:
                            _key=_str.split(":")[0]
                            _property=_str.split(":")[1]
                        else:
                            _property=_str
                            
                        if _key not in args_dict:
                            args_dict[_key]=[_property]

                        else:
                            if _property == 'and':
                                pass
                            else:
                               args_dict[_key].append(_property)
                        
                    # setup the multi-term search
                    bool_search=[{"terms": {_key:_val}} for _key,_val in args_dict.items()]
                    search = search.post_filter("bool", must=bool_search)

                elif "or" in pf_args: # OR clause case
                    args_dict={} 
                    for _str in pf_args:
                        # loop through arguments 
                        # separate the arguments passed in and
                        # set the _key and _property values
                        if ":" in _str:
                            _key=_str.split(":")[0]
                            _property=_str.split(":")[1]
                        else:
                            _property=_str
                
                        if _key not in args_dict:
                            args_dict[_key]=[_property]

                        else:
                            if _property == 'or':
                                pass
                            else:
                               args_dict[_key].append(_property)
                        
                    # setup the multi-term search
                    bool_search=[{"terms": {_key:_val}} for _key,_val in args_dict.items()]
                    search = search.post_filter("bool", should=bool_search)


                else: # default case to AND -- no explicit arg 
                    args_dict={} 
                    for _str in pf_args: # loop through arguments 
                        # separate the arguments passed in and
                        # set the _key and _property values
                        if ":" in _str:
                            _key=_str.split(":")[0]
                            _property=_str.split(":")[1]
                        else:
                            _property=_str
                            
                        if _key not in args_dict:
                            args_dict[_key]=[_property]
                        else:
                            args_dict[_key].append(_property)
                        
                    # setup the multi-term search
                    bool_search=[{"terms": {_key:_val}} for _key,_val in args_dict.items()]
                    search = search.post_filter("bool", must=bool_search)
            
        return super().apply_extras(search, options)

    