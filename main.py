# Python Packages and Modules
import utilities
import exp.pow_module

num1 = 5
num2 = 3

print(utilities.mult(num1, num2))
print(utilities.add(num1, num2))
print(utilities.sub(num1, num2))
print(utilities.div(num1, num2))

pow_result = exp.pow_module.pow_fn(num1)
print(pow_result)
