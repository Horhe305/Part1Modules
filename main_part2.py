"""Python from-import *"""
from exp.extra_functions.modulo_fn import modulo_fun
from utilities import mult, div, add, sub
from exp.pow_module import pow_fn
# import utilities2
from utilities2 import *

num1 = 6
num2 = 3

print('Utilities2 output')
# print(utilities2.mult2(num1, num2))
print(mult2(num1, num2))
print(add2(num1, num2))
print(sub2(num1, num2))
print(div2(num1, num2))

print('Utilities output')
mult_result = mult(num1, num2)
add_result = add(num1, num2)
sub_result = sub(num1, num2)
div_result = div(num1, num2)
mod_result = modulo_fun(num1, num2)
pow_result = pow_fn(num1)

print(mult_result)
print(add_result)
print(sub_result)
print(div_result)
print(mod_result)
print(pow_result)
