
import sys

for char in raw_input():
    if not char.isalpha():
        sys.stdout.write(char)
    elif char.islower():
        sys.stdout.write(char.upper())
    else:
        sys.stdout.write(char.lower())
print ""
