def soma(a=2, b=3):
    if type(a) not in [int, float] or type(b) not in [int, float]:
        raise TypeError(f"O input 'a' e 'b' devem ser string, recebido a: {a}, {type(a)}, b: {b}, {type(b)}")
    return a + b

def sub(a=5, b=2):
    return a - b

def mult(a, b):
    if type(a) not in [int, float] or type(b) not in [int, float]:
        raise TypeError(f"O input 'a' e 'b' devem ser string, recebido a: {a}, {type(a)}, b: {b}, {type(b)}")
    return a * b

def div(a=10, b=2):
    if b != 0: return a / b
    pass