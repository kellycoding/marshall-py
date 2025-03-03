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

value = stringCleaner(input())
print(f"Value is: {value}")