def is_default_ascii(char: str) -> bool:
    if 0 <= ord(char) <= 127:
        return True
    return False

def validate_text(text: str) -> list[str]:
    chars_not_in_default_ascii: list[str] = []
    for char in text:
        if not is_default_ascii(char):
            chars_not_in_default_ascii.append(char)
    return chars_not_in_default_ascii