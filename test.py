from functools import reduce

prices = []

# initial  value is given when we have empty list,dict , set  .... etc
total_purchase = reduce(lambda total, price: total + price, prices, 0)

print(total_purchase)
