#The iteration protocol is the mechanism Python uses to loop over objects.
#Two key functions:
#iter(obj) → gets an iterator
#next(iterator) → gets next value

nums = [1, 2, 3]

it = iter(nums)   # step 1: get iterator

while True:
    try:
        val = next(it)   # step 2: get next item
        print(val)
    except StopIteration:
        break
#################################################

#CUSTOM ITERATOR
#__iter__()
#__next__()
class Counter:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.limit:
            self.current += 1
            return self.current
        else:
            raise StopIteration












