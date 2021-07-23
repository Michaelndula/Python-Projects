from cs50 import get_string
from sys import argv

word = set()

def main():

    if not len(argv) == 2:
        print("Usage: python bleep.py dictionary")
        exit(1)
    else:
        ban = set()

        # open banned words file to read
        with open("banned.txt", "r") as f:
            # copy words to the set
            for line in f:
                ban.add(line.strip())

        # prompt user for message
        msg = get_string("What message would you like to censor?\n")
        # split msg to words
        msg_words = msg.split(" ")

        msg_censor = ""
        # censor banned words
        for word in msg_words:
            if word.lower() in ban:
                msg_censor += ("*" * len(word)) + " "
            else:
                msg_censor += word + " "

        # print censored msg
        print(msg_censor.strip())


if __name__ == "__main__":
    main()
