tuple1 = (4, 3, 2, 2, -1, 18)
tuple2 = (2, 4, 8, 8, 3, 2, 9)
product1 = 1
product2 = 1
for i in tuple1:
    product1 *= i
for m in tuple2:
    product2 *= m
print(f"The product in tuple {tuple1} is {product1}")
print(f"The product in tuple {tuple2} is {product2}")