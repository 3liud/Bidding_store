import datetime

time = datetime.datetime.now()
sell_date = datetime.datetime(2019, 3, 9, 13, 42)
print(time)
print(sell_date)
min_price = 500
livetime = 30

if time == sell_date:
	livetime = reversed(range(30, 0, -1))
else:
	if sell_date >= time:
		print("sell time for the item is not yet. kindly check later")
	else:
		if sell_date <= time and livetime !=0:
			amount = input("enter your purchase amount:")
			print(amount)
			if int(amount) <= int(min_price):
				while int(amount) <= int(min_price):
					amount = input("kindly update your price. it should be higher than the minimum price:")
					print(amount)
			else:
				if int(amount) >= int(min_price):
					min_price = amount
					print(min_price)
