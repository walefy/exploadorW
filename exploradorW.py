from os import popen, chdir, system, path, rename, getcwd, remove, listdir, name
from time import sleep

chdir(path.expanduser('~'))

def clear():
	if name == 'nt':
		system('cls')
	else:
		#print("\x1b[2J\x1b[1;1H", end="")
		system('clear')

clear()

def listar():
	global saida_lista

	clear()

	saida_lista = listdir('.')

	for item in tuple(saida_lista):
		if item[:1] == '.':
			saida_lista.remove(item)


	print(f'{getcwd()}\n')

	for c in range(0, len(saida_lista)):
		print(f'[{c}] {saida_lista[c]}')

def abrir(n):
	if n.isnumeric():
		n = int(n)
		local = getcwd()


		try:
			if path.isdir(f'{local}/{saida_lista[n]}'):
				chdir(f'{local}/{saida_lista[n]}')

			elif path.isfile(f'{local}/{saida_lista[n]}'):
				menu(f'{local}/{saida_lista[n]}')

		except:
			print('Algo deu errado!')
			sleep(3)
		

		listar()

	elif n == '':
		listar()

	elif n == 'help':
		system('clear')
		print('[*] para voltar digite back')
		print('[*] para listar digite list')
		print('[*] para sair digite quit')

	elif n == 'back':
		chdir('..')
		listar()

	elif n == 'list':
		listar()

	elif n == 'quit':
		clear()
		quit()

	else:
		clear()
		print('Comado inexistente! Tente help')

def menu(caminho):
	clear()
	print(caminho + '\n')
	print('[0] cancelar')
	print('[1] abrir arquivo')
	print('[2] excluir arquivo')
	print('[3] renomear arquivo')

	subcmd = int(input('\n' + '>> '))

	if subcmd == 0:
		pass

	elif subcmd == 1:
		system(f'thunar {caminho}')

	elif subcmd == 2:
		escolha = input('deseja apagar o arquivo? [y/n] ').lower()

		if escolha == 'y':
			remove(f'{caminho}')

	elif subcmd == 3:
		escolha = input('digite o novo nome do arquivo: ')
		escolha2 = input(f'você deseja renomear o arquivo {caminho.split("/")[-1]} para {escolha}? [y/n] ').lower()

		if escolha2 == 'y':
			rename(caminho, escolha)


listar()

while True:
	cmd = input('\n' + '>> ')
	abrir(cmd)
