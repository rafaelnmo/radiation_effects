import fileinput, os
import re

#valor1 = valor2 = 0
flag = 0

#=====================FUNCAO: converte as strings para floats==================================
def multiplyer_prefix(unidade, float_value):
	if unidade == 'c':
		float_value = float_value * 10**-2
	elif unidade == 'm':
		float_value = float_value * 10**-3
	elif unidade == 'u':
		float_value = float_value * 10**-6
	elif unidade == 'p':
		float_value = float_value * 10**-9

	return float_value

#======================FUNCAO: convert string para float=======================================
def converter(value):
	# print(value)
	# print(value[-1])
	unidade = value[-1]
	value = value[:-1]
	# print(value)
	float_value = float(value)
	float_converted = multiplyer_prefix(unidade, float_value)
	#print(float_converted)
	#print(unidade)

	return float_converted

#====FUNCAO: le o arquivo da simulacao e busca os valores "v_saida_xor" e v_invert_invert======
def funct_read_fileText(fileName):
	# print("ENTREEEEEEI")
	fileText = open(fileName, "r+")
	valor1 = valor2 = 0
	#flag = 0
	for line in fileText:
		#print("ESTOU NA LINHA")
		#print(line)
		line.strip().split('\n')
		if "v_saida_xor" in line:
			string_value = line.strip().split('=')
			# print(string_value)
			# print(string_value[-1])
			# print("ACHEI XOR")
			valor1 = converter(string_value[-1])

		if "v_saida_inv" in line:
			string_value = line.strip().split('=')
			valor2 = converter(string_value[-1])
	# print(valor1 - valor2)		
	if (abs(valor1 - valor2)) >= 0.035:
		# print("ENNNNNNTREI")
		#print(valor1)
		return 0
	#print("NAAAAAAo ENNNNNNTREI")
	return 1	

	#print("flag = ", flag)

	fileText.close()

#===========FUNCAO: insere os diferentes valores em A e B (tabela verdade XOR)=================
def pulse_insert(pulso):
	pulse_value = " "
	if pulso == 0:
		pulse_value = "00"
		# print("pulse = 00")
		filepath = 'fontes.cir' #Pensar em colocar essa linha fora do if-else
		with open(filepath, 'r+') as fp:
			lines = fp.read()
			linesVect = lines.split('\n')
			fp.seek(0)
			fp.truncate()
			linesVect[11] = 'Va a gnd 0'
			linesVect[12] = 'Vb b gnd 0'
			x = '\n'.join(linesVect)
			fp.write(x)
			fp.close()
	elif pulso == 1:
		# print("pulse = 01")
		pulse_value = "01"
		filepath = 'fontes.cir'
		with open(filepath, 'r+') as fp:
			lines = fp.read()
			linesVect = lines.split('\n')
			fp.seek(0)
			fp.truncate()
			linesVect[11] = 'Va a gnd 0'
			linesVect[12] = 'Vb b gnd 0.7'
			x = '\n'.join(linesVect)
			fp.write(x)
			fp.close()
	elif pulso == 2:
		# print("pulse = 10")
		pulse_value = "10"
		filepath = 'fontes.cir'
		with open(filepath, 'r+') as fp:
			lines = fp.read()
			linesVect = lines.split('\n')
			fp.seek(0)
			fp.truncate()
			linesVect[11] = 'Va a gnd 0.7'
			linesVect[12] = 'Vb b gnd 0'
			x = '\n'.join(linesVect)
			fp.write(x)
			fp.close()
	else:
		# print("pulse = 11")
		pulse_value = "11"
		filepath = 'fontes.cir'
		with open(filepath, 'r+') as fp:
			lines = fp.read()
			linesVect = lines.split('\n')
			fp.seek(0)
			fp.truncate()
			linesVect[11] = 'Va a gnd 0.7'
			linesVect[12] = 'Vb b gnd 0.7'
			x = '\n'.join(linesVect)
			fp.write(x)
			fp.close()
	return pulse_value		
