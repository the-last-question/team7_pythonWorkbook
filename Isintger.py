def isInteger():
    try: 
        s = input("Insira um numero inteiro valido: ")
        s.strip()
        int(s)
        return True
    except ValueError:
        return False

isInteger()