hexadecimal_int_dict = {
    '0': 0, '1': 1, '2': 2,
    '3': 3, '4': 4, '5': 5,
    '6': 6, '7': 7, '8': 8,
    '9': 9, 'A': 10, 'B': 11,
    'C': 12, 'D': 13, 'E': 14,
    'F': 15,
    'a': 10, 'b': 11, 'c': 12,
    'd': 13, 'e': 14, 'f': 15
}


def hex_to_decimal(input:str):
    result = 0

    for char in input:
        result = result * 16 + hexadecimal_int_dict[char]
    
    return result

def represents_hex_str(hex_code: str) -> bool:
    if len(hex_code) != 6:
        return False
    
    for char in hex_code:
        if char not in hexadecimal_int_dict:
            return False
    
    return True

def hex_to_rgb(input: str):
    # check if str represents an int, if it does then return it else compute from hexadecimal

    if input[0] == '#':
        input = input[1:]
    
    if not represents_hex_str(input):
        return (0, 0, 0, 0)

    result = (
        hex_to_decimal(input[0:2]),
        hex_to_decimal(input[2:4]),
        hex_to_decimal(input[4:6])
    )

    return result
