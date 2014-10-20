from socket import *
import impacket
from impacket import ImpactDecoder

# cl interface
usrInput = input('argh matie! establish tis protocol: ')

# serverPort = 12000
protocolNum = getprotobyname(usrInput) # get port num
serverSocket = socket(AF_INET, SOCK_RAW, protocolNum)
serverSocket(IPPROTO_IP, IP_HDRINCL, 1)
# serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print "The server is ready to recieve"

decoder = ImpactDecoder.IPDecoder()

while 1:
	# decode and print packet
	packet = serverSocket.recvfrom(4096)[0]
	packet = decoder.decode(packet)
	print packet

	connectionSocket, addr = serverSocket.accept()
	sentence = connectionSocket.recv(1024)
	capitalizedSentence = sentence.upper()
	connectionSocket.send(capitalizedSentence)
	connectionSocket.close()