#==========FUNCAO:insere os diferentes valores de temperatura (25, 50, 75, 100, 125)===========
def temperature_insert(temp):
	filepath = 'xor.cir'
	with open(filepath, 'r+') as fp:
		lines = fp.read()
		linesVect = lines.split('\n')
		fp.seek(0)
		fp.truncate()
		linesVect[45] = '.temp ' + str(temp)
		x = '\n'.join(linesVect)
		#print(x)
		fp.write(x)
		fp.close()

#==========FUNCAO: insere as diferentes versoes XOR(V1,V2,V3,V4,V5,V6,V7,V8,V9)================
def version_insert(version):
	if version == 0:
		#print("version = XORV1")
		filepath = 'xor.cir' #Pensar em colocar essa linha fora do if-else
		with open(filepath, 'r+') as fp:
			lines = fp.read()
			linesVect = lines.split('\n')
			fp.seek(0)
			fp.truncate()
			linesVect[25] = 'Xinv_a buff_a buff_not_a vdd1 gnd inversor'
			linesVect[26] = 'Xinv_b buff_b buff_not_b vdd1 gnd inversor'
			linesVect[30] = 'Xxor_v1 buff_a buff_not_a buff_b buff_not_b xor vdd2 gnd xor_v1'
			linesVect[31] = '*Xxor_v2 buff_a buff_b xor vdd2 gnd xor_v2'
			linesVect[32] = '*Xxor_v3 buff_a buff_b xor vdd2 gnd xor_v3'
			linesVect[33] = '*Xxor_v4 buff_a buff_b xor vdd2 gnd xor_v4'
			linesVect[34] = '*Xxor_v5 buff_a buff_not_a buff_b buff_not_b xor vdd2 gnd xor_v5'
			linesVect[35] = '*Xxor_v6 buff_a buff_not_a buff_b buff_not_b xor vdd2 gnd xor_v6'
			linesVect[36] = '*Xxor_v7 buff_a buff_not_a buff_b buff_not_b xor vdd2 gnd xor_v7'
			linesVect[37] = '*Xxor_v8 buff_a buff_b xor vdd2 gnd xor_v8'
			linesVect[38] = '*Xxor_v9 buff_a buff_b buff_not_b xor vdd2 gnd xor_v9'

			x = '\n'.join(linesVect)
			fp.write(x)
			fp.close()
	elif version == 1:
		#print("version = XORV2")
		filepath = 'xor.cir'
		with open(filepath, 'r+') as fp:
			lines = fp.read()
			linesVect = lines.split('\n')
			fp.seek(0)
			fp.truncate()
			linesVect[25] = '*Xinv_a buff_a buff_not_a vdd1 gnd inversor'
			linesVect[26] = '*Xinv_b buff_b buff_not_b vdd1 gnd inversor'
			linesVect[30] = '*Xxor_v1 buff_a buff_not_a buff_b buff_not_b xor vdd2 gnd xor_v1'
			linesVect[31] = 'Xxor_v2 buff_a buff_b xor vdd2 gnd xor_v2'
			linesVect[32] = '*Xxor_v3 buff_a buff_b xor vdd2 gnd xor_v3'
			linesVect[33] = '*Xxor_v4 buff_a buff_b xor vdd2 gnd xor_v4'
			linesVect[34] = '*Xxor_v5 buff_a buff_not_a buff_b buff_not_b xor vdd2 gnd xor_v5'
			linesVect[35] = '*Xxor_v6 buff_a buff_not_a buff_b buff_not_b xor vdd2 gnd xor_v6'
			linesVect[36] = '*Xxor_v7 buff_a buff_not_a buff_b buff_not_b xor vdd2 gnd xor_v7'
			linesVect[37] = '*Xxor_v8 buff_a buff_b xor vdd2 gnd xor_v8'
			linesVect[38] = '*Xxor_v9 buff_a buff_b buff_not_b xor vdd2 gnd xor_v9'

			x = '\n'.join(linesVect)
			fp.write(x)
			fp.close()
	elif version == 2:
		#print("version = XORV3")
		filepath = 'xor.cir'
		with open(filepath, 'r+') as fp:
			lines = fp.read()
			linesVect = lines.split('\n')
			fp.seek(0)
			fp.truncate()
			linesVect[25] = '*Xinv_a buff_a buff_not_a vdd1 gnd inversor'
			linesVect[26] = '*Xinv_b buff_b buff_not_b vdd1 gnd inversor'
			linesVect[30] = '*Xxor_v1 buff_a buff_not_a buff_b buff_not_b xor vdd2 gnd xor_v1'
			linesVect[31] = '*Xxor_v2 buff_a buff_b xor vdd2 gnd xor_v2'
			linesVect[32] = 'Xxor_v3 buff_a buff_b xor vdd2 gnd xor_v3'
			linesVect[33] = '*Xxor_v4 buff_a buff_b xor vdd2 gnd xor_v4'
			linesVect[34] = '*Xxor_v5 buff_a buff_not_a buff_b buff_not_b xor vdd2 gnd xor_v5'
			linesVect[35] = '*Xxor_v6 buff_a buff_not_a buff_b buff_not_b xor vdd2 gnd xor_v6'
			linesVect[36] = '*Xxor_v7 buff_a buff_not_a buff_b buff_not_b xor vdd2 gnd xor_v7'
			linesVect[37] = '*Xxor_v8 buff_a buff_b xor vdd2 gnd xor_v8'
			linesVect[38] = '*Xxor_v9 buff_a buff_b buff_not_b xor vdd2 gnd xor_v9'

			x = '\n'.join(linesVect)
			fp.write(x)
			fp.close()
	elif version == 3:
		#print("version = XORV4")
		filepath = 'xor.cir'
		with open(filepath, 'r+') as fp:
			lines = fp.read()
			linesVect = lines.split('\n')
			fp.seek(0)
			fp.truncate()
			linesVect[25] = '*Xinv_a buff_a buff_not_a vdd1 gnd inversor'
			linesVect[26] = '*Xinv_b buff_b buff_not_b vdd1 gnd inversor'
			linesVect[30] = '*Xxor_v1 buff_a buff_not_a buff_b buff_not_b xor vdd2 gnd xor_v1'
			linesVect[31] = '*Xxor_v2 buff_a buff_b xor vdd2 gnd xor_v2'
			linesVect[32] = '*Xxor_v3 buff_a buff_b xor vdd2 gnd xor_v3'
			linesVect[33] = 'Xxor_v4 buff_a buff_b xor vdd2 gnd xor_v4'
			linesVect[34] = '*Xxor_v5 buff_a buff_not_a buff_b buff_not_b xor vdd2 gnd xor_v5'
			linesVect[35] = '*Xxor_v6 buff_a buff_not_a buff_b buff_not_b xor vdd2 gnd xor_v6'
			linesVect[36] = '*Xxor_v7 buff_a buff_not_a buff_b buff_not_b xor vdd2 gnd xor_v7'
			linesVect[37] = '*Xxor_v8 buff_a buff_b xor vdd2 gnd xor_v8'
			linesVect[38] = '*Xxor_v9 buff_a buff_b buff_not_b xor vdd2 gnd xor_v9'

			x = '\n'.join(linesVect)
			fp.write(x)
			fp.close()
	elif version == 4:
		#print("version = XORV5")
		filepath = 'xor.cir'
		with open(filepath, 'r+') as fp:
			lines = fp.read()
			linesVect = lines.split('\n')
			fp.seek(0)
			fp.truncate()
			linesVect[25] = 'Xinv_a buff_a buff_not_a vdd1 gnd inversor'
			linesVect[26] = 'Xinv_b buff_b buff_not_b vdd1 gnd inversor'
			linesVect[30] = '*Xxor_v1 buff_a buff_not_a buff_b buff_not_b xor vdd2 gnd xor_v1'
			linesVect[31] = '*Xxor_v2 buff_a buff_b xor vdd2 gnd xor_v2'
			linesVect[32] = '*Xxor_v3 buff_a buff_b xor vdd2 gnd xor_v3'
			linesVect[33] = '*Xxor_v4 buff_a buff_b xor vdd2 gnd xor_v4'
			linesVect[34] = 'Xxor_v5 buff_a buff_not_a buff_b buff_not_b xor vdd2 gnd xor_v5'
			linesVect[35] = '*Xxor_v6 buff_a buff_not_a buff_b buff_not_b xor vdd2 gnd xor_v6'
			linesVect[36] = '*Xxor_v7 buff_a buff_not_a buff_b buff_not_b xor vdd2 gnd xor_v7'
			linesVect[37] = '*Xxor_v8 buff_a buff_b xor vdd2 gnd xor_v8'
			linesVect[38] = '*Xxor_v9 buff_a buff_b buff_not_b xor vdd2 gnd xor_v9'

			x = '\n'.join(linesVect)
			fp.write(x)
			fp.close()
	elif version == 5:
		#print("version = XORV6")
		filepath = 'xor.cir'
		with open(filepath, 'r+') as fp:
			lines = fp.read()
			linesVect = lines.split('\n')
			fp.seek(0)
			fp.truncate()
			linesVect[25] = 'Xinv_a buff_a buff_not_a vdd1 gnd inversor'
			linesVect[26] = 'Xinv_b buff_b buff_not_b vdd1 gnd inversor'
			linesVect[30] = '*Xxor_v1 buff_a buff_not_a buff_b buff_not_b xor vdd2 gnd xor_v1'
			linesVect[31] = '*Xxor_v2 buff_a buff_b xor vdd2 gnd xor_v2'
			linesVect[32] = '*Xxor_v3 buff_a buff_b xor vdd2 gnd xor_v3'
			linesVect[33] = '*Xxor_v4 buff_a buff_b xor vdd2 gnd xor_v4'
			linesVect[34] = '*Xxor_v5 buff_a buff_not_a buff_b buff_not_b xor vdd2 gnd xor_v5'
			linesVect[35] = 'Xxor_v6 buff_a buff_not_a buff_b buff_not_b xor vdd2 gnd xor_v6'
			linesVect[36] = '*Xxor_v7 buff_a buff_not_a buff_b buff_not_b xor vdd2 gnd xor_v7'
			linesVect[37] = '*Xxor_v8 buff_a buff_b xor vdd2 gnd xor_v8'
			linesVect[38] = '*Xxor_v9 buff_a buff_b buff_not_b xor vdd2 gnd xor_v9'

			x = '\n'.join(linesVect)
			fp.write(x)
			fp.close()
	elif version == 6:
		#print("version = XORV7")
		filepath = 'xor.cir'
		with open(filepath, 'r+') as fp:
			lines = fp.read()
			linesVect = lines.split('\n')
			fp.seek(0)
			fp.truncate()
			linesVect[25] = 'Xinv_a buff_a buff_not_a vdd1 gnd inversor'
			linesVect[26] = 'Xinv_b buff_b buff_not_b vdd1 gnd inversor'
			linesVect[30] = '*Xxor_v1 buff_a buff_not_a buff_b buff_not_b xor vdd2 gnd xor_v1'
			linesVect[31] = '*Xxor_v2 buff_a buff_b xor vdd2 gnd xor_v2'
			linesVect[32] = '*Xxor_v3 buff_a buff_b xor vdd2 gnd xor_v3'
			linesVect[33] = '*Xxor_v4 buff_a buff_b xor vdd2 gnd xor_v4'
			linesVect[34] = '*Xxor_v5 buff_a buff_not_a buff_b buff_not_b xor vdd2 gnd xor_v5'
			linesVect[35] = '*Xxor_v6 buff_a buff_not_a buff_b buff_not_b xor vdd2 gnd xor_v6'
			linesVect[36] = 'Xxor_v7 buff_a buff_not_a buff_b buff_not_b xor vdd2 gnd xor_v7'
			linesVect[37] = '*Xxor_v8 buff_a buff_b xor vdd2 gnd xor_v8'
			linesVect[38] = '*Xxor_v9 buff_a buff_b buff_not_b xor vdd2 gnd xor_v9'

			x = '\n'.join(linesVect)
			fp.write(x)
			fp.close()
	elif version == 7:
		#print("version = XORV8")
		filepath = 'xor.cir'
		with open(filepath, 'r+') as fp:
			lines = fp.read()
			linesVect = lines.split('\n')
			fp.seek(0)
			fp.truncate()
			linesVect[25] = '*Xinv_a buff_a buff_not_a vdd1 gnd inversor'
			linesVect[26] = '*Xinv_b buff_b buff_not_b vdd1 gnd inversor'
			linesVect[30] = '*Xxor_v1 buff_a buff_not_a buff_b buff_not_b xor vdd2 gnd xor_v1'
			linesVect[31] = '*Xxor_v2 buff_a buff_b xor vdd2 gnd xor_v2'
			linesVect[32] = '*Xxor_v3 buff_a buff_b xor vdd2 gnd xor_v3'
			linesVect[33] = '*Xxor_v4 buff_a buff_b xor vdd2 gnd xor_v4'
			linesVect[34] = '*Xxor_v5 buff_a buff_not_a buff_b buff_not_b xor vdd2 gnd xor_v5'
			linesVect[35] = '*Xxor_v6 buff_a buff_not_a buff_b buff_not_b xor vdd2 gnd xor_v6'
			linesVect[36] = '*Xxor_v7 buff_a buff_not_a buff_b buff_not_b xor vdd2 gnd xor_v7'
			linesVect[37] = 'Xxor_v8 buff_a buff_b xor vdd2 gnd xor_v8'
			linesVect[38] = '*Xxor_v9 buff_a buff_b buff_not_b xor vdd2 gnd xor_v9'

			x = '\n'.join(linesVect)
			fp.write(x)
			fp.close()
	else:
		#print("version = XORV9")
		filepath = 'xor.cir'
		with open(filepath, 'r+') as fp:
			lines = fp.read()
			linesVect = lines.split('\n')
			fp.seek(0)
			fp.truncate()
			linesVect[25] = '*Xinv_a buff_a buff_not_a vdd1 gnd inversor'
			linesVect[26] = 'Xinv_b buff_b buff_not_b vdd1 gnd inversor'
			linesVect[30] = '*Xxor_v1 buff_a buff_not_a buff_b buff_not_b xor vdd2 gnd xor_v1'
			linesVect[31] = '*Xxor_v2 buff_a buff_b xor vdd2 gnd xor_v2'
			linesVect[32] = '*Xxor_v3 buff_a buff_b xor vdd2 gnd xor_v3'
			linesVect[33] = '*Xxor_v4 buff_a buff_b xor vdd2 gnd xor_v4'
			linesVect[34] = '*Xxor_v5 buff_a buff_not_a buff_b buff_not_b xor vdd2 gnd xor_v5'
			linesVect[35] = '*Xxor_v6 buff_a buff_not_a buff_b buff_not_b xor vdd2 gnd xor_v6'
			linesVect[36] = '*Xxor_v7 buff_a buff_not_a buff_b buff_not_b xor vdd2 gnd xor_v7'
			linesVect[37] = '*Xxor_v8 buff_a buff_b xor vdd2 gnd xor_v8'
			linesVect[38] = 'Xxor_v9 buff_a buff_b buff_not_b xor vdd2 gnd xor_v9'

			x = '\n'.join(linesVect)
			fp.write(x)
			fp.close()

