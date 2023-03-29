from funcoes import soma, sub, mult, div

def calcule():
    a = float( input('digite a: ') )
    b = float( input('digite b: ') )
    o = input('digite operacao +,-,/,*: ')
    res = '...'
    if o == '+': 
        res = soma(a, b)
    if o == '-': 
        res = sub(a, b)
    print(res)
    pass