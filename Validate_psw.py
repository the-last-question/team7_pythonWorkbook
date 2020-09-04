import re

def ValidarSenha():
    while True:
        password = input("Insira a senha: ")
        if len(password) < 8:
            print("A senha está ruim, pois necessita de 8 caracteres")
            return false
        elif re.search('[0-9]',password) is None:
            print("A senha está ruim, pois necessita de um número")
            return false
        elif re.search('[A-Z]',password) is None: 
            print("A senha está ruim, pois necessita de uma letra maiúsculas")
            return false
        elif re.search('[a-z]',password) is None: 
            print("A senha está ruim, pois necessita de uma letra minuscula")
            return false
        else:
            print("A senha é boa")
            return true
ValidarSenha()