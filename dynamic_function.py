def my_function2(num):

    def mult_by(x):
        return num * x
    
    return mult_by
get_ans = my_function2(5)
print("5 x 10: {} ".format(get_ans(10)))