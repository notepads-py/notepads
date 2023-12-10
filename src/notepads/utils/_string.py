def lines(string):
    return str(string).split('\n')

def words(string):
    return str(string).split(' ')

def chars(string):
    return list(str(string))

def ints(string):
    int_list = []
    for i in str(string):
        if i.isdigit():
            int_list.append(int(i))
    return int_list

def floats(string):
    float_list = []
    for i in str(string):
        if i.isdigit() or i == '.':
            float_list.append(float(i))
    return float_list

def join(string, separator):
    return str(separator).join(str(string))

def split(string, separator):
    return str(string).split(str(separator))

def replace(string, old, new):
    return str(string).replace(str(old), str(new))

def strip(string, chars=None):
    return str(string).strip(str(chars))

def lstrip(string, chars=None):
    return str(string).lstrip(str(chars))

def rstrip(string, chars=None):
    return str(string).rstrip(str(chars))

def capitalize(string):
    return str(string).capitalize()

def lower(string):
    return str(string).lower()

def upper(string):
    return str(string).upper()

def title(string):
    return str(string).title()

def swapcase(string):
    return str(string).swapcase()

def islower(string):
    return str(string).islower()

def isupper(string):
    return str(string).isupper()

def istitle(string):
    return str(string).istitle()

def isdigit(string):
    return str(string).isdigit()

def isnumeric(string):
    return str(string).isnumeric()

def isdecimal(string):
    return str(string).isdecimal()

def isalpha(string):
    return str(string).isalpha()

def isalnum(string):
    return str(string).isalnum()

def isidentifier(string):
    return str(string).isidentifier()

def isspace(string):
    return str(string).isspace()

def isprintable(string):
    return str(string).isprintable()

def isascii(string):
    return str(string).isascii()
