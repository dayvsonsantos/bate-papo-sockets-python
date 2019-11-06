import socket
import sys
import threading
import os
import time

from cryptography import AESciph
from cryptography import RSAciph
from cryptography import RSA


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
		#try:
		# importanto a chave do servidor
		serv_key = RSA.importKey(serv_key)

		while True:
			msg = input()

			print('\nEncriptando mensagem...')
			msg_encr, aes_key, aes_iv = aes.encrypto(msg)
			print(f'MSG ENCRIPTO = {msg_encr}\n')
			
			print(f'AES KEY = {aes_key}')
			print(f'AES IV = {aes_iv}\n')

			print('encriptando chave...')
			aes_key_encr = rsa.encrypto(aes_key, serv_key)
			print(f'KEY ENCRIPTO = {aes_key_encr}\n')

			print('encriptando iv...')
			aes_iv_encr = rsa.encrypto(aes_iv, serv_key)
			print(f'IV ENCRIPTO = {aes_iv_encr}\n')


			print(f'envidando mensagem...')
			self.s.sendall(msg_encr)
			time.sleep(0.5)
			print(f'envidando chave...')
			self.s.sendall(aes_key_encr)
			time.sleep(0.5)
			print(f'envidando iv...\n')
			self.s.sendall(aes_iv_encr)
			time.sleep(0.5)
			print('mensagem enviada!!!')


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

	def recebe_msg_chave_iv(self):
		msg = self.s.recv(10240)
		print(f'\nMensagem recebida encriptografada = {msg}\n')
		time.sleep(0.5)

		key = self.s.recv(6144)
		print(f'Chave recebida encriptografada = {key}\n')
		time.sleep(0.5)

		iv = self.s.recv(6144)
		print(f'iv recebida encriptografada = {iv}\n')

		key = rsa.decrypto(key).decode('utf-8')
		print(f'chave decriptografada = {key}')

		iv = rsa.decrypto(iv).decode('utf-8')
		print(f'iv decriptografada = {iv}')

		msg = aes.decrypto(msg, key, iv).decode('utf-8')
		print(f'mensagem decriptografada = {msg}\n')

	def recebe_mensagem_do_servidor(self):
		'''Recebe mensagem do servidor'''
		while True:
			msg = self.s.recv(4096).decode('utf-8')
			time.sleep(0.5)
			if msg == '/SERVIDOR_OFF': #Servidor por algum motivo encerrou
				print('Encerrando conexão, servidor está OFF.')
				self.s.close()
				os._exit(1)			
			elif msg.startswith('/BANIDO'):
				print(' '.join(msg.split()[1:]))
				self.s.close()
				os._exit(1)
			elif msg == '/vaichave':	
				self.recebe_msg_chave_iv()
			else:
				print (msg)

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

		print('pegando a chave publica do servidor...')
		SERVIDOR_KEY = self.s.recv(2048).decode('utf-8')
		self.s.send(rsa.get_public_key().exportKey('PEM'))
		
		# print('encriptando a mensagem...')
		# msg = 'oi'
		# serv_key = RSA.importKey(SERVIDOR_KEY)
		# print('enviado a mensagem critografada...')
		# msg_enc = rsa.encrypto(msg, serv_key)
		#self.s.send(msg_enc)
		
		from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit
		from PyQt5.QtGui import QIcon

		msg = self.s.recv(4096).decode('utf-8')
		apelido = input("Apelido: ")	
		self.s.sendall(apelido.encode('utf-8'))

		thread = threading.Thread(target = self.recebe_mensagem_do_servidor)
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
	
	