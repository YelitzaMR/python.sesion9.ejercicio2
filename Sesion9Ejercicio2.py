from functools import reduce
def sumaImpares():
    def impares (x):
        if x% 2!=0:
            return True
        return False
    resultado= list(filter(impares, numeros))
    print(resultado)
    resultado = reduce((lambda a,b:a+b), resultado)
    print (resultado)
numeros=list(range(100))
sumaImpares()
