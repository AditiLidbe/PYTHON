def is_isogram(string):
    char_list = []
    for char in string.lower(): 
        if char.isalpha(): 
            if char in char_list:
                return False
            else:
                char_list.append(char)
    return True
