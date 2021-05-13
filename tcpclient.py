from socket import *

# Nome ou endereço IP e numero da porta socket do servidor
server_name = 'servername'
server_port = 2021
# Criando socket chamado client_socket com endereço tipo IPV4 e protocolo TCP
client_socket = socket(AF_INET, SOCK_STREAM)
# Estabelecendo conexão com servidor antes do envio de dados
client_socket.connect((server_name,server_port))
# Enviando mensagem ao servidor 
sentence = input('Input lowercase sentence: ')
client_socket.send(sentence)
# Recebimento da resposta do servidor 
modified_sentence = client_socket.recv(2048)
print ('From Server: ', modified_sentence)
# Encerrando socket
client_socket.close()