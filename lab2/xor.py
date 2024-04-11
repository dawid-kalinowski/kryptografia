import os

def prepare():
    with open("orig.txt", "r", encoding="ASCII") as orig, open("plain.txt", "w", encoding="UTF-8") as plain:
        all_text = ""
        for line in orig:
            line = line.strip()
            line = "".join(char for char in line if char.isalpha() or char.isspace())
            line = line.lower()
            all_text += line[:35] + "\n"
        plain.write(all_text)

def cryptanalysis():
    with open("crypto.txt", "r", encoding="US-ASCII") as crypto, open("decrypt.txt", "w", encoding="US-ASCII") as decrypt:
        lines = crypto.readlines()
        line_length = len(lines[0].strip())
        arr = []
        for line in lines:
            arr.append(bytearray(line.strip(), encoding="US-ASCII"))
        bytes = bytearray(line_length)
        key_bytes = bytearray(line_length)
        for x in range(len(lines)):
            for y in range(line_length):
                if arr[x][y] < 58:
                    bytes[y] = 32
                    key_bytes[y] = arr[x][y] - bytes[y]
        out = ""
        for x in range(len(lines)):
            line = bytearray(line_length)
            for y in range(line_length):
                arr[x][y] -= key_bytes[y]
                if 33 < arr[x][y] < 97:
                    arr[x][y] += 25
                line[y] = arr[x][y]
            out += line.decode("US-ASCII") + "\n"
        decrypt.write(out)


def asciikey():
    try:
        with open("key.txt", "r", encoding="ASCII") as key_file:
            key = key_file.readline().strip()
            bytes = bytearray(key, encoding="US-ASCII")
            for i in range(len(key)):
                bytes[i] -= 97
            return bytes
    except FileNotFoundError:
        print("No key file found")
    except IOError:
        print("I/O problem")
    return None

def encrypt():
    key = asciikey()
    with open("plain.txt", "r", encoding="US-ASCII") as plain, open("crypto.txt", "w", encoding="US-ASCII") as crypto:
        all_text = plain.read().strip()
        bytes = bytearray(all_text, encoding="US-ASCII")
        z = 0
        out = bytearray()
        for byte in bytes:
            if z >= len(key) - 1:
                z = 0
            result = byte + key[z]
            z += 1
            if result > 122:
                result -= 25
            if byte == 10:
                result = 10
                z = 0
            out.append(result)
        crypto.write(out.decode("US-ASCII"))

def main(args):
    if args[0] == "-p":
        prepare()
    elif args[0] == "-e":
        encrypt()
    elif args[0] == "-k":
        cryptanalysis()

if __name__ == "__main__":
    import sys
    main(sys.argv[1:])
