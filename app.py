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

async def get_one_todo(request):
    id = int(request.match_info["id"])
    if id >= len(TODOS):
        return web.json_response({"error": "Todo not found"}, status=404)
    return web.json_response({"id":id, **TODOS[id]})



def app_factory(args=()):
    app = web.Application()
    app.router.add_get("/todos/", get_all_todos)
    app.router.add_get('/todos/{id:\d+}', get_one_todo, name='one_todo')
    return web.run_app(app)

if __name__ == "__main__":
    app_factory()

#web.run_app(app)
