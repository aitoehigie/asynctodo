#!/usr/bin/env python

from aiohttp import web
import ujson as json

TODOS = [
{"name": "Start this tutorial",
"finished": True},
{"name": "Finish this tutorial",
"finished": False},
]

async def get_all_todos(request):
    return web.json_response([
        {'id': idx, **todo} for idx, todo in enumerate(TODOS)
    ])

app = web.Application()
app.router.add_get("/", get_all_todos)

web.run_app(app)
