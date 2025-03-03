def stringCleaner(text):
    '''
    arguments
        text: string argument that is to be cleaned

    returns
        string object with only alphabetical lowercased characters
    '''

    result = ""
    for character in text:
        if character.isalpha():
            result += character.lower()
    return result

def palindromeChecker(text):
    '''
    arguments
        text: string argument that is to be checked if it is a palindrome

    returns
        True or False indicating whether or not the argument is a palindrome, not non-alphabetical characters or lower/uppercase
    '''

    text = stringCleaner(text)

    for i in range(len(text)//2):
        if text[i] != text[-1*i-1]:
            return False
            
    return True

print(palindromeChecker(input()))