"""
Supporting functions for Comp 521 A4
October 2018
Gary Bishop
"""
from bottle import Bottle, ServerAdapter
import threading
import urllib.error
import urllib.request
import json
from IPython.lib.pretty import pprint

adapter = None
thread = None
ready = threading.Event()

host = '127.0.0.1'
port = 8080
root = f'http://{host}:{port}'


def makeURL(*parts):
    '''Construct the URL by joining the parts with /'''
    return '/' + '/'.join(str(part) for part in parts)


def getJson(*parts, method='get', postData=None):
    '''Submit a request and return the response for testing'''
    # construct the URL
    path = root + makeURL(*parts)
    # start the request object
    request = urllib.request.Request(path, method=method)
    # if we have data to post encode it properly
    if postData:
        # add the content header to signal json is coming
        request.add_header('Content-Type', 'application/json; charset=utf-8')
        # encode as json and then as utf-8 bytes
        postData = json.dumps(postData).encode('utf-8')
        # tell it the length of the data
        request.add_header('Content-Length', len(postData))

    result = None
    try:
        with urllib.request.urlopen(request, postData) as fp:
            code = fp.getcode()
            if code == 200:
                data = fp.read().decode('utf-8')
                result = json.loads(data)
    except urllib.error.HTTPError as e:
        code = e.code

    print(f'http response = {code}')
    if result:
        pprint(result, max_seq_length=8)
    return result or code


# https://stackoverflow.com/a/16056443/1115662
class MyWSGIRefServer(ServerAdapter):
    server = None

    def run(self, handler):
        from wsgiref.simple_server import make_server, WSGIRequestHandler
        if self.quiet:
            class QuietHandler(WSGIRequestHandler):
                def log_request(*args, **kw):
                    pass
            self.options['handler_class'] = QuietHandler
        self.server = make_server(self.host, self.port, handler,
                                  **self.options)
        ready.set()
        self.server.serve_forever()


app = Bottle()
adapter = MyWSGIRefServer(host=host, port=port)


def server():
    """Run the bottle server"""
    app.run(server=adapter)


thread = threading.Thread(target=server, daemon=True)
thread.start()
ready.wait()
