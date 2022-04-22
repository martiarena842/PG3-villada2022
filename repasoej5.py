def palindromo():
    word = str(input("Ingresa una plabra : "))

    if word == word[::-1]:
        return True
    else:
        return False


print(palindromo())
