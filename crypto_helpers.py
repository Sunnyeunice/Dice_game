


ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def in_engl_alpha(string):
    """
    (str) -> bool
    
    returns True if the non-empty string contains only characters
    from the English aphabet
    otherwise, returns false
    
    >>> in_engl_alpha("determine")
    True
    >>> in_engl_alpha("Ge")
    True
    >>> in_engl_alpha("cats and dogs")
    False
    >>> in_engl_alpha("my_list")
    False
    
    """
    # first checks if the string is empty by comparing the length
    if len(string) == 0: # if string == ""
        return False # ends here if the if statement is True 
    # for non-empty string, all English alphabet characters become lower case
    string = string.lower()
    for char in string:
        #iterates through each character in the string
        if char not in ALPHABET:
            return False # stops the loop
        
    return True # returns True for if all characters are in the alphabet 

    

def shift_char(char, n):
    """
    (str, int) -> str
    
    first verifies if string contains only one character
    returns lower case letter in the position given by the integer
    only if the character is in the English alphabet
    otherwise it returns the character itself
    
    >>> shift_char("r", 3)
    'u'
    >>> shift_char("5", 3)
    '5'
    >>> shift_char("*&", 8)
    Traceback (most recent call last):
    ValueError: the input string should contain a single character
    >>> shift_char("H", 90)
    't'
    
    """
    
    # raises error if it's more than one character
    # otherwise, it checks the next if statement
    if len(char) != 1:
        raise ValueError("the input string should contain a single character")
    
    # calls a helper function
    if in_engl_alpha(char):
        # goes through this if the character is in the Englis alphabet
        # finding the index of character(changed to lower case) in ALPHABET
        index = ALPHABET.find(char.lower())
        #index takes a new value
        index = index + n
        # since ALPHABET[0:26], n may be greater than 26, so we find the remainder
        # index then takes a new value
        index = index % 26
        return ALPHABET[index]
    else:
        # if the character is not in the alphabet
        return char
    

def get_keys(string):
    """
    (str) -> list[int]
    
    Returns list of elements corresponding to the position of each
    character in the string as a letter of the English alphabet
    raises ValueError if string contains non-characters of English alphabet
    returns empty list for empty strings
    
    >>> get_keys("hAndle")
    [7, 0, 13, 3, 11, 4]
    >>> get_keys("pla_tes")
    Traceback (most recent call last):
    ValueError: the input string must contain only characters from the English alphabet
    >>> get_keys("")
    []
    >>> get_keys("KJUUNN")
    [10, 9, 20, 20, 13, 13]
    
    """
    list_keys = [] # for an empty list onto which integers may be added 
    for char in string:
        # checks every chaarcter in teh string
        # calls a helper function, makes lower case if True
        if in_engl_alpha(char):
            char = char.lower() 
            #finding the index index of the character in ALPHABET 
            index = ALPHABET.find(char)
            #appends the indices to the empty list
            list_keys.append(index)
        else:
            # if the string contains a non-English alphabet character
            raise ValueError("the input string must contain only \
characters from the English alphabet")
    return list_keys
        

def pad_keyword(keyword, n):
    """
    (str, int) -> str
    returns string of length n obtained by concatenating characters
    of the input string
    runs through the loop until the desired length is matched
    raises ValueError is string is empty
    
    >>> pad_keyword("cat", 30)
    'catcatcatcatcatcatcatcatcatcat'
    >> pad_keyword("bjhgtyf@fg", 10)
    'bjhgtyf@fg'
    >>> pad_keyword("CaptainAmerica", 5)
    'Capta'
    >>> pad_keyword("", 1)
    Traceback (most recent call last):
    ValueError: empty string not allowed
    
    """
    # first checks for empty string
    if len(keyword) == 0:
        raise ValueError("empty string not allowed") 
    # this empty string is for concatenation  
    repeated_char = "" 
    for i in range(n):
        # concatenates string input till desired length, then stops 
        char = keyword[i % len(keyword)]
        # repeated_char takes a new value with each iteration
        repeated_char = repeated_char + char
    return repeated_char
    
    
    
    