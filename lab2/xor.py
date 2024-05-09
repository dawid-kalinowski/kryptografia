import sys
from typing import List


def prepare():
    with open("orig.txt", 'r') as orig:
        text = orig.read().replace('\n', ' ').strip().lower()
        text = ''.join(char for char in text if char.isalpha() or char == ' ')
        with open("plain.txt", 'w') as plain:
            for i in range(0, len(text), 64):
                line = text[i:i+64]
                if len(line) < 64:
                    line += 'a' * (64 - len(line))
                plain.write(line + '\n')
    print("Przygotowano tekst.")


def encrypt(block_size: int = 64) -> None:
    with open("plain.txt", "r") as file_plain:
        plaintext = [line.rstrip("\n") for line in file_plain.readlines()]
        
    with open("key.txt", "r") as file_key:
        key = file_key.read()
        
    with open("crypto.txt", "w") as file_crypto:
        for line in plaintext:
            for i in range(block_size):
                file_crypto.write(chr(ord(line[i]) ^ ord(key[i])))
    print("Zaszyfrowano tekst.")



def crypto(lines: List[str]) -> List[str]:
    columns = [[line[i] for line in lines] for i in range(len(lines[0]))]
    decrypted_columns = []

    for col in columns:
        line = ["" for _ in range(len(col))]
        differences = [ord(col[i]) ^ ord(col[i+1]) for i in range(len(col)-1)]

        i = 0
        while i <= len(differences):
            try:
                if differences[i] >> 5 == 0 and differences[i+1] >> 5 == 2 and differences[i+2] >> 5 == 2:
                    line[i] = chr(differences[i] ^ differences[i+1] ^ 0b00100000)
                    line[i+1] = chr(0b00100000 ^ differences[i+1])
                    line[i+2] = chr(0b00100000 ^ differences[i+2])
                    i += 3
                elif differences[i] >> 5 == 2 and differences[i+1] >> 5 == 2 and differences[i+2] >> 5 == 0 and i < len(line) - 2:
                    line[i] = chr(0b00100000 ^ differences[i])
                    line[i+1] = chr(0b00100000)
                    line[i+2] = chr(0b00100000 ^ differences[i+1])
                    i += 3
                elif differences[i] == differences[i+2] and differences[i] >> 5 == 0 and differences[i+1] >> 5 == 2:
                    line[i] = chr(0b00100000)
                    line[i+1] = chr(differences[i+1] ^ 0b00100000)
                    line[i+2] = chr(0b00100000)
                    i += 3
                elif differences[i] >> 5 == 0 and differences[i+1] >> 5 == 2 and differences[i+2] >> 5 == 0:
                    line[i] = chr(differences[i] ^ differences[i+1] ^ 0b00100000)
                    line[i+1] = chr(0b00100000 ^ differences[i+1])
                    line[i+2] = chr(0b00100000)
                    i += 3
                elif differences[i] >> 5 == 2 and differences[i+1] >> 5 == 0 and differences[i+2] >> 5 == 0:
                    line[i] = chr(0b00100000)
                    line[i+1] = chr(differences[i] ^ 0b00100000)
                    line[i+2] = chr(differences[i+1] ^ differences[i] ^ 0b00100000)
                    i += 1
                else:
                    line[i] = "_"
                    i += 1
            except IndexError:
                line[i] = "_"
                i += 1

        decrypted_columns.append("".join(line))

    decrypted_lines = ["".join([col[i] for col in decrypted_columns]) for i in range(len(decrypted_columns[0]))]
    return decrypted_lines


def cryptoanalysis(block_size: int = 64) -> None:
    with open("crypto.txt", "r") as f:
        crypto_text = f.read()
    blocks = [crypto_text[i:i+block_size] for i in range(0, len(crypto_text), block_size)]
    with open("decrypt.txt", "w") as f:
        f.write("\n".join(crypto(blocks)))
    print("Kryptoanaliza wykonana.")


def main():
    action = sys.argv[1]
    if action in ("-p"):
        prepare()
    elif action in ("-e"):
        encrypt()
    elif action in ("-k"):
        cryptoanalysis()
    else:
        print("Nieprawidłowy argument")

if __name__ == "__main__":
    main()