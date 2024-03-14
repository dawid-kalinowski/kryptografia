import sys
import math
# alphabet = ['a', 'ą', 'b', 'c', 'ć', 'd', 'e', 'ę', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'ł', 'm', 'n', 'ń', 'o', 'ó', 'p', 'r', 's', 'ś', 't', 'u', 'w', 'y', 'z', 'ź', 'ż']
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
crypto = open("crypto.txt", "r").read()
plain = open("plain.txt", "r").read().lower()


def cezarCrypt():
    try:
        tryKey = int(open("key.txt", "r").read().split()[0])
        if tryKey < 0:
            raise ValueError("Klucz nie może być mniejszy od 0.")
    except (IndexError):
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
    print(f"Tekst został pomyślnie zaszyfrowany szyfrem Cezara o kluczu {key} w pliku crypto.txt")


def affineCrypt():
    try:
        tryKey = int(open("key.txt", "r").read().split()[0]) 
        factor = int(open("key.txt", "r").read().split()[1])
        
        if tryKey < 0 or factor < 0:
            raise ValueError("Klucz i współczynnik nie mogą być mniejsza od 0.")
        if math.gcd(factor, len(alphabet)) != 1:
            raise ValueError("Współczynnik nie jest względnie pierwszy z długością alfabetu.")
    except (IndexError):
        raise ValueError("Nieprawidłowy klucz.")
    
    key = tryKey % len(alphabet)

    crypted = ""
    for i in range(len(plain)):
        for j in range(len(alphabet)):
            if plain[i] == " ":
                crypted += " "
                break
            elif plain[i] == alphabet[j]:
                crypted += alphabet[(factor * j + key) % len(alphabet)]
                break
    with open("crypto.txt", "w") as cryptoTxt:
        cryptoTxt.write(crypted)
    print(f"Tekst został pomyślnie zaszyfrowany szyfrem alfinicznym o kluczu {key} oraz współczynniku {factor} w pliku crypto.txt")

def cezarDecrypt():
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
    print(f"Tekst został pomyślnie rozszyfrowany. Tekst jawny został zapisany w pliku decrypt.txt")

def affineDecrypt():
    try:
        tryKey = int(open("key.txt", "r").read().split()[0]) 
        factor = int(open("key.txt", "r").read().split()[1])
        
        if tryKey < 0 or factor < 0:
            raise ValueError("Nieprawidłowy klucz.")
        
        if math.gcd(factor, len(alphabet)) != 1:
            raise ValueError("Współczynnik nie jest względnie pierwszy z długością alfabetu.")
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
                factor_inv = pow(factor, -1, len(alphabet))
                decrypted += alphabet[(factor_inv * (j - key)) % len(alphabet)]
                break
    with open("decrypt.txt", "w") as decryptTxt:
        decryptTxt.write(decrypted)
    print(f"Tekst został pomyślnie rozszyfrowany. Tekst jawny został zapisany w pliku decrypt.txt")




def cezarKryptoanaliza():
    with open("decrypt.txt", "w") as decryptTxt:
        decryptTxt.write("")
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
    print(f"Kryptoanaliza szyfru Cezara zakończona pomyślnie. Rozszyfrowane teksty znajdują się w pliku decrypt.txt")


def affineKryptoanaliza():
    with open("decrypt.txt", "w") as decryptTxt:
        decryptTxt.write("")
        
    for key in range(1, len(alphabet)):
        for factor in range(1, len(alphabet)):
            if math.gcd(factor, len(alphabet)) == 1:
                decrypted = ""
                for i in range(len(crypto)):
                    for j in range(len(alphabet)):
                        if crypto[i] == " ":
                            decrypted += " "
                            break
                        elif crypto[i] == alphabet[j]:
                            factor_inv = pow(factor, -1, len(alphabet))
                            decrypted += alphabet[(factor_inv * (j - key)) % len(alphabet)]
                            break
                with open("decrypt.txt", "a") as decryptTxt:
                    decryptTxt.write(decrypted + "\n")
    print(f"Kryptoanaliza szyfru alfinicznego zakończona pomyślnie. Rozszyfrowane teksty znajdują się w pliku decrypt.txt")

def cezarKryptoanalizaJawna():
    success = False
    extra = open("extra.txt", "r").read()
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
        if extra in decrypted:
            success = True
            print(f"Udało się odnaleźć klucz - {key}! Odszyfrowany tekst został zapisany w pliku decrypt.txt")
            with open("decrypt.txt", "w") as decryptTxt:
                decryptTxt.write(decrypted)
            with open("key-new.txt", "w") as keyTxt:
                keyTxt.write(str(key))
            break
    if success == False:
        raise ValueError("Nie udało się odnaleźć klucza.")
    
def affineKryptoanalizaJawna():
    success = False
    extra = open("extra.txt", "r").read()
    for key in range(1, len(alphabet)):
        if success == False:
            for factor in range(1, len(alphabet)):
                if math.gcd(factor, len(alphabet)) == 1:
                    decrypted = ""
                    for i in range(len(crypto)):
                        for j in range(len(alphabet)):
                            if crypto[i] == " ":
                                decrypted += " "
                                break
                            elif crypto[i] == alphabet[j]:
                                factor_inv = pow(factor, -1, len(alphabet))
                                decrypted += alphabet[(factor_inv * (j - key)) % len(alphabet)]
                                break
                    print(decrypted)
                if extra in decrypted:
                    success = True
                    print(f"Udało się odnaleźć klucz - {key} - oraz współczynnik - {factor}! Odszyfrowany tekst został zapisany w pliku decrypt.txt.\n"
                        "Klucz oraz współczynnik zostały zapisane w pliku key-new.txt")
                    with open("decrypt.txt", "w") as decryptTxt:
                        decryptTxt.write(decrypted)
                    with open("key-new.txt", "w") as keyTxt:
                        keyTxt.write(str(key) + " " + str(factor))
                    break
    if success == False:
        raise ValueError("Nie udało się odnaleźć klucza.")

        


if __name__ == "__main__":
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
  
    if arg1 == "-c":
        if arg2 == "-e":
            cezarCrypt()
        elif arg2 == "-d":
            cezarDecrypt()
        elif arg2 == "-j":
            cezarKryptoanalizaJawna()
        elif arg2 == "-k":
            cezarKryptoanaliza()
        else:
            raise Exception("Nieprawidłowy drugi argument")
        
    elif arg1 == "-a":
        if arg2 == "-e":
            affineCrypt()
        elif arg2 == "-d":
            affineDecrypt()
        elif arg2 == "-j":
            affineKryptoanalizaJawna()
        elif arg2 == "-k":
            affineKryptoanaliza()
        else:
            raise Exception("Nieprawidłowy drugi argument")
    else:
        raise Exception("Nieprawidłowy pierwszy argument")
    


