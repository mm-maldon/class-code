import socket
import os
import sys

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
    if os.path.exists(filename):       
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


"""
b"GET / HTTP/1.1",
b"Host: 127.0.0.1:8000",
b"Connection: keep-alive",
b"User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Code/1.74.2 Chrome/102.0.5005.167 Electron/19.1.8 Safari/537.36",
b"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
b"Accept-Encoding: gzip, deflate, br",
b"Accept-Language: en-US",
b""
"""


