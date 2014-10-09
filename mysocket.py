class mysocket:
  def __init__(self, s=None):
    if s is None:
      self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    else:
      self.s = s

  def connect(self, host, port):
    self.s.connect((host,port))

  def mysend(self, msg):
    totalsent = 0
    while totalsent < MSGLEN:
      sent = self.sock.send(msg[totalsent:])
      if sent == 0:
        raise RuntimeError("socket connection broken")
      totalsent = totalsent + sent

  def myrecive(self):
    chunks = []
    bytes_recd = 0
    while bytes-recd < MSGLEN:
      chunks = self.s.recv(min(MSGLEN - bytes_recd, 2048))
      if chunks == "":
        raise RuntimeError("socket connection broken")
      chunks.append(chunk)
      bytes_recd = bytes_recd + len(chunk)
    return ''.join(chunks)
