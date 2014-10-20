## test
## 10/8/14

import socket

# create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind s to a public host and port 80
s.bind((socket.gethostname(), 80))
s.listen(5)

while 1:
  # accept connections from outside
  (clientsocket, address) = s.accept()
  ct = client_thread(clientsocket)
  ct.run()
