x = 3;
while x > 0:
	passwd = input("please enter the password: ")
	if passwd != 'a123456':
		x = x - 1;
		print('Error! your still have ', x, ' time(s) to try.' )
	else:
		print('Password is correct!')
		break
print('')
print('End')