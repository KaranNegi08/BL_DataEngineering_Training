import re

class InputSanitizationError(Exception):
    pass

def sanitize_input(text):
    modify_text = re.sub(r'[!@#$%^&\.*]','',text)

    if len(modify_text) == 0:
        raise InputSanitizationError("Text is empty after removing special character")
    
    else:
        print(modify_text)

