def split_binary(binary: str, size: int) -> str:
    return binary[:size]

def remove_bits_from_binaries(binaries: str, amount: int):
    return binaries[amount:]