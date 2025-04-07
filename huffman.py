import main
from decode_utils import *
from table import *
from collections import Counter

def code(text: str) -> str:
    table = []
    final_binary: str = ""
    decimals: list[int] = []
    for char in text:
        decimal: int = ord(char)
        decimals.append(decimal)

    ordered_frequency = _get_ordered_frequency(decimals)
    codes = _code_frequencies(ordered_frequency)

    for char in text:
        decimal: int = ord(char)
        binary_with_compression: str = codes.get(decimal)
        table.append([char, decimal, binary_with_compression])
        final_binary += binary_with_compression

    show_code(table, "HUFFMAN")
    print("Binario completo: ")
    print(final_binary)

    return final_binary

def decode(binaries: str, frequencies: dict[str, int]) -> str:
    table = []
    final_str: str = ""

    if not binaries:
        print("Binario nulo!")
    else:
        decimal_frequencies: dict[int, int] = _convert_keys_to_decimals_in_ascii(frequencies)
        ordered_tuple: list[tuple[int, int]] = _convert_dict_to_ordered_tuple(decimal_frequencies)
        codes = _code_frequencies(ordered_tuple)
        total_bits: int = len(binaries)
        while True:
            decimal_decoded, bits_to_exclude = decode_a_symbol(binaries, codes)
            binary_decoded: str = binaries[-bits_to_exclude:]
            binaries = remove_bits_from_binaries(binaries, bits_to_exclude)
            total_bits -= bits_to_exclude
            char_symbol: str = chr(decimal_decoded)
            table.append([binary_decoded, decimal_decoded, char_symbol])
            final_str = final_str + char_symbol

            if not binaries:
                print("Total de bits menor que o minimo necessario, finalizado a decodificacao!")
                break

        show_decode(table, "HUFFMAN")
        print("Palavra completa: ")
        print(final_str)

        return final_str

def decode_a_symbol(binaries: str, codes_dict: dict[int, str]):
    actual_binary: str = ""
    for binary in binaries:
        actual_binary = actual_binary + binary
        decimal: int = _get_decimal_by_binary(codes_dict, actual_binary)
        if decimal == -1:
            continue
        else:
            return decimal, len(actual_binary)

    print("ERRO, binario nao pode ser decodificado!")
    main.menu()

def _get_ordered_frequency(decimals: list[int]):
    count = Counter(decimals)
    return sorted(count.items(), key=lambda x: (-x[1], x[0]))

def _code_frequencies(tuple_of_frequencies):
    codes = {}
    total = len(tuple_of_frequencies)
    for i, (value, _) in enumerate(tuple_of_frequencies):
        if i == total - 1:
            code = '1' * i
        else:
            code = '1' * i + '0'
        codes[value] = code
    return codes

def _convert_keys_to_decimals_in_ascii(freq_dict: dict[str, int]) -> dict[int, int]:
    return {ord(k): v for k, v in freq_dict.items()}

def _convert_dict_to_ordered_tuple(freq_dict: dict[int, int]) -> list[tuple[int, int]]:
    return sorted(freq_dict.items(), key=lambda x: (-x[1], x[0]))

def _get_decimal_by_binary(codes: dict[int, str], binary_to_search: str) -> int:
    for key, value in codes.items():
        if value == binary_to_search:
            return key
    return -1