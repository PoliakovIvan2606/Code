from aiohttp import web
import aiohttp_jinja2  
import jinja2

# Это так для слобачков надо делать так как ниже
# async def index(request):
#     print(request)
#     data={'hello': 'world'}
#     return web.json_response(data=data)

# app = web.Application()
# app.add_routes([web.get('/', index)])
# web.run_app(app)


# Можно и через роутеры, сеорее всего так и надо
# routes = web.RouteTableDef()

# @routes.get('/{name}')
async def hello(request):
    return web.json_response(data={'data':request.match_info['name']})

async def index(request):
    name = request.query['name']
    return web.json_response(data={'data': name})

@aiohttp_jinja2.template('index.html')
async def jinja_index(request):
    return {}

app = web.Application()
app.add_routes([#web.get('/{name}', hello), 
                web.get('/', index), 
                web.get('/index', jinja_index)])
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('templates'))

if __name__ == '__main__':
    web.run_app(app, host='localhost', port=8000)