# 44#import
#Once a module is imported, you can use any of the functions and variables 
# defined in the module by using the dot notation. For example, to use the 
# sqrt function from the math module, you would write:

# import math
# result = math.sqrt(9)
# print(result)  # Output: 3.0

#----------->from keyword
# You can also import specific functions or variables from a module using 
# the from keyword. For example, to import only the sqrt function from the math module, you would write:

# from math import sqrt
# result = sqrt(9)
# print(result)  # Output: 3.0

# You can also import multiple functions or variables 
# at once by separating them with a comma:

# from math import sqrt, pi
# result = sqrt(9)
# print(result)  # Output: 3.0
# print(pi)  # Output: 3.141592653589793

#-------------->importing everything
# It's also possible to import all functions and variables from a module using 
# the * wildcard. However, this is generally not recommended as it can lead to 
# confusion and make it harder to understand where specific functions and variables are coming from.

# from math import *
# result = sqrt(9)
# print(result)  # Output: 3.0
# print(pi)  # Output: 3.141592653589793

# ----------------->The "as" keyword

# Python also allows you to rename imported modules using the as keyword. 
# This can be useful if you want to use a shorter or more descriptive name for 
# a module, or if you want to avoid naming conflicts with other modules or variables in your code.

# import math as m
# result = m.sqrt(9)
# print(result)  # Output: 3.0
# print(m.pi)  # Output: 3.141592653589793

# ------------> from dir function
# Finally, Python has a built-in function called dir that you can use to view the names of all 
# the functions and variables defined in a module. This can be helpful for exploring and understanding 
# the contents of a new module.

# import math
# print(dir(math))
# This will output a list of all the names defined in the math module, including functions 
# like sqrt and pi, as well as other variables and constants.

maths=['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh',
       'atan', 'attan2', 'atanh', 'cbrt', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 
       'e', 'erf', 'erfc', 'exp', 'exp2', 'expm1', 'fabs', 'factorial', 'floor', 'fma', 'fmod', 'frexp',
       'fsum', 'gamma', 'gcd', 'hypot', 'finf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm',
       'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow',
       'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'sumprod', 'tan', 'tanh', 'tau', 'trunc', 'ulp']
# from math import sqrt, pi
# from math import pi, sqrt as s
# import math as math_builtin_python

# result = math_builtin_python.sqrt(9) * math_builtin_python.pi
# print(result)  # Output: 3.0

# from harry import welcome, harry
# import harry as hr
# import math

# print(dir(math))
# print(math.nan, type(math.nan))
# hr.welcome()
# print(hr.harry)