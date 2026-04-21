
# multiply = lambda x,y:x*y
# print(multiply(2,3))


products = [("Monitor", 15000), ("Mouse", 1200), ("Keyboard", 3500)]

prod = sorted(products, key=lambda item: item[1])
print(prod)