#==============FUNCAO: modifica o valor do pulso de corrente===================================

def increment_current(signal, currentValue):
	# print("increment_current")
	# print(signal)
	# print(currentValue)
	if(signal == 0 or signal ==3):
		filepath = 'xor.cir'
		with open(filepath, 'r+') as fp:
			lines = fp.read()
			linesVect = lines.split('\n')
			fp.seek(0)
			fp.truncate()
			linesVect[14] = 'Iset gnd xor EXP (0 '+str(currentValue)+'u 4ns 10ps 10ps 200ps)'
			# print(linesVect[14])
			linesVect[16] = '*Iset xor gnd EXP (0 29u 4ns 10ps 10ps 200ps)'
			x = '\n'.join(linesVect)
			#print(currentValue)
			fp.write(x)
			fp.close()
	else:
		filepath = 'xor.cir'
		with open(filepath, 'r+') as fp:
			lines = fp.read()
			linesVect = lines.split('\n')
			fp.seek(0)
			fp.truncate()
			linesVect[14] = '*Iset gnd xor EXP (0 28u 4ns 10ps 10ps 200ps)'
			linesVect[16] = 'Iset xor gnd EXP (0 '+str(currentValue)+'u 4ns 10ps 10ps 200ps)'
			x = '\n'.join(linesVect)
			#print(currentValue)
			fp.write(x)
			fp.close()

