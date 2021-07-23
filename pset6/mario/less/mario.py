from cs50 import get_int

def main():

    while True:
# get input from the user
        height = get_int("Height: ")
        width = height
# if the user inputs an integer which is greater than eight and less than 1 the code should break and prompt the user for new input
        if height >= 1 and height <= 8:
            break

    for i in range(height):
        for j in range(height - i - 1):
            print(" ", end="")
        for k in range(i+1):
            print("#", end="")
        print("")

if __name__ == "__main__":
    main()