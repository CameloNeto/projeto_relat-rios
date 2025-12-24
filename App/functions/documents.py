from sqlalchemy import false
from string import punctuation
import re

def transform_document(document: str | int):
    """"""
    if type(document) is int:
        document = str(document)

    document_split = [c for c in document if c not in punctuation]
    if len(document_split) == 11:
        document_split.insert(3, '.')
        document_split.insert(7, '.')
        document_split.insert(11, '-')
    elif len(document_split) == 14:
        document_split.insert(2, '.')
        document_split.insert(6, '.')
        document_split.insert(10, '/')
        document_split.insert(15, '-')
    else:
        raise ValueError("A quantidade de caracteres é inválida")
        
    document = ''
    for c in document_split:
        document += c
    
    return document