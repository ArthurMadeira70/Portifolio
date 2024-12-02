num1=int(input('Digite um numero: '))
num2=int(input('Digite outro numero: '))
#As linhas 1 e 2 ela servem para pedir para o usuario inserir dois valores que ele deseja caucular
operação=int(input('Digite qual operação deseja (1:Soma|2:Subtração|3:Multiplicação|4:Divisão): '))
#Na Linha 4 o programa pergunta qual das 4 operações basicas o usuario deseja fazer
def soma (num1,num2):
    res1=num1+num2
    return res1
#Nas Linhas 6, 7 e 8 o programa realiza a função que neste caso realiza a soma com os numeros fornecidos pelo usuario 
def subtração (num1,num2):
    res2=num1-num2
    return res2
#Das linhas 10 a 12 é a função de subtração que como seu nome ja diz ela raliza a operação de subtrair os numeros que o usuarios forneceu
def multiplicação (num1,num2):
    res3=num1*num2
    return res3
#Das linhas 14 a 16 é a função de multiplicação que realiza a operação de multiplicação com os numeros que o usuario forneceu
def divisão(num1,num2):
    res4=num1/num2
    return res4
#Das linhas 18 a 20 é a função de divisão que realiza a operação de divisão com os numeros que o usuario forneceu
if operação == 1:
    print('Sua soma:',soma(num1,num2))
#Nas linhas 22 a 23 o programa ele executa a estruta de decisão da cauculadora, caso o usuario deseja realizar apenas a soma ele digita 1 
elif operação == 2:
    print('Sua Subtração: ',subtração(num1,num2))
#Nas linhas 25 e 26 o programa executa a função de subtração caso o usuario digite 2
elif operação == 3:
    print('Sua Multiplicação: ',multiplicação(num1,num2))
#Nas linhas 28 e 29 o programa executa a função de multiplicação caso o usuario digite 3
elif operação == 4:
    print('Sua Divisão é:',divisão(num1,num2))
#Nas linhas 31 e 32 o programa executa a função de divisão caso o usuario digite 4 
else:
    print(' Digite um numero valido.')
# E por ultimo nas linhas 33 e 34 o programa ele não executa nada caso o usuario não digite um numero entre 1 a 4 e pede para que o usuario digite um valor valido