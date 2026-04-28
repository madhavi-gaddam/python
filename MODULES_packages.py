#importing a module
#✅ Method 1: Import entire module
import math_utils

print(math_utils.add(2, 3))
#✅ Method 2: Import specific functions

from math_utils import add

print(add(5, 6))

#✅ Method 3: Import with alias
import math_utils as mu

print(mu.multiply(3, 4))



###################################################

#Real Built-in Modules
import math

print(math.sqrt(16))   # 4.0















































