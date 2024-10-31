import sys

def reverse_bytes(hex_string):
    return ''.join(reversed([hex_string[i:i+2] for i in range(0, len(hex_string), 2)]))

def hex_to_dec(hex_string):
    hex_string = hex_string.replace(':', '')
    reversed_hex = reverse_bytes(hex_string)
    return int(reversed_hex, 16)

def dec_to_hex(decimal):
    hex_string = '{:08X}'.format(decimal)
    reversed_hex = reverse_bytes(hex_string)
    return ':'.join([reversed_hex[i:i+2] for i in range(0, len(reversed_hex), 2)])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <serial_number>")
        sys.exit(1)

    input_value = sys.argv[1]

    if ':' in input_value:
        result = hex_to_dec(input_value)
        print(f"Decimal: {result}")
    else:
        try:
            decimal = int(input_value)
            result = dec_to_hex(decimal)
            print(f"Hexadecimal: {result}")
        except ValueError:
            print("Invalid decimal number")
            sys.exit(1)
