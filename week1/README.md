Read more info about HTTP:

https://developer.mozilla.org/en-US/docs/Web/HTTP/Session

# Url parsing

    URL: http://example.com:80/index#something?name=hello
         ====   =========== == ===== ========= ==========
    http or https (scheme)
    example.com   (domain name) -> 127.0.0.1 (ipv4 address aka AF_INET)
    80            (port for http)
    443           (port for https - ssl)
    /index        (path_info)
    ?name=hello   (query_string)
    #something    (hash)

# Example HTTP client

    # create an INET, STREAMing socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # now connect to the web server on port 80 - the normal http port
    s.connect(("www.python.org", 80))

# Example HTTP server

    # create an INET, STREAMing socket
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # bind the socket to a public host, and a well-known port
    serversocket.bind((socket.gethostname(), 80))
    # become a server socket listening to up to 1 client
    serversocket.listen(1)
    while True:
        # accept connections from outside
        (clientsocket, address) = serversocket.accept()
	data = clientsocket.recv(10000)
	response = "..."
	clientsocket.send(response)	
