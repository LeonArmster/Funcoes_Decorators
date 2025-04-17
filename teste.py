from log_decorator import log_decorator

@log_decorator
def soma(a,b):
    return a + b


print(soma(3,'u'))