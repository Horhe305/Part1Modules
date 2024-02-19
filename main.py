"""Python Packages and Modules"""
# import utilities
# import exp.pow_module
# import exp.extra_functions.modulo_fn

# Python from-import
from exp.extra_functions.modulo_fn import modulo_fun
from utilities import mult, div, add, sub
from exp.pow_module import pow_fn

num1 = 5
num2 = 3

# print(utilities.mult(num1, num2))
# print(utilities.add(num1, num2))
# print(utilities.sub(num1, num2))
# print(utilities.div(num1, num2))

print(mult(num1, num2))
print(add(num1, num2))
print(sub(num1, num2))
print(div(num1, num2))  # More simple and shorter with import-from

# pow_result = exp.pow_module.pow_fn(num1)
pow_result = pow_fn(num1)  # Same here
print(pow_result)

# modulo_result = exp.extra_functions.modulo_fn.modulo_fun(num1, num2)
modulo_result = modulo_fun(num1, num2)  # Much more simple with import-from
print(modulo_result)
