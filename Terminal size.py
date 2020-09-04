import os
stringparam = input()
columns, lines = os.get_terminal_size()
size = len(stringparam)
columns = (columns//2) + (size//2)
ste = stringparam.rjust(int(columns))
print(ste)