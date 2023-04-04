import socket
import os
import sys

def is_safe(filename):
    """make sure only serve files from inside the static folder"""
    return os.path.normpath(filename) == filename and filename.startswith("static/")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind(("0.0.0.0", int(sys.argv[1])))

sock.listen(1)

while True:
    (conn, address) = sock.accept()
    print(address)
    request = conn.recv(10000).decode()
    lines = request.split('\r\n')
    a,filename,c = lines[0].split()
    if filename == '/':
        filename = "/index.html"
    filename = "static" + filename    
    if os.path.exists(filename) and is_safe(filename): 
        if filename.endswith(".txt") or filename.endswith(".html"):
            with open(filename) as stream:
                http_body = stream.read()
            http_headers = [
                "HTTP/1.1 200 OK",
                "Content-Type: text/html; charset=utf-8",
                "Content-Length: %s" % len(http_body),
                "Content-Language: en-US",
                "Date: Thu, 06 Dec 2018 17:37:18 GMT",
                "Server: my-very-own-little-server",
                ""
            ]
            data = "\r\n".join(http_headers) + "\r\n" + http_body
            conn.send(data.encode())
            conn.close()
        elif filename.endswith(".jpeg"):
            with open(filename, "rb") as stream:
                http_body = stream.read()

            http_headers = [
                "HTTP/1.1 200 OK",
                "Content-Type: image/jpeg; charset=utf-8",
                "Content-Length: %s" % len(http_body),
                "Content-Language: en-US",
                "Date: Thu, 06 Dec 2018 17:37:18 GMT",
                "Server: my-very-own-little-server",
                ""
            ]
            data = "\r\n".join(http_headers).encode() + b"\r\n" + http_body
            conn.send(data)
            conn.close()
        else:
            http_headers = [
                "HTTP/1.1 500 INTERNAL SERVER ERROR",
                ""
                "Cannot handle this type of data"
            ]
            conn.send("\r\n".join(http_headers).encode())
            conn.close()

    else:
        http_headers = [
            "HTTP/1.1 404 NOT FOUND",
            ""
            "This file does not exist"
        ]
        conn.send("\r\n".join(http_headers).encode())
        conn.close()
