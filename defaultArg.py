# Default arguments

# def price(list_price,discount = 0,tax = 0.05):
#     return f"Your total price comes out to be: ${list_price * (1-discount) * (1+tax)}"
#
# print(price(500,0.1,0))

#Count up Timer

import time as t

def count_down(end,start = 0):
    for n in range(start,end+1):
        print(n)
        t.sleep(1)

count_down(10)
count_down(20,11)


