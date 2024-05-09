import argparse

def prepare_text(input_file, output_file, line_length):
    with open(input_file, 'r') as f:
        text = f.read()
        prepared_text = ''.join(format(ord(c), '08b') for c in text)
        prepared_lines = [prepared_text[i:i+line_length] for i in range(0, len(prepared_text), line_length)]

        with open(output_file, 'w') as output:
            for line in prepared_lines:
                output.write(line + '\n')
    print("Text prepared successfully.")

def encrypt(input_file, key_file, output_file):
    with open(input_file, 'r') as f:
        plain_text = f.read()
    with open(key_file, 'r') as f:
        key = f.read()

    encrypted_text = ''.join(chr(ord(plain_text[i]) ^ ord(key[i % len(key)])) for i in range(len(plain_text)))
    with open(output_file, 'w') as output:
        output.write(encrypted_text)
    print("Text encrypted successfully.")

def cryptoanalysis(crypto_file, output_file):
    with open(crypto_file, 'r') as f:
        crypto_text = f.readlines()

    space_positions = []
    for i in range(len(crypto_text[0])):
        count_ones = sum(1 for line in crypto_text if line[i] == '1')
        if count_ones > len(crypto_text) / 2:
            space_positions.append(i)

    decrypted_text = []
    for line in crypto_text:
        decrypted_line = ''
        for i in range(len(line)):
            if i in space_positions:
                decrypted_line += ' '
            else:
                decrypted_line += '_'
        decrypted_text.append(decrypted_line)

    with open(output_file, 'w') as output:
        for line in decrypted_text:
            output.write(line + '\n')
    print("Cryptoanalysis completed successfully.")

def main():
    parser = argparse.ArgumentParser(description="XOR encryption and cryptoanalysis tool")
    parser.add_argument("-p", "--prepare", metavar="line_length", type=int, default=64, help="Prepare text for encryption")
    parser.add_argument("-e", "--encrypt", action="store_true", help="Encrypt text")
    parser.add_argument("-k", "--cryptoanalysis", action="store_true", help="Perform cryptoanalysis")

    args = parser.parse_args()

    if args.prepare:
        prepare_text("orig.txt", "plain.txt", args.prepare)
    elif args.encrypt:
        encrypt("plain.txt", "key.txt", "crypto.txt")
    elif args.cryptoanalysis:
        cryptoanalysis("crypto.txt", "decrypt.txt")

if __name__ == "__main__":
    main()
