#This is a script that codes a message using the Vigenere table and decodes a vigenere coded message.
#Play around with it to see how it works.
def key_code():
	matrix = []
	i, k = 0, 0
	cols, rows = 95, 95
	ch, temp = ' ', ' '
	
	#Populate the matrix
	for i in range(rows):
		row = []
		for k in range(cols):
			#Check if the alphabet has reached Z
			#If true the alphabet restarts from A
			if ord(ch) == ord('~') + 1:
				ch = ' '
			row.append(ch)
			ch = chr(ord(ch) + 1)
		matrix.append(row)
		temp = chr(ord(temp) + 1)
		ch = temp
	return matrix

def coder(password, message):
	mess_arr = []
	pass_arr = []
	matrix = key_code()
	k = 0
	coded = ""
	temp = ""
	
	#Append password and message to array for manipulation
	for i in password:
		pass_arr.append(i)
	for i in message:
		mess_arr.append(i)
	#Levels the length of password and message
	while len(pass_arr) < len(mess_arr) or k < len(password):
		if len(pass_arr) == len(mess_arr):
			break
		if k == len(password):
			k = 0
		pass_arr.append(password[k])
		k += 1
	#Find coded value for a message character
	for p, m in zip(pass_arr, mess_arr):
		row = (ord(m)) - 32
		col = ord(p) - 32
		temp = matrix[row][col]
		coded += temp
		temp = ""
	return (coded)

def decoder(message):
	password = input("Enter password: ").rstrip()
	matrix = key_code()
	pass_arr = []
	mess_arr = []
	temp = ""
	decoded = ""
	k = 0
	col = 0
	a = ord('A')
	
	#Append message and password to an array
	for i in password:
		pass_arr.append(i)
	for i in message:
		mess_arr.append(i)
	
	#Level password and message lengths
	while len(pass_arr) < len(mess_arr) or k < len(password):
		if len(pass_arr) == len(mess_arr):
			break
		if k == len(password):
			k = 0
		pass_arr.append(password[k])
		k += 1
	#Finds corresponding message to the code
	for m, p in zip(mess_arr, pass_arr):
		col = ord(p) - 32
		row = 0
		for ch in range(len(matrix[0])):
			if matrix[ch][col] == m:
				temp = matrix[ch][0]
				decoded += temp
				temp = ""
	return decoded
	
def main():
	i = 0
	option = input("Coder (c) or Decoder (d)\n").rstrip()
	if option == 'c' or option == 'C':
		message = input("Please enter your message: ").rstrip()
		while not message and i < 3:
			message = input("Message cannot empty.Try Again: \n").rstrip()
			if i == 2:
				print("Too many attempts\nExiting...")
				return
			i += 1
		password = input("Provide a password for your message: ").rstrip()
		while len(password) < 8:
			password = input("Password is too short\nPassword should be 8 characters long. Try Again:\n").rstrip()
		coded = coder(password, message)
		print(f"Here is your coded message:\n{coded}")
		input()
	elif option == 'd' or option == 'D':
		message = input("Enter message you need to decode: ").rstrip()
		decoded = decoder(message)
		print(f"Here is your decoded message:\n{decoded}")
		input()
	else:
		print("Option not available :( Try Again")
		input()
		main()
	res = input("Run Again?: ").rstrip()
	if res == 'Y' or res == 'y':
		main()
	if res == 'N' or res == 'n':
		print("Exiting...")
		return
	else:
		print("Invalid option")
		print(res)
	
main()
