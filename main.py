def alphabet_position(text):
    result = ""
    for i in text:
        asc = ord(i)
        if asc >= 65 and asc <= 90:
            result += str(asc - 64)
            result += " "
        elif asc >= 97 and asc <=122:
            result += str(asc - 96)
            result += " "   
    return result[:-1]

def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())