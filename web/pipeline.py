from biothings.web.query import ESResultFormatter
from biothings.web.query import ESQueryBuilder, AsyncESQueryPipeline
from elasticsearch_dsl import Search

class MyFormatter(ESResultFormatter):
    """
    Converting the entrezgene into an integer
    """
    def transform_hit(self, path, doc, options):

        if path == '' and 'entrezgene' in doc:  # root level
            try:
                doc['entrezgene'] = int(doc['entrezgene'])
            except:
                ...

class MyQueryBuilder(ESQueryBuilder):
    """
    Modify the query builder stage to add features
    Feature 1- use domain knowledge to deliver search results: docs are scored with rules to
    increase the result relevancy
    """
    def apply_extras(self, search, options):

        search = Search().query(
            "function_score",
            query=search.query,
            functions=[
                {"filter": {"term": {"name": "pseudogene"}}, "weight": "0.5"},  # downgrade
                {"filter": {"term": {"taxid": 9606}}, "weight": "1.55"},
                {"filter": {"term": {"taxid": 10090}}, "weight": "1.3"},
                {"filter": {"term": {"taxid": 10116}}, "weight": "1.1"},
            ], score_mode="first")

        return super().apply_extras(search, options)


class MyQueryPipeline(AsyncESQueryPipeline):
    """
    A tutorial page to show what annotation results can look like
    """
    async def fetch(self, id, **options):

        if id == "rdp-test":
            res = {"_welcome": "RDP API"}
            res.update(await super().fetch("1017", **options))
            return res

        res = await super().fetch(id, **options)
        return res