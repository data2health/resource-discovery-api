EXTRA_HANDLERS = [(r"/{ver}/es_query/(.+)", "handlers.EchoHandler"),
                 (r"/{ver}/login", "handlers.EchoHandler")]