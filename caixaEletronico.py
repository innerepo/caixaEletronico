'''
notas = [100,50,20,10,5,2,1]
saque = int(input('Digite o valor do Saque: '))
count = 0
resto = saque
for x in range(0,7):
    if saque >= notas[x]:
        inteiro = saque // notas[x]
        resto = saque % notas[x]
        notasSaque = [[x], [inteiro, notas[x]]]
        print(notasSaque)
        if resto == 0:
            notasSaque = [[x],[inteiro,notas[x]]]
            print (notasSaque)
        else:
            while resto != 0:
                count = len(notas)
                for y in range(x,count):
                    if resto >= notas[y]:
                        inteiro = resto // notas[y]
                        notasSaque = [[y], [inteiro, notas[y]]]
                        resto = resto % notas[y]
                        notasSaque = [[y+1], [inteiro, notas[y]]]
            print(notasSaque)


notas = [100,50,20,10,5,2,1]
saque = int(input('Digite o valor do Saque: '))
count = 0
resto = saque
for x in range(0,7):
    if saque >= notas[x]:
        inteiro = saque // notas[x]
        resto = saque % notas[x]

        if resto != 0:
            notasSaque = [[x], [inteiro, notas[x]]]
            print(notasSaque)

        if resto == 0:
            notasSaque = [[x],[inteiro,notas[x]]]
            print (notasSaque)
        else:
            while resto != 0:
                count = len(notas)
                for y in range(x,count):
                    if resto >= notas[y]:
                        inteiro = resto // notas[y]
                        notasSaque = [[y], [inteiro, notas[y]]]
                        resto = resto % notas[y]
                        notasSaque = [[y+1], [inteiro, notas[y]]]
            print(notasSaque)

'''

notas = [100,50,20,10,5,2,1]
saque = int(input('Digite o valor do Saque: '))
count = 0
resto = saque
for x in range(0,7):
    if saque >= notas[x]:
        inteiro = saque // notas[x]
        resto = saque % notas[x]

        if resto != 0:
            notasSaque = [[x], [inteiro, notas[x]]]
            print(notasSaque)

        if resto == 0:
            notasSaque = [[x],[inteiro,notas[x]]]
            print (notasSaque)
        else:
            while resto != 0:
                count = len(notas)
                for y in range(x,count):
                    if resto >= notas[y]:
                        inteiro = resto // notas[y]
                        notasSaque = [[y], [inteiro, notas[y]]]
                        resto = resto % notas[y]
                        notasSaque = [[y+1], [inteiro, notas[y]]]
            print(notasSaque)
