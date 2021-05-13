from socket import *

# Nome ou endereço IP e numero da porta socket do servidor 
server_name = 'server_name'
server_port = 8000
# Criando socket chamado client_socket com endereço tipo IPV4 e protocolo UDP
client_socket = socket(AF_INET, SOCK_DGRAM)
# Aplicacao...
message = input('Input lowercase sentence: ')
# Enviando mensagem ao servidor buscando endereço e porta socket
client_socket.sendto(message.encode(),(server_name, server_port))
# Recebimento da resposta do servidor mais seu endereço (do qual não necessitamos, pois já o temos)
modifiedMessage, serverAddress = client_socket.recvfrom(2048)
print (modifiedMessage)
# Encerrando socket
client_socket.close()



