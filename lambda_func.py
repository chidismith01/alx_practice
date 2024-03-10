age_bracket = lambda age: True if age >= 18 else False
print("hey! your age is: ", age_bracket(21))

power_func = [lambda x: x ** 2,
              lambda x: x ** 3,
              lambda x: x ** 4]
for func in power_func:
    print(func(5))