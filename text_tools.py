def to_upper(str):
    return str.upper()

def to_word_list_isupper(str_list):
    if isinstance(str_list, list) == False:
        raise TypeError("the parameter should be a list")
    for word in str_list:
        if word.islower():
            return False
    return True

def to_upper(str):
    return str.upper()