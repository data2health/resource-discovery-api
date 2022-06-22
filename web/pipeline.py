from biothings.web.query import ESQueryBuilder
from elasticsearch_dsl import Search


class RDPQueryBuilder(ESQueryBuilder):

    def default_string_query(self, q, options):

        search = Search()
        q = q.strip()
        
        # elasticsearch query string syntax
        if ":" in q or " AND " in q or " OR " in q:
            search = search.query('query_string', query=q)
        
        # Boost fields : ['name','title', 'label', 'toolName', 'article_title']
        # Note: 'author' field goes by various names across indices, ['name', 'etc'...],
        # therefore we have to account for the variety
        # -- term search 
        elif q.startswith('"') and q.endswith('"'):
            query = {
                "query": {
                    "dis_max": {
                        "queries": [
                            {"term": {"author.name": {"value": q.strip('"'), "boost": 5}}},
                            {"term": {"name": {"value": q.strip('"'), "boost": 5}}},
                            {"term": {"label": {"value": q.strip('"'), "boost": 5}}},
                            {"term": {"toolName": {"value": q.strip('"'), "boost": 5}}},
                            {"term": {"article_title": {"value": q.strip('"'), "boost": 5}}},
                            #{"match": {"author.name": {"query": q, "boost": 3, "operator": "AND"}}},
                            {"multi_match": {"fields": ['author.name', 'title', 'name', 'label', 'toolName', 'article_title'], "query": q, "boost": 5, "operator": "AND"}},
                            # ---------------------------------------------
                            {"query_string": {"query": q, "default_operator": "AND"}}  # base score
                        ]
                    }
                }
            }
            search = search.update_from_dict(query)

        # -- text search
        else:  
            query = {
                "query": {
                    "dis_max": {
                        "queries": [
                            {"term": {"author.name": {"value": q.strip('"'), "boost": 5}}},
                            {"term": {"name": {"value": q.strip('"'), "boost": 5}}},
                            {"term": {"label": {"value": q.strip('"'), "boost": 5}}},
                            {"term": {"toolName": {"value": q.strip('"'), "boost": 5}}},
                            {"term": {"article_title": {"value": q.strip('"'), "boost": 5}}},
                            #{"match": {"author.name": {"query": q, "boost": 3}}},
                            {"multi_match": {"fields": ['author.name', 'title', 'name', 'label', 'toolName', 'article_title'], "query": q, "boost": 5, "operator": "AND"}},
                            # ---------------------------------------------
                            {"query_string": {"query": q, "default_field": "all"}},  # base score
                            # ---------------------------------------------
                            {"wildcard": {"title": {"value": q + "*", "boost": 3}}},
                            {"wildcard": {"label": {"value": q + "*", "boost": 3}}},
                            {"wildcard": {"article_title": {"value": q + "*", "boost": 3}}},
                            {"wildcard": {"toolName": {"value": q + "*", "boost": 3}}}
                        ],
                    }
                }
            }
            search = search.update_from_dict(query)

        return search
        
    def apply_extras(self, search, options):

        search = Search().query(
            "function_score",
            query=search.query,
           )

        # Feature: post_filter
        # -- implementation using query string matching
        if options.aggs and options.post_filter:
            args_str = ' '.join(options['post_filter']) # set arguments as a string for query format
            search = search.post_filter("query_string", query = args_str)
            
        return super().apply_extras(search, options)