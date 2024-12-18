def is_prime(func):
    def wrapper(*args, **kwargs):
        number = func(*args, **kwargs)
        for i in range(2, number):
            if i % number != 0:
                print('Простое')
            else:
                print('Составное')
            return number
    return wrapper


@is_prime           # декоратор
def sum_three(*args):
    summ = 0
    for i in args:
        summ += i
    return summ


result = sum_three(2, 3, 6)
print(result)