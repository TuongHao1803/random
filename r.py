import random # 用別人做好的東西
# randint = random integer
r = random.randint(1, 100) # (.)是‘的’的意思
count = 0
while True:
	count += 1 # count = count + 1
	num = input('請輸入一個數字:')
	num = int(num)
	if num == r:
		print('猜中了哦')
		print('這是你猜的第', count, '次')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
	print('這是你猜的第', count, '次')





