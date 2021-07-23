import sys
from cs50 import get_string


def main():
    # here the compiler checks if the user has input atleast two arguments
    if len(sys.argv) != 2:
        print("Usage: ./caesar k")
        sys.exit(1)

    k = int(sys.argv[1])
    #get input from user
    plaintext = get_string("plaintext: ")
 # print the ciphertext after conversion
    print("ciphertext: ")
 #Cheks for an alphabetic character which is either uppercase or lowercase
    for ch in plaintext:
        if not ch.isalpha():
            print(ch, end="")
            continue
 # Here the compiler cheks if the characters are uppercase or lowercase
        ascii_offset = 65 if ch.isupper() else 97

        pi = ord(ch) - ascii_offset
        ci = (pi + k) % 26

        print(chr(ci + ascii_offset), end="")

    print()

    return 0


if __name__ == "__main__":
    main()