import unidecode


def remove_accent(text,down_case:bool = True):
    result = unidecode.unidecode(text)
    if down_case:
        result = str(result).lower()
    return result
