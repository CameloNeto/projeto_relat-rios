from string import punctuation


def clear_punctuation(data: int | str):
    """Remove pontução e simbolos"""
    if type(data) is int:
        data = str(int)
    elif type(data) is str:
        pass
    else:
        raise TypeError("O tipo fornecido não é aceito")
    
    data_split = [c for c in data if c not in punctuation]
    data = ""
    for c in data_split:
        data += c
    
    return data