rain = input('is it raining outside? Ans: ')
dinner_time = input('In evening now? Ans: ')

if rain == 'yes':
    print('stay home')
    print('read a book')
    print('have a cup of coffee')
    if dinner_time == 'yes':
        print('prepare for your dinner')
    else:
    	print('order a pizza')