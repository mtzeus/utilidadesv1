import random
import string
import qrcode
import time
import tempfile
import subprocess
import os

def gerar_senha():
    tamanho = int(input("Digite o tamanho da senha: "))
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def verificar_palindromo():
    palavra = input("Digite uma palavra: ")
    if palavra == palavra[::-1]:
        print("É um palíndromo!")
    else:
        print("Não é um palíndromo!")

def calcular_fatorial():
    numero = int(input("Digite um número: "))
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    print("O fatorial de", numero, "é", fatorial)

def contar_vogais_consoantes():
    palavra = input("Digite uma palavra: ")
    vogais = 0
    consoantes = 0
    for letra in palavra:
        if letra.lower() in 'aeiou':
            vogais += 1
        elif letra.isalpha():
            consoantes += 1
    print("Número de vogais:", vogais)
    print("Número de consoantes:", consoantes)

def calcular_media():
    numeros = []
    n = int(input("Digite a quantidade de números: "))
    for i in range(n):
        numero = float(input("Digite o número " + str(i + 1) + ": "))
        numeros.append(numero)
    media = sum(numeros) / n
    print("A média é", media)

def busca_binaria(lista, elemento):
    inicio = 0
    fim = len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == elemento:
            print("Elemento encontrado na posição", meio)
            return
        elif lista[meio] < elemento:
            inicio = meio + 1
        else:
            fim = meio - 1
    print("Elemento não encontrado na lista")

def calculadora():
    operacao = input("Digite a operação (ex: 2 + 2): ")
    resultado = eval(operacao)
    print("O resultado é", resultado)

def conversor_unidades():
    print("----- Conversor de Unidades -----")
    print("1. Comprimento")
    print("2. Massa")
    print("3. Temperatura")
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        valor = float(input("Digite o valor em metros: "))
        print("Em centímetros:", valor * 100)
        print("Em quilômetros:", valor / 1000)
    elif opcao == 2:
        valor = float(input("Digite o valor em quilogramas: "))
        print("Em gramas:", valor * 1000)
        print("Em libras:", valor * 2.20462)
    elif opcao == 3:
        valor = float(input("Digite o valor em Celsius: "))
        print("Em Fahrenheit:", valor * 9/5 + 32)
        print("Em Kelvin:", valor + 273.15)
    else:
        print("Opção inválida. Por favor, tente novamente.")

def gerar_qrcode(voltar_ao_menu=False):
    dados = input("Digite os dados para o QR Code: ")
    imagem = qrcode.make(dados)

    temp_dir = os.path.dirname(os.path.abspath(__file__))
    temp_file_path = os.path.join(temp_dir, "qrcode.png")

    imagem.save(temp_file_path)
    subprocess.call(["start", temp_file_path], shell=True)

    if voltar_ao_menu:
        menu()

    
def main():
    while True:
        print("""
         __  _ ___     __          __         
  __  __/ /_(_) (_)___/ /___ _____/ /__  _____
 / / / / __/ / / / __  / __ `/ __  / _ \/ ___/
/ /_/ / /_/ / / / /_/ / /_/ / /_/ /  __(__  ) 
\__,_/\__/_/_/_/\__,_/\__,_/\__,_/\___/____/  
                                              
""")
        print("----- UTILIDADES v1. by mtz -----")
        print("1. Gerar Senha")
        print("2. Verificar Palíndromo")
        print("3. Calcular Fatorial")
        print("4. Contar Vogais e Consoantes")
        print("5. Calcular Média")
        print("6. Busca Binária")
        print("7. Calculadora")
        print("8. Conversor de Unidades")
        print("9. Gerar QR Code")
        print("0. Sair")
        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            print("A senha gerada é:", gerar_senha())
        elif opcao == "2":
            verificar_palindromo()
        elif opcao == "3":
            calcular_fatorial()
        elif opcao == "4":
            contar_vogais_consoantes()
        elif opcao == "5":
            calcular_media()
        elif opcao == "6":
            lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
            elemento = int(input("Digite o elemento a ser buscado: "))
            busca_binaria(lista, elemento)
        elif opcao == "7":
            calculadora()
        elif opcao == "8":
            conversor_unidades()
        elif opcao == "9":
            gerar_qrcode()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

        time.sleep(2)

if __name__ == "__main__":
    main()
