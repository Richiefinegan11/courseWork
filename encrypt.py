import errno
import string
import requests
import os.path
from requests.exceptions import MissingSchema


def read_file(url):
    """Fetch a URL
    Arg:
        url: A string in the URL form.
    Returns:
        The response in text
    """
    resp = requests.get(url)
    return resp.text


def encrypt(url, key):
    output = []
    for char in url:
        output.append(chr(ord(char)+key))
    output.reverse()
    return ''.join(output)


def main():

    while True:
        try:
            entry = input("Please enter a URL: ")
            url = read_file(entry)
            print(url)
            break
        except MissingSchema:
            print(f" '{entry}' is not a valid URL")
    while True:
        try:
            key = input("Please enter any four digit number: ")
            key = int(key)
            if (key > 0) and (key < 9999):
                encrypted = encrypt(url, key)
                print(encrypted)
                break
            else:
                print(f"This number '{key}' is not 4 digits,\nPlease try again")
        except ValueError:
            print(f"Sorry, '{key}' doesn't seem to be a number")
            print("Please try enter a 4 digits, using whole numbers")

    save_path = '/Users/richie/Documents/Folder.cache/'
    name_of_file = input("What do you wish to call the file? ")
    complete_name = os.path.join(save_path, name_of_file+".txt")
    file1 = open(complete_name, "w")
    to_file = encrypted
    file1.write(to_file)
    file1.close()


if __name__ == "__main__":
    main()
