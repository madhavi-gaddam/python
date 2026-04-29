#yield is used inside a function ot turn it into a henerator
#instead of returning all values at once, it prodeces values one at a time.
"""
Difference: return vs yield
return	                       yield
Ends function	           Pauses function
Returns one value	        Returns multiple values (one-by-one)
Memory heavy (stores all)	Memory efficient
"""
def count_up_to(n):
    for i in range(1, n+1):
        yield i

for num in count_up_to(5):
    print(num)


def squares(n):
    for i in range(n):
        yield i * i

for val in squares(1000000):
    if val > 100:
        break
#Only needed values are generated (not all 1M stored)
######################################################################

gen = (x*x for x in range(5))

print(next(gen))  # 0
print(next(gen))  # 1
###########################
gen = (x*x for x in range(5))

for val in gen:
    print(val)


#compare with list
# List comprehension
lst = [x*x for x in range(1000000)]

# Generator expression
gen = (x*x for x in range(1000000))


#lst → uses huge memory
# gen → generates values on demand





