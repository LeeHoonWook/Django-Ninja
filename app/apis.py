from ninja.router import Router

ninja = Router()


@ninja.get("/hello")
def hello(request):
    return "Hello world"
