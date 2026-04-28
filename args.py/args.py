#*args allows a function to accept any number of positional arguments
# It stores them as a tuple


def show_numbers(*args):
    print(args)

show_numbers(1, 2, 3)


def total_price(*prices):
    return sum(prices)

print(total_price(100, 200, 300))  # 600











