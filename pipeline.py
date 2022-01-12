from biothings.web.query import ESResultFormatter
from biothings.web.query import ESQueryBuilder, AsyncESQueryPipeline
from elasticsearch_dsl import Search

class MyFormatter(ESResultFormatter):

    def transform_hit(self, path, doc, options):

        if path == '' and 'entrezgene' in doc:  # root level
            try:
                doc['entrezgene'] = int(doc['entrezgene'])
            except:
                ...

class MyQueryBuilder(ESQueryBuilder):

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
    Now we made ourselves a tutorial page to show what annotation results can look like,
    """
    async def fetch(self, id, **options):

        if id == "tutorial":
            res = {"_welcome": "to the world of biothings.api"}
            res.update(await super().fetch("1017", **options))
            return res

        res = await super().fetch(id, **options)
        return res