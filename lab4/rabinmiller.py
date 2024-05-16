import sys
import random

def gcd(a, b):
    if b != 0:
        return gcd(b, a % b)
    return a

def main():
    input_file = open("wejscie.txt", "r")
    output_file = open("wyjscie.txt", "w")
    
    number1 = input_file.readline().strip()
    number2 = input_file.readline().strip()
    number3 = input_file.readline().strip()
    
    if number1:
        number1 = int(number1)
    if number2:
        number2 = int(number2)
    if number3:
        number3 = int(number3)

    if len(sys.argv) > 1:
        if sys.argv[1] == "-f":
            a = random.randint(2, number1 - 1)
            m = number1 - 1
            bj = pow(a, m, number1)
            if bj != 1:
                output_file.write("Prawdopodobnie złożona")
                exit()
            output_file.write("Brak pewności, dla a =" + str(a))
    else:
        if number3:
            number2 = (number2 * number3) - 1
            for _ in range(0, 40):
                a = random.randint(2, number1 - 1)
                if gcd(a, number1) != 1:
                    ret = gcd(a, number1)
                    output_file.write(str(ret))
                    exit()
                m = number2
                k = 0
                while m % 2 != 1:
                    k += 1
                    m //= 2
                bj = pow(a, m, number1)
                if bj == 1 or bj == number1 - 1:
                    continue
                b_before = 0
                first = True
                for _ in range(0, k):
                    bj_before = bj
                    bj = pow(bj, 2, number1)
                    if bj == 1 and first:
                        b_before = bj_before
                        first = False
                        break
                ret = gcd(b_before - 1, number1)
                if ret != 1:
                    output_file.write(str(ret))
                    exit()
            output_file.write("Prawdopodobnie pierwsza")
        elif number2:
            for _ in range(0, 40):
                a = random.randint(2, number1 - 1)
                if gcd(a, number1) != 1:
                    ret = gcd(a, number1)
                    output_file.write(str(ret))
                    exit()
                m = number2
                k = 0
                while m % 2 != 1:
                    k += 1
                    m //= 2
                bj = pow(a, m, number1)
                if bj != 1:
                    output_file.write(f":Liczba r: {number2} nie jest wykladnikiem uniwersalnym: ({a}^{number2}) mod {number1} = {bj}")
                    exit()
                if bj == 1 or bj == number1 - 1:
                    continue
                b_before = 0
                first = True
                for _ in range(0, k):
                    bj_before = bj
                    bj = pow(bj, 2, number1)
                    if bj == 1 and first:
                        b_before = bj_before
                        first = False
                        break
                ret = gcd(b_before - 1, number1)
                if ret != 1:
                    output_file.write(str(ret))
                    exit()
            output_file.write("Prawdopodobnie pierwsza")
        elif number1:
            for _ in range(0, 40):
                a = random.randint(2, number1 - 1)
                if gcd(a, number1) != 1:
                    ret = gcd(a, number1)
                    output_file.write(str(ret))
                    exit()
                m = number1 - 1
                k = 0
                while m % 2 != 1:
                    k += 1
                    m //= 2
                bj = pow(a, m, number1)
                if bj == 1 or bj == number1 - 1:
                    continue
                b_before = 0
                first = True
                for _ in range(0, k):
                    bj_before = bj
                    bj = pow(bj, 2, number1)
                    if bj == 1 and first:
                        b_before = bj_before
                        first = False
                        break
                if bj != 1:
                    output_file.write("Na pewno złożona")
                    exit()
                else:
                    if b_before != number1 - 1:
                        ret = gcd(b_before - 1, number1)
                        output_file.write(str(ret))
                        exit()
            output_file.write("Prawdopodobnie pierwsza")
        else:
            print("Brak pliku wejscie.txt")

    input_file.close()
    output_file.close()

if __name__ == "__main__":
    main()
