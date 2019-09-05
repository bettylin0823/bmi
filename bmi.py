height = input('請輸入您的身高(單位m)：')
weight = input('請輸入您的體重：')
bmi = float(weight)/(float(height)*float(height))
print(bmi)
if float(bmi) < 18.5:
	print('體重過輕')
if 24 > float(bmi) >= 18.5:
	print('正常範圍')
else:
	print('體重過重')