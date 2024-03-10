def mult_by_2(num):
    return num * 2
times_two = mult_by_2
print("4 x 2 = ", times_two(4))

def do_math(func, num):
    return func(num)
print("8 x 2 = ", do_math(mult_by_2, 8))


def my_function2(num):

    def mult_by(x):
        return num * x
    
    return mult_by
get_ans = my_function2(5)
print("5 x 10: {} ".format(get_ans(10)))

list_of_func =  [times_two, get_ans]
print("5 * 9 =", list_of_func[1](9))