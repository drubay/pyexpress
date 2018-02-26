from pyexpress.httpserverhelper import HttpServerHelper

PORT = 8080


def use_hello(req, res, next):
    print("USE /hello")
    next()


def use_hello_no_next(req, res, next):
    print("USE /hello/use")
    if not next():
        res.status(200).send('OK! OK! No next...'.encode('UTF-8'))


def post_hello(req, res, next):
    print("POST /hello")
    print("body: " + str(req.body))
    res.status(204).send()


def get_hello(req, res, next):
    print("GET /hello/:helloId")
    print("helloId: " + req.path_params['helloId'])
    res.status(200).send('Hello'.encode('UTF-8'))


def put_hello(req, res, next):
    print("PUT /hello?helloId=1&value=world")
    print("helloId: " + req.query_params['helloId'] + ", value: " + req.query_params['value'])
    res.status(200).send('Hello? World!'.encode('UTF-8'))


def delete_hello(req, res, next):
    print("DELETE /hello")
    res.status(404).send('Hello not found'.encode('UTF-8'))


def run():
    HttpServerHelper.use("/hello/use", use_hello_no_next)
    HttpServerHelper.use("/hello", use_hello)
    HttpServerHelper.post("/hello", post_hello)
    HttpServerHelper.get("/hello/:helloId", get_hello)
    HttpServerHelper.put("/hello", put_hello)
    HttpServerHelper.delete("/hello", delete_hello)
    HttpServerHelper.static()
    HttpServerHelper.start(PORT)


run()

try:
    while True:
        pass
except KeyboardInterrupt:
    pass
