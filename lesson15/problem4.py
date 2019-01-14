print('-'*60)
password= input('what is the password?' )
while password != "open sesame":
	print('password is invalid, try again.')
	password= input('what is the password?' )
if password =='open sesame':
	print('password is valid, welcome!')

print('-'*60)