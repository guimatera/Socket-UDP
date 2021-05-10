from sockets import *

server_port = 12000
server_socket = socket(AF_INET, SOCK_DGRAM)
# Cria socket no numero da porta declarada
server_socket.bind(['', server_port])
print ('The server is ready to receive')
# Loop para manter servidor pronto para receber/enviar menssagens para algum cliente
while 1:
    message, client_address = server_socket.recvfrom(2048)
    modified_message = message.upper()
    server_socket.sendto(modified_message, client_address)