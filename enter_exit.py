"""
__enter__ & __enit__ context manager.
"""


from socket import socket, AF_INET, SOCK_STREAM


class LazySocket(object):

    def __init__(self, address, family=AF_INET, stype=SOCK_STREAM):
        self.address = address
        self.family = family
        self.stype = stype
        self.sock = None

    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError("Already connected!")
        self.sock = socket(self.family, self.stype)
        self.sock.connect(self.address)
        return self.sock

    def __exit__(self, exc_ty, exc_val, exc_tb):
        self.sock.close()
        self.sock = None
        return False


conn = LazySocket(('www.python.org', 80))
with conn as c:
    # __enter__ executes
    c.send('GET /index.html HTTP/1.0\r\n')
    # __exit__ executes
