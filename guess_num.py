import random

lower_bnd = input('Number Guessing: enter the lower bound number: ')
upper_bnd = input('Number Guessing: enter the upper bound number: ')

lower_bnd = int(lower_bnd)
upper_bnd = int(upper_bnd)

random_gold = random.randint(lower_bnd,upper_bnd)

guess_cnt = 0

while True:
	guess_cnt += 1
	guess_num = input('Number Guessing: enter your guess number: ')
	guess_num = int(guess_num)
	if guess_num == random_gold:
		print('Congradulation! You got the num.')
		break
	elif guess_num < random_gold:
		print('Try Again. Please guess a larger number.')
	elif guess_num > random_gold:
		print('Try Again. Please guess a smaller number.')
	print('You"ve tried ', guess_cnt, ' time(s)')