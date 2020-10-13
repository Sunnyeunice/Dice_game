
from crypto_helpers import * 
# imports all the functions from the module crypto_helpers.py

def caesar(string, k, m):
    """
    (str, int, int) -> str
    
    Returns a string obtained by encrypting or decripting the message received
    Encrypts when the mode is 1
    decrypts when the mode is -1
    
    >>> caesar("cats and dogs", 5, -1)
    'xvon viy yjbn'
    >>> caesar("Life of Pi", 5, 1)
    'qnkj tk un'
    >>> caesar("direction", 20, 1)
    'xclywncih'
    >>> caesar("xclywncih", 20, -1)
    'direction'
    >>> caesar("where is", 17, 15)
    Traceback (most recent call last):
    ValueError: mode not supported
    
    """
    
    # checking if the mode if supported i.e 1 or -1
    if m != 1 and m != -1:
        raise ValueError("mode not supported")
    #if the above condition is True, it stops and displays the error
    # if False, it then goes through the next if statements
    
    result = ""
    if m == 1:
        
        for i in string:
            #calls the helper function from the crypto_helpers module
            shift = shift_char(i, k)
            result += shift # goes through all the characters in the string
        #return result

    if m == -1:
        for i in string:
            shift = shift_char(i, -1*k) # k* -1
            result += shift
        #return result
          
    return result
    #if no characters are entered, then an empty string is returned
    # otherwise, returns the corresponding strings(encrypted or decrypted)
    # the function is then terminated


def vigenere(string, key, m):
    """
    (str, str, int) -> str
    
    Returns a string obtained by encrypting or decripting the message received
    Encrypts when the mode is 1
    decrypts when the mode is -1
    
    >>> vigenere('elephants and hippos', 'rats', 1)
    'vlxhyaglj tfu aagphk'
    >>> vigenere('it is suny', 'bottle', 1)
    'jh bd tigr'
    >>> vigenere('jh bd tigr', 'bottle', -1)
    'it is suny'
    >>> vigenere('language', 'bottle', -10)
    Traceback (most recent call last):
    ValueError: Mode not supported
    >>> vigenere('HUggee', 'JUgs', 1)
    'qomyny'
    >>> vigenere('qomyny', 'JUgs', -1)
    'huggee'
    
    """
    
    # first checks if the mode is supported, then if key is not empty
    # it raises an error is it isn't supported and if key is empty
    #otherwise, proceeds to the next statements
    if m != 1 and m != -1:
        raise ValueError("Mode not supported")
    elif len(key) == 0:
        raise ValueError("The key should not be empty")
    
    
    result = ""
    # calls helper functions from the imported module
    
    keyword = pad_keyword(key, len(string))
    # in above, len converts the string into an integer
    # stores in a variable, keyword, which is a string
    my_list = get_keys(keyword)
    #the above returns a list which is passed through the following statements
    if m == 1:
        index = 0 # starts from character at position 0
        #iterates through the loop
        for i in string:
            shift = shift_char(i, my_list[index])
            result += shift
            index += 1 # passes all characters on the lists
            # returns a string with the encryption
        return result
    if m == -1:
        index = 0
        for i in string:
            # the shift starts from the last character moving backwards
            #iterates through all the characters
            shift = shift_char(i, -1 * my_list[index]) #*(-1) #to make negative
            result += shift
            index += 1 # passes all characters on the lists
        return result # returns a string with the decryption 
            
    
    








