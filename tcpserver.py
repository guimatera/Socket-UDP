from socket import *

server_port = 8000
server_socket = socket(AF_INET,SOCK_STREAM)
# Cria socket no numero da porta declarada
server_socket.bind(('', server_port))
# Nessa parte, o programa 'escuta' as requisições do cliente. 1 é o numero máximo de conexoes em fila.
server_socket.listen(1)
print ('The server is ready to receive')
# Loop para manter servidor pronto para receber/enviar mensagens para algum cliente
while 1:
    connection_socket, addr = server_socket.accept()
    sentence = connection_socket.recv(2048)
    capitalized_sentence = sentence.upper()
    connection_socket.send(capitalized_sentence)
    # Encerra a conexão TCP com o cliente
    connection_socket.close()
