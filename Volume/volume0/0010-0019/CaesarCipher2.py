
import time


def shift_char(char,index):
    if not (char.isalpha() and char.islower()):
        return char
    code = ord(char) + index
    if code > 122:
        return chr(code % 122 + 96)
    else:
        return chr(code)


def shift_text(text,index):
    return "".join(map(lambda x: shift_char(x,index),text))

def decrypt_text(text):
    tmp = ""
    i = 0
    while not (("the" in tmp) or ("this" in tmp) or ("that" in tmp)):
        tmp = shift_text(text,i)
        i += 1
    return tmp

while True:
    try:
        print decrypt_text(raw_input().strip())
    except (EOFError):break
