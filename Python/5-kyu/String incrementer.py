import re

def increment_string(strng):
    match = re.search(r'(\d*)$', strng)
    
    if match:
        number = match.group(1)
        if number:
            new_number = str(int(number) + 1).zfill(len(number))
            return strng[:match.start()] + new_number
        else:
            return strng + '1'
    else:
        return '1'
