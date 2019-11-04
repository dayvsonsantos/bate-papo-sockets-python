import socket
import sys
import threading
import os
from cryptography import AESciph
from cryptography import RSAciph
from cryptography import RSA
import json

aes = AESciph()
rsa = RSAciph()

SERVIDOR_KEY = ''

class Cliente:
	'''Usuário do bate-papo'''

	def __init__(self, host = '127.0.0.1', port = 9999):
		'''Inicializa as variáveis iniciais do cliente'''
		self.host = host
		self.port = port

	def envia_mensagem(self, serv_key):
		'''Envia mensagem ao servidor'''
		
		'''
		len(xxx)(xxx):
		{
			chave: crypto
			mesagem: crypto
		}
		'''

		#try:
		while True:
			msg = input('>-==: ')
			
			msg_encr, aes_key = aes.encrypto(msg)
			serv_key = RSA.importKey(serv_key)
			aes_key_encr = rsa.encrypto(aes_key, serv_key)

			self.s.sendall(bytes(msg_encr))

			#self.s.send(msg.encode('utf-8'))
			is_saida = msg.split() #Coloca as substrings da mensagem numa lista
			if not is_saida:
				continue 
			if is_saida[0] == '/tchau':
				self.s.close()
				os._exit(1)
		# except: #Trata o CTRL+C
		# 	print("Erro: envio de mesagem errada")
		# 	msg = '/tchau'
		# 	self.s.send(msg.encode('utf-8'))
		# 	self.s.close()
		# 	os._exit(1)


	def feedback_servidor(self):
		'''Recebe mensagem do servidor'''
		while True:
			msg = self.s.recv(4096).decode('utf-8')
			if msg == '/SERVIDOR_OFF': #Servidor por algum motivo encerrou
				print('Encerrando conexão, servidor está OFF.')
				self.s.close()
				os._exit(1)			
			if msg.startswith('/BANIDO'):
				print(' '.join(msg.split()[1:]))
				self.s.close()
				os._exit(1)
			print (msg)
			input("Apelido: ")

	def cria_conexao_tcp(self):
		'''Cria conexão TCP com o servidor'''
		try:
			self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	#Cria a conexão TCP 
		except:
			print('Erro ao criar o socket')
			os._exit(1)

		dest = (self.host, self.port)
		try:
			self.s.connect(dest)	#conecta ao servidor

		except:
			print("Servidor não está conectado no momento.")
			sys.exit()


	def main(self):
		'''Começa a execução do cliente, conecta socket TCP '''

		self.cria_conexao_tcp()

		SERVIDOR_KEY = self.s.recv(2048).decode('utf-8')
		self.s.send(rsa.get_public_key().exportKey('PEM'))
		#print(pbkey_servidor)
		msg = self.s.recv(4096).decode('utf-8')
		print(msg)
		apelido = input("Apelido: ")
		self.s.sendall(apelido.encode('utf-8'))

		thread = threading.Thread(target = self.feedback_servidor)
		thread.start()
		self.envia_mensagem(SERVIDOR_KEY)
		

if __name__ == "__main__":
	cliente = Cliente()
	cliente.main()

	# SERVIDOR_KEY = rsa.get_public_key()

	# msg = "oi"

	# msg_encr, aes_key = aes.encrypto(msg) # bytes
	# print(aes_key)
	# key_encr = rsa.encrypto(aes_key, SERVIDOR_KEY) # bytes

	# print(type(key_encr))
	# print(type(msg_encr))

	# print(key_encr)
	# print(msg_encr)

	# print(rsa.decrypto(key_encr).decode('utf-8'))
	# print(aes.decrypto(msg_encr, rsa.decrypto(key_encr).decode('utf-8')).decode('utf-8'))
	
	