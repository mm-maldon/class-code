import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind(("0.0.0.0", 8000))

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

    with open(filename) as stream:
        message = stream.read()
    lines = [
        "HTTP/1.1 200 OK",
        "Content-Type: text/html; charset=utf-8",
        "Content-Length: %s" % len(message),
        "Content-Language: en-US",
        "Date: Thu, 06 Dec 2018 17:37:18 GMT",
        "Server: my-very-own-little-server",
        ""
    ]
    data = "\r\n".join(lines) + "\r\n" + message
    conn.send(data.encode())

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


