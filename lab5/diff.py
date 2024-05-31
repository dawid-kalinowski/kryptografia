def hex_to_bin(hex_string):
    return bin(int(hex_string, 16))[2:].zfill(len(hex_string) * 4)

def count_different_bits(hash1, hash2):
    bin1 = hex_to_bin(hash1)
    bin2 = hex_to_bin(hash2)
    different_bits = sum(b1 != b2 for b1, b2 in zip(bin1, bin2))
    total_bits = len(bin1)
    percentage = (different_bits / total_bits) * 100
    return different_bits, total_bits, percentage

def print_diff_results(hash1, hash2):
    different_bits, total_bits, percentage = count_different_bits(hash1, hash2)
    print(f"Liczba różniących się bitów: {different_bits} z {total_bits}, procentowo: {percentage:.0f}%.")


print_diff_results('4d40e5a1f00a6f48c90f689c04ce5c11', 'eec301eac745aba40735fe65d5234278')
print_diff_results('449682f221412755726e277ee6837fa8f0a66c02', '8b4dd68af201eda0d94c45a5c3840c75f5b6dfde')
print_diff_results('4a42a0c4f1866ed435e066e3194fc8fa5f672b70b96dded3d675a5b0', 'e7e8ee88a9dc8182609e9deae076adf1e91981569855c08e2352014c')
print_diff_results('cb15646af8f8efd8121bce5c66efc031c0743e8d35b870c5a0de53cfffb8b264', '32afb1a584742a2d5c21a719d286a65b214437e43c8a6b296b0cd265c6af8e8a')
print_diff_results('c1ca168af2482bfef14ae64cbb7371601fafc170807fd441aa927bf693a0b8d05941a32c462d9af753760aca396fd876', '65036f50ff1f7bf173de4d84993f12d29fac244a1bcc659fd1b8b3d2d2977dfe7690f0dca33951c3008006fa93ad5a78')
print_diff_results('e624f9de880a37322e0aa725abc34f1efefe9f1a918a5d635e34dc9ec600b548cb4572b760df747ff1b1004e92fdd6e90dfaafa1fe84ece02185ecc119865aa1', 'c488278c1a9bf2dbf4a122ab3ac5ed3b6108930997f90240ed9ffbb47352b7a3fec0516537b47b5882a9628c6e567470f0d688b88a9030f8b194c49bad7baf53')
print_diff_results('4bfb2a873ae9769f1eb912e6da1eecc8a2de404296b00518c05c62f0bd980e7ea97734f93e42e1b146f84904420fe96657bdc428eb4f8d273748e64d474e168b', '9aa79282be6ed256b9c97929c726f11c4e14294b3b76c1570f79b9b729984668b0e7989d5f1c286f41c778d0b021e4617aee694c0321e22648781e1c36854509')
