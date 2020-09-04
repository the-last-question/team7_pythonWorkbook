import random

def pasw_generate():
    size = random.readint(7,10)
    for item in range(size):
        char_random = random.readint(33,126)
        psw = psw + chr(char_random)

    print(psw)