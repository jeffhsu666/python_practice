password = 'a123456' #correct password
x = 3; #re-try allow time
while x > 0:
	x = x - 1;
	passwd = input("please enter the password: ")
	if passwd != password:
		print('Error!')
		if x > 0:
			print('You still have ', x, ' time(s) to try.' )
		else:
			print('Service lock! Please contact 02-1234-5678 for help.')
	else:
		print('Password is correct!')
		break
