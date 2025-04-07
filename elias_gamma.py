import math
from table import *
from decode_utils import *

stopbit: str = "1"
min_bits: int = 1

def code(text: str) -> str:
    table = []
    final_binary: str = ""
    for char in text:
        decimal: int = ord(char)
        binary_with_compression: str = code_a_symbol(decimal)
        table.append([char, decimal, binary_with_compression])
        final_binary += binary_with_compression

    show_code(table, "ELIAS GAMMA")
    print("Binario completo: ")
    print(final_binary)

    return final_binary

def code_a_symbol(symbol: int) -> str:
    n: int = math.floor(math.log2(symbol))
    remainder: int = symbol - int(math.pow(2, n))
    binary_code = ("0" * n) + stopbit
    binary_code += str(bin(remainder)[2:].zfill(n))
    return binary_code

def decode(binaries: str) -> str:
    table = []
    final_str: str = ""

    if not binaries or len(binaries) < min_bits or not "1" in binaries:
        print("Binario nulo, menor que 1 bit ou nao contem stop bit")
    else:
        total_bits: int = len(binaries)
        while True:
            n: int = binaries.index("1")
            size_to_split: int = (n * 2) + 1
            binary_to_decode: str = split_binary(binaries, size_to_split)
            binaries = remove_bits_from_binaries(binaries, size_to_split)
            total_bits -= size_to_split
            decimal_symbol: int = decode_a_symbol(binary_to_decode, n)
            char_symbol: str = chr(decimal_symbol)
            table.append([binary_to_decode, decimal_symbol, char_symbol])
            final_str = final_str + char_symbol

            if total_bits < min_bits or not "1" in binaries:
                    print("Total de bits menor que o minimo necessario ou nao existe mais stopbit, finalizado a decodificacao!")
                    break

        show_decode(table, "ELIAS GAMMA")
        print("Palavra completa: ")
        print(final_str)

        return final_str

def decode_a_symbol(binaries: str, n: int) -> int:
    suffix_binaries = binaries[-n:]
    return int(math.pow(2, n)) + int(suffix_binaries, 2)