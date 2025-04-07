from table import *
from decode_utils import *

stopbit: str = "1"
min_bits: int = 2
fibonacci_sequence: list[int] = [1,2,3,5,8,13,21,34,55,89,144]

def code(text: str) -> str:
    table = []
    final_binary: str = ""
    for char in text:
        decimal: int = ord(char)
        binary_with_compression: str = code_a_symbol(decimal)
        table.append([char, decimal, binary_with_compression])
        final_binary += binary_with_compression

    show_code(table, "FIBONACCI")
    print("Binario completo: ")
    print(final_binary)

    return final_binary

def code_a_symbol(symbol: int) -> str:
    first_index: int = _get_first_index(symbol)
    return _get_binaries_by_first_index(symbol, first_index) + stopbit

def decode(binaries: str) -> str:
    table = []
    final_str: str = ""

    if not binaries or len(binaries) < min_bits or not "11" in binaries:
        print("Binario nulo, menor que 1 bit ou nao contem sequencia de stop bit (11)")
    else:
        total_bits: int = len(binaries)
        while True:
            index_stop_bit: int = binaries.find("11")
            binary_to_decode: str = split_binary(binaries, index_stop_bit + 1)
            binaries = remove_bits_from_binaries(binaries, index_stop_bit + 2)
            total_bits -= index_stop_bit + 1
            decimal_symbol: int = decode_a_symbol(binary_to_decode)
            char_symbol: str = chr(decimal_symbol)
            table.append([binary_to_decode, decimal_symbol, char_symbol])
            final_str = final_str + char_symbol

            if total_bits < min_bits or not "11" in binaries:
                print("Total de bits menor que o minimo necessario ou nao existe mais stopbit (11), finalizado a decodificacao!")
                break

        show_decode(table, "FIBONACCI")
        print("Palavra completa: ")
        print(final_str)

        return final_str

def decode_a_symbol(binaries: str) -> int:
    symbol_sum: int = 0
    print(binaries)
    for index, char in enumerate(binaries):
        if char == "1":
            symbol_sum = symbol_sum + fibonacci_sequence[index]
    return symbol_sum

def _get_first_index(symbol: int) -> int:
    for index, n in enumerate(fibonacci_sequence):
        if symbol < n:
            return index - 1

def _get_binaries_by_first_index(symbol: int, first_index: int) -> str:
    symbol_sum: int = fibonacci_sequence[first_index]
    binaries: str = "1"
    for i in range(first_index - 1, -1, -1):
        if symbol_sum + fibonacci_sequence[i] <= symbol:
            binaries = "1" + binaries
            symbol_sum += fibonacci_sequence[i]
        else:
            binaries = "0" + binaries

    return binaries