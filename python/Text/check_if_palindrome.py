from reverse_a_string import *
rev_str = ReverseAString()

def check_if_palindrome(test_str):
    if(rev_str.reverse_string(test_str).__eq__(test_str)):
        return("It's a palindrome!")
    return("It's not a palindrome.")

def main():
    print(check_if_palindrome(input("Enter string to be checked: ")))

main()