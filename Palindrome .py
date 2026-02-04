def is_palindrome(s):
    # Clean the input string
    clean_string = ''.join(char.lower() for char in s if char.isalnum())
    return clean_string == clean_string[::-1]

def get_user_input():
    user_input = input("Enter a string to check if it's a palindrome: ")
    return user_input

def palindrome_checker():
    while True:
        user_string = get_user_input()
        if user_string.lower() == 'exit':
            print("Exiting the palindrome checker.")
            break
        
        if is_palindrome(user_string):
            print(f"'{user_string}' is a palindrome.")
        else:
            print(f"'{user_string}' is not a palindrome.")

palindrome_checker()
#output
Enter a string to check if it's a palindrome: 121
'121' is a palindrome.
Enter a string to check if it's a palindrome: 221
'221' is not a palindrome.
