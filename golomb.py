from table import *
from decode_utils import *

divisor: int = 64
suffix_size: int = 6
stopbit: str = "1"
min_bits: int = 7
max_bits: int = 8

def code(text: str) -> str:
    table = []
    final_binary: str = ""
    for char in text:
        decimal: int = ord(char)
        binary_with_compression: str = code_a_symbol(decimal)
        table.append([char, decimal, binary_with_compression])
        final_binary += binary_with_compression

    show_code(table, "GOLOMB")
    print("Binario completo: ")
    print(final_binary)

    return final_binary

def code_a_symbol(symbol: int) -> str:
    if symbol > divisor:
        quotient: int = symbol // divisor
        binary_code = ("0" * quotient) + stopbit
    else:
        binary_code = stopbit

    remainder: int = symbol % divisor
    binary_code += str(bin(remainder)[2:].zfill(suffix_size))
    return binary_code

def decode(binaries: str) -> str:
    table = []
    final_str: str = ""

    if not binaries or len(binaries) < min_bits:
        print("Binario nulo ou menor que 7 bits (tamanho minimo para tabela ascii com k=64)")
    else:
        total_bits: int = len(binaries)
        while True:
            if (binaries[0] != "1") and (binaries[1] != "1"):
                print("Binario nao respeita a stop bit, impossivel decodificar")
            else:
                if binaries[0] == "0":
                    binary_to_decode: str = split_binary(binaries, max_bits)
                    binaries = remove_bits_from_binaries(binaries, max_bits)
                    total_bits -= max_bits
                else:
                    binary_to_decode: str = split_binary(binaries, min_bits)
                    binaries = remove_bits_from_binaries(binaries, min_bits)
                    total_bits -= min_bits

                decimal_symbol: int = decode_a_symbol(binary_to_decode)
                char_symbol: str = chr(decimal_symbol)

                table.append([binary_to_decode, decimal_symbol, char_symbol])
                final_str = final_str + char_symbol

                if total_bits < min_bits:
                    print("Total de bits menor que o minimo necessario, finalizado a decodificacao!")
                    break

        show_decode(table, "GOLOMB")
        print("Palavra completa: ")
        print(final_str)

        return final_str

def decode_a_symbol(binaries: str) -> int:
    suffix_binaries = binaries[-suffix_size:]
    if binaries[0] == "0":
        return divisor + int(suffix_binaries, 2)
    return int(suffix_binaries, 2)