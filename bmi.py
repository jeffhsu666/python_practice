height = input('enter your height(in cm): ')
weight = input('enter your weight(in kg): ')

height = float(height)/100
weight = float(weight)

bmi = weight / (height * height)

if bmi >= 35:
	print('your bmi is ', bmi, '; high risk of obesity')
elif bmi >= 30:
	print('your bmi is ', bmi, '; medium risk of obesity')
elif bmi >= 27:
	print('your bmi is ', bmi, '; a little risk of obesity')
elif bmi >= 24:
	print('your bmi is ', bmi, '; overweight')
elif bmi >= 18.5:
	print('your bmi is ', bmi, '; normal')
else:
	print('your bmi is ', bmi, '; underweight')