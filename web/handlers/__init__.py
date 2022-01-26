
EXTRA_HANDLERS = [(r"/rdp-cd2h/test_query/(.+)", "web.handlers.handlers.EchoHandler"),
                 (r"/rdp-test/", "web.pipeline.MyQueryPipeline")]

