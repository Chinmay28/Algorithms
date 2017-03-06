
def diffbits(a, b):
    c = bin (a ^ b)
    print(str(c).count("1"))


diffbits(int(input().strip()), int(input().strip()))
