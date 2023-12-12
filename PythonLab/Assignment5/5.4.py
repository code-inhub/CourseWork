
import re

def extract_type_name(type_string):
    match = re.search(r"<type '(.*)'>", type_string)
    if match:
        return match.group(1)
    return None  # Return None if no match is found

type_string = "<type 'int'>"
type_name = extract_type_name(type_string)
print(type_name)
