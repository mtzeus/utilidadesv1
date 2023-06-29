import random
import string
import time

def gerar_senha(comprimento=8, tipos=['ascii_letters', 'digits']):
    caracteres = ''.join(getattr(string, tipo) for tipo in tipos)
    return ''.join(random.choice(caracteres) for _ in range(comprimento))

def verificar_palindromo(palavra=''):
    if not palavra:
        palavra = input("Digite uma palavra: ")

    palavra_invertida = palavra[::-1]
    if palavra == palavra_invertida:
        print("A palavra é um palíndromo.")
    else:
        print("A palavra não é um palíndromo.")

def calcular_fatorial(num=0):
    if num == 0:
        num = int(input("Digite um número inteiro positivo: "))

    resultado = 1
    for i in range(1, num + 1):
        resultado *= i
    print("O fatorial de", num, "é", resultado)

def contar_vogais_consoantes(texto=''):
    if not texto:
        texto = input("Digite um texto: ")

    vogais = 0
    consoantes = 0
    for char in texto.lower():
        if char.isalpha():
            if char in 'aeiou':
                vogais += 1
            else:
                consoantes += 1
    print("Número de vogais:", vogais)
    print("Número de consoantes:", consoantes)

def calcular_media():
    numeros = [float(num) for num in iter(input, 'sair')]

    if numeros:
        media = sum(numeros) / len(numeros)
        print("A média dos números é:", media)
    else:
        print("Nenhum número foi inserido.")

def busca_binaria(lista, elemento):
    primeiro = 0
    ultimo = len(lista) - 1
    encontrado = False

    while primeiro <= ultimo and not encontrado:
        meio = (primeiro + ultimo) // 2
        if lista[meio] == elemento:
            encontrado = True
        else:
            if elemento < lista[meio]:
                ultimo = meio - 1
            else:
                primeiro = meio + 1

    if encontrado:
        print("Elemento encontrado na posição", meio)
    else:
        print("Elemento não encontrado.")

def menu():
    print("""
 
██╗░░░██╗████████╗██╗██╗░░░░░██╗██████╗░░█████╗░██████╗░███████╗░██████╗
██║░░░██║╚══██╔══╝██║██║░░░░░██║██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝
██║░░░██║░░░██║░░░██║██║░░░░░██║██║░░██║███████║██║░░██║█████╗░░╚█████╗░
██║░░░██║░░░██║░░░██║██║░░░░░██║██║░░██║██╔══██║██║░░██║██╔══╝░░░╚═══██╗
╚██████╔╝░░░██║░░░██║███████╗██║██████╔╝██║░░██║██████╔╝███████╗██████╔╝
░╚═════╝░░░░╚═╝░░░╚═╝╚══════╝╚═╝╚═════╝░╚═╝░░╚═╝╚═════╝░╚══════╝╚═════╝░v1
    """)
    print("===== Utilidades v1 =====")
    print("1. Gerar Senha")
    print("2. Verificar Palíndromo")
    print("3. Calcular Fatorial")
    print("4. Contar Vogais e Consoantes")
    print("5. Calcular Média")
    print("6. Busca Binária")
    print("7. Sair")

def opcao_gerar_senha():
    print("\n--- Gerar Senha ---")
    comprimento = input("Digite o comprimento da senha (padrão: 8): ")

    if not comprimento:
        comprimento = 8
    else:
        comprimento = int(comprimento)

    senha = gerar_senha(comprimento)
    print("Senha gerada:", senha)
    time.sleep(2)

def opcao_verificar_palindromo():
    print("\n--- Verificar Palíndromo ---")
    palavra = input("Digite uma palavra: ")
    verificar_palindromo(palavra)
    time.sleep(2)

def opcao_calcular_fatorial():
    print("\n--- Calcular Fatorial ---")
    num = input("Digite um número inteiro positivo (padrão: 5): ")

    if not num:
        num = 5
    else:
        num = int(num)

    calcular_fatorial(num)
    time.sleep(2)

def opcao_contar_vogais_consoantes():
    print("\n--- Contar Vogais e Consoantes ---")
    texto = input("Digite um texto: ")
    contar_vogais_consoantes(texto)
    time.sleep(2)

def opcao_calcular_media():
    print("\n--- Calcular Média ---")
    calcular_media()
    time.sleep(2)

def opcao_busca_binaria():
    print("\n--- Busca Binária ---")
    lista = sorted([random.randint(1, 100) for _ in range(10)])
    print("Lista:", lista)
    elemento = input("Digite o elemento a ser buscado: ")
    busca_binaria(lista, int(elemento))
    time.sleep(2)

def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            opcao_gerar_senha()
        elif opcao == '2':
            opcao_verificar_palindromo()
        elif opcao == '3':
            opcao_calcular_fatorial()
        elif opcao == '4':
            opcao_contar_vogais_consoantes()
        elif opcao == '5':
            opcao_calcular_media()
        elif opcao == '6':
            opcao_busca_binaria()
        elif opcao == '7':
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")
        
        print("\n--- Voltando ao Menu Principal ---")
        time.sleep(2)

if __name__ == "__main__":
    main()
