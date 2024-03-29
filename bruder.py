import requests
import argparse
import sys
from datetime import datetime
from threading import Thread


# colored text and background


def prRed(skk): print("\033[91m {}\033[00m".format(skk))


def prGreen(skk): print("\033[92m {}\033[00m".format(skk))


# This function will store the output

parser = argparse.ArgumentParser(description="This is directory brute forcing tool --->> BRUDER V1.0 ")

parser.add_argument("--url", required=True, help="enter the url in the given format "
                                                 "[ http://www.example.com or"
                                                 " http://ip_address of the server ]")
parser.add_argument("-v", "--valid", action="store_true", help="This will only show valid addresses")
parser.add_argument("-i", "--invalid", action="store_true", help="This will only show invalid addresses")
parser.add_argument("-a", "--all", action="store_true", help="This will show all valid and invalid addresses")
parser.add_argument("--status_code", type=int, help="This will show only particular status_code")
parser.add_argument("--output", type=str, help="This will save the output to a entered file location"
                                               " format for path [/xyz/xyz/eg_word_list.txt]")

parser.add_argument("-e", "--extension", help="this will help to enter multiple extension "
                                              "ex [ .php,.html,etc]")

args = parser.parse_args()

output_path = args.output

d = datetime.now()

print("\n--------------")
print("BRUDER V1.0")
print("By HARDIK")
print("--------------")


def output(path, code, check_url):
    try:
        f_o = open(path, "a")

        text_v = "\n" + "[ ++ ] " + "[" + str(code) + "]" + " --- " + str(check_url) + "\n"
        text_i = "\n" + "[ -- ] " + "[" + str(code) + "]" + " --- " + str(check_url) + "\n"

        if 200 <= code < 400:
            f_o.write(text_v)
        elif code >= 400:
            f_o.write(text_i)
    except IOError:
        print("I/O error file or path not found")
        sys.exit()


def Urlcheck(word, enum_url):
    check_url = str(enum_url) + "/" + str(word)
    c = requests.get(check_url)
    if args.valid:
        if 200 <= c.status_code < 400:
            prGreen("[ ++ ] " + "[" + str(c.status_code) + "]" + " --- " + str(check_url))
            if args.output:
                output(output_path, c.status_code, check_url)
    elif args.invalid:
        if c.status_code >= 400:
            prRed("[ -- ] " + "[" + str(c.status_code) + "]" + " --- " + str(check_url))
            if args.output:
                output(output_path, c.status_code, check_url)
    elif args.all:
        if 200 <= c.status_code < 400:
            prGreen("[ ++ ] " + "[" + str(c.status_code) + "]" + " --- " + str(check_url))
            if args.output:
                output(output_path, c.status_code, check_url)
        else:
            prRed("[ -- ] " + "[" + str(c.status_code) + "]" + " --- " + str(check_url))
            if args.output:
                output(output_path, c.status_code, check_url)
    elif args.status_code:
        code = args.status_code
        if c.status_code == code:
            prGreen("[ ++ ] " + "[" + str(c.status_code) + "]" + " --- " + str(check_url))
    else:
        if 200 <= c.status_code < 400:
            prGreen("[ ++ ] " + "[" + str(c.status_code) + "]" + " --- " + str(check_url))
            if args.output:
                output(output_path, c.status_code, check_url)
        else:
            prRed("[ -- ] " + "[" + str(c.status_code) + "]" + " --- " + str(check_url))
            if args.output:
                output(output_path, c.status_code, check_url)


def main(url_name, w_choice):

    base_url = str(url_name)

    if w_choice == "1":
        try:
            print("\nSyntax for entering the path for wordlist [/xyz/xyz/eg_word_list.txt]")
            path = input("Enter the path for your wordlist to brute force :: ")
            print("\n")
            print("**** STARTING BRUTE FORCING ****")
            print("---------------------------------")
            print("Started at " + str(d))
            print("BASE URL == " + str(base_url))
            print("WORDLIST == " + str(path))
            print("---------------------------------\n")

            file_total_words = open(path, "rt")
            data = file_total_words.read()
            words = data.split()

            print("Total generated Words = ", len(words))
            print("\n")

            with open(path, "r") as file:
                for line in file:
                    for word in line.split():
                        if args.extension:
                            new = args.extension.split(',')
                            for i in new:
                                word = word + i
                                Urlcheck(word, base_url)

                        else:
                            Urlcheck(word, base_url)
        except IOError:
            prRed("IO ERROR -->> Wordlist not found / Entered host is not valid")
            sys.exit()

    elif w_choice == "2":
        try:
            print("\n")
            print("**** STARTING BRUTE FORCING ****")
            print("---------------------------------")
            print("Started at " + str(d))
            print("BASE URL == " + str(base_url))
            print("WORDLIST == default wordlist [common.txt]")
            print("---------------------------------\n")

            file_total_words = open("common.txt", "rt")
            data = file_total_words.read()
            words = data.split()

            print("Total generated Words = ", len(words))
            print("\n")

            with open("common.txt", "r") as file:
                for line in file:
                    for word in line.split():
                        if args.extension:
                            new = args.extension.split(',')
                            for i in new:
                                word = word + i
                                Urlcheck(word, base_url)
                        else:
                            Urlcheck(word, base_url)

        except IOError:
            prRed("IO ERROR -->> Wordlist not found / Entered host is not valid")
            sys.exit()

    print("\n----------------------\n")
    print("Ended at " + str(d))
    print("\n")


if __name__ == '__main__':

    url = args.url.split(',')

    print("\nWhich wordlist do you want to use for brute forcing directories")
    wordlist_choice = input("PRESS 1 for your own wordlist and 2 for default wordlist : ")

    count = 0

    for j in url:
        count = count + 1

    # Start all threads.
    threads = []
    for n in range(count):
        t = Thread(target=main, args=(url[n], wordlist_choice,))
        t.start()
        threads.append(t)

    # Wait all threads to finish.
    for t in threads:
        t.join()
