class Palindrome:

    def reverse(self, word):
        self.word = word
        words = word[::-1]
        print(words)

    def is_palindrome(self, check):
        self.check = check
        word = check[::-1]
        check = check.lower()
        word = word.lower()
        if word == check:
            print("True")
        else:
            print("False")


Palindrome().reverse("racecar")
Palindrome().is_palindrome("RacecaR")
