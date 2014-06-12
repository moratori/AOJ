


def shift(char,n):
    if char == ".":
        return char
    elif char == " ":
        return char
    elif char == "\n":
        return char
    else:
        return chr(((ord(char) + n) % 122) + 96)

def shift_text(text,n):
    return "".join(map(lambda c: shift(c,n),text))



def decrypt(line):
    tmp = ""
    i = 0
    while not (("the" in tmp) or ("this" in tmp) or ("that" in tmp)):
        tmp = shift_text(line,i)
        i += 1
    return tmp

def main():
    while True:
        try:
            line = raw_input()
            print decrypt(line)
        except (EOFError):break


main()

