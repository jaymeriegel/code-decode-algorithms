import golomb
import elias_gamma
import fibonacci
import huffman
from ascii import *

max_chars: int = 500

def code():
    print("\n--- SELECIONE O ALGORITMO ---")
    print("1. Golomb")
    print("2. Elias Gamma")
    print("3. Fibonacci")
    print("4. Huffman")
    print("5. Voltar ao menu anterior")
    option = input("Escolha uma opção: ")

    if option == "1":
        str_for_coding: str = write_for_code()
        golomb.code(str_for_coding)
    elif option == "2":
        str_for_coding: str = write_for_code()
        elias_gamma.code(str_for_coding)
    elif option == "3":
        str_for_coding: str = write_for_code()
        fibonacci.code(str_for_coding)
    elif option == "4":
        str_for_coding: str = write_for_code()
        huffman.code(str_for_coding)
    elif option == "5":
        menu()
    else:
        print("Opção inválida. Tente novamente.")

def decode():
    print("\n--- SELECIONE O ALGORITMO ---")
    print("1. Golomb")
    print("2. Elias Gamma")
    print("3. Fibonacci")
    print("4. Huffman")
    print("5. Voltar ao menu anterior")
    option = input("Escolha uma opção: ")

    if option == "1":
        binaries_for_decode: str = write_for_decode()
        golomb.decode(binaries_for_decode)
    elif option == "2":
        binaries_for_decode: str = write_for_decode()
        elias_gamma.decode(binaries_for_decode)
    elif option == "3":
        binaries_for_decode: str = write_for_decode()
        fibonacci.decode(binaries_for_decode)
    elif option == "4":
        binaries_for_decode: str = write_for_decode()
        frequencies: dict[str, int] = write_frequencies()
        huffman.decode(binaries_for_decode, frequencies)
    elif option == "5":
        menu()
    else:
        print("Opção inválida. Tente novamente.")

def menu():
    print("------> ATENCAO!!! Esta aplicacao utiliza a tabela ASCII padrao de 128 caracteres!!!")
    while True:
        print("\n--- MENU ---")
        print("1. Codificar")
        print("2. Decodificar")
        print("3. Sair")
        option = input("Escolha uma opção: ")

        if option == "1":
            code()
        elif option == "2":
            decode()
        elif option == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

def write_for_code() -> str | None:
    while True:
        print("ATENCAO! Textos de no maximo 500 caracteres!")
        str_for_code: str = input("Escreva seu texto para ser codificado: ")
        if len(str_for_code) > 500:
            print("Texto com mais de 500 chars, reescreva!")
            continue
        not_valid_chars: list[str] = validate_text(str_for_code)
        if not_valid_chars:
            print(not_valid_chars)
            print("Texto com chars fora do acsii padrao de 128 chars, reescreva!")
        else:
            return str_for_code

def write_for_decode() -> str | None:
    while True:
        print("ATENCAO! Binarios de no maximo 1000 bits!")
        binary_for_decode: str = input("Escreva seu binario para ser decodificado: ")
        if len(binary_for_decode) > 1000:
            print("Binario com mais de 1000 bits, reescreva!")
            continue

        if not binary_validation(binary_for_decode):
            print("Existe char diferentes de 0 e 1, reescreva!")
            continue
        else:
            return binary_for_decode

def binary_validation(binaries: str) -> bool:
    for bits in binaries:
        if bits not in ('0', '1'):
            return False
    return True

def write_frequencies() -> dict[str, int]:
    frequencies: dict[str, int] = {}

    print("Escreva a frequência dos caracteres.")
    print("Para sair, digite 'sair' quando for perguntado pelo caracter.\n")

    while True:
        while True:
            character = input("Escreva seu caracter (ou 'sair' para terminar): ").strip()
            if character.lower() == 'sair':
                return frequencies
            if len(character) != 1:
                print("Erro: escreva somente um único caracter!")
            else:
                break

        while True:
            try:
                frequency = int(input(f"Escreva a quantidade de vezes que o caractere '{character}' aparece: "))
                if frequency <= 0:
                    print("Erro: a frequência deve ser um número inteiro positivo (maior que zero).")
                else:
                    break
            except ValueError:
                print("Erro: por favor, digite um número inteiro válido.")

        frequencies[character] = frequency
        print(f"Caracter '{character}' com frequência {frequency} adicionado!\n")

if __name__ == "__main__":
    menu()