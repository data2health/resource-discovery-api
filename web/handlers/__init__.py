
EXTRA_HANDLERS = [(r"/{ver}/es_query/(.+)", "web.handlers.EchoHandler"),
                 (r"/{ver}/login/(.+)", "web.handlers.EchoHandler")]