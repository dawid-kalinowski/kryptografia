import sys
def cezarCrypt():
    plain = open("plain.txt", "r").read().lower()
    # alphabet = ['a', 'ą', 'b', 'c', 'ć', 'd', 'e', 'ę', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'ł', 'm', 'n', 'ń', 'o', 'ó', 'p', 'r', 's', 'ś', 't', 'u', 'w', 'y', 'z', 'ź', 'ż']
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    try:
        tryKey = int(open("key.txt", "r").read().split()[0]) 
        if tryKey < 0:
            raise ValueError("Nieprawidłowy klucz.")
    except (ValueError, IndexError):
        raise ValueError("Nieprawidłowy klucz.")
    key = tryKey % len(alphabet)

    crypted = ""
    for i in range(len(plain)):
        for j in range(len(alphabet)):
            if plain[i] == " ":
                crypted += " "
                break
            elif plain[i] == alphabet[j]:
                if j + key > len(alphabet) - 1:
                    crypted += alphabet[j - len(alphabet) + key]
                else:
                    crypted += alphabet[j + key]
                break
    with open("crypto.txt", "w") as cryptoTxt:
        cryptoTxt.write(crypted)

def cezarDecrypt():
    crypto = open("crypto.txt", "r").read()
    # alphabet = ['a', 'ą', 'b', 'c', 'ć', 'd', 'e', 'ę', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'ł', 'm', 'n', 'ń', 'o', 'ó', 'p', 'r', 's', 'ś', 't', 'u', 'w', 'y', 'z', 'ź', 'ż']
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    try:
        tryKey = int(open("key.txt", "r").read().split()[0]) 
        if tryKey < 0:
            raise ValueError("Nieprawidłowy klucz.")
    except (ValueError, IndexError):
        raise ValueError("Nieprawidłowy klucz.")
    key = tryKey % len(alphabet)
    
    decrypted = ""
    for i in range(len(crypto)):
        for j in range(len(alphabet)):
            if crypto[i] == " ":
                decrypted += " "
                break
            elif crypto[i] == alphabet[j]:
                if j - key < 0:
                    decrypted += alphabet[len(alphabet) - key + j]
                else:
                    decrypted += alphabet[j - key]
                break
    with open("decrypt.txt", "w") as decryptTxt:
        decryptTxt.write(decrypted)


def cezarKryptoanaliza():
    with open("decrypt.txt", "w") as decryptTxt:
        decryptTxt.write("")
    crypto = open("crypto.txt", "r").read()
    # alphabet = ['a', 'ą', 'b', 'c', 'ć', 'd', 'e', 'ę', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'ł', 'm', 'n', 'ń', 'o', 'ó', 'p', 'r', 's', 'ś', 't', 'u', 'w', 'y', 'z', 'ź', 'ż']
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for key in range(1, len(alphabet)):    
        decrypted = ""
        for i in range(len(crypto)):
            for j in range(len(alphabet)):
                if crypto[i] == " ":
                    decrypted += " "
                    break
                elif crypto[i] == alphabet[j]:
                    if j - key < 0:
                        decrypted += alphabet[len(alphabet) - key + j]
                    else:
                        decrypted += alphabet[j - key]
                    break
        with open("decrypt.txt", "a") as decryptTxt:
            decryptTxt.write(decrypted + "\n")



if __name__ == "__main__":
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
  
    if arg1 == "-c":
        if arg2 == "-e":
            cezarCrypt()
        elif arg2 == "-d":
            cezarDecrypt()
        elif arg2 == "-j":
            print("na razie nie ma -j")
        elif arg2 == "-k":
            cezarKryptoanaliza()
        else:
            raise Exception("Nieprawidłowy drugi argument")
        
    elif arg1 == "-a":
        if arg2 == "-e":
            print()
        elif arg2 == "-d":
            print()
        elif arg2 == "-j":
            print()
        elif arg2 == "-k":
            print()
        else:
            raise Exception("Nieprawidłowy drugi argument")
    else:
        raise Exception("Nieprawidłowy pierwszy argument")
    