'''
def altera_text(valor1, valor2):
	filepath = 'text.txt'
	with open(filepath, 'r+') as fp:
		lines = fp.read()
		linesVect = lines.split('\n')
		fp.seek(0)
		fp.truncate()
		linesVect[14] = 'v_saida_xor= '+ str(valor1)+'m'
		linesVect[16] = 'v_invert_invert= '+ str(valor2)+'m'
		x = '\n'.join(linesVect)
		#print(x)
		fp.write(x)
		fp.close()
'''

#valorIniciala = 0.3818220
#valorInicialb = 0.3133669
textao = ""
#os.system('hspice xor.cir > text.txt')

#for temp in range(25, 130, 25): #temp loop
for temp in range(25, 126, 25):
	#print("temp= {}" .format(temp))
	temperature_insert(temp)
	for version in range(9): #version loop
		version_insert(version)
		for pulso in range(4): # pulso loop
			#print(pulso)
			currentValue = 0
			os.system('echo -e "v_saida_xor= 136m \nv_invert_invert= 0m" > text.txt')
			#valorIniciala = 0.3818220
			#valorInicialb = 0.3133669
			#altera_text(valorIniciala*1000, valorInicialb*1000)
			pulse_value = pulse_insert(pulso)
			# print(funct_read_fileText('text.txt') == 0)
	
			while(funct_read_fileText('text.txt') == 0):
				# print(currentValue)
				# print(pulso)
				#print(currentValue)
				currentValue+=0.5
				increment_current(pulso, currentValue)
				os.system('hspice xor.cir > text.txt')
				# print("Depois increment_current")
				#print(currentValue)
				
				#valorIniciala -= 0.0012
				#valorInicialb += 0.0005
				#altera_text(valorIniciala*1000, valorInicialb*1000)

			textao += "XOR V" + str(version+1) + ", pulse= " + str(pulse_value) + ", i= " + str(currentValue) + ", temp= " + str(temp) + "\n"
#os.system()				
print(textao)




#=======Loop para chamadas MODIFICAR===========================================================
'''
for i in range (25, 130, 25):
	temperature_insert(i)
'''
'''
for pulso in range(3):
'''
'''
#version_insert(2)
for i in range(9):
	version_insert(i)
'''
#=============================CHAMADAS========================================
'''
while (flag == 0):
	funct_read_fileText("text.txt")


#pulse_insert(3)
#temperatute_insert(50)

print(flag)
'''






















