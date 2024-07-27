# Program to convert between decimal, octal, binary, and hexadecimal number systems - Vinesh V

# Define a function to convert decimal to binary
def decimal_to_binary(n):
    """
    Convert a decimal number to its binary representation.
    
    Parameters:
    n (int): The decimal number to be converted.
    
    Returns:
    str: The binary representation of the decimal number.
    """
    bins = ""
    while n > 0:
        bins = str(n % 2) + bins
        n = n // 2
    return bins

# Define a function to convert binary to decimal
def binary_to_decimal(n):
    """
    Convert a binary number to its decimal representation.
    
    Parameters:
    n (int): The binary number to be converted.
    
    Returns:
    int: The decimal representation of the binary number.
    """
    dec = 0
    power = 0
    while n > 0:
        dec = dec + (n % 10) * (2 ** power)
        n = n // 10
        power = power + 1
    return dec

# Define a function to convert octal to decimal
def octal_to_decimal(n):
    """
    Convert an octal number to its decimal representation.
    
    Parameters:
    n (int): The octal number to be converted.
    
    Returns:
    int: The decimal representation of the octal number.
    """
    dec = 0
    power = 0
    while n > 0:
        dec = dec + (n % 10) * (8 ** power)
        n = n // 10
        power = power + 1
    return dec

# Define a function to convert decimal to octal
def decimal_to_octal(n):
    """
    Convert a decimal number to its octal representation.
    
    Parameters:
    n (int): The decimal number to be converted.
    
    Returns:
    str: The octal representation of the decimal number.
    """
    octs = ""
    while n > 0:
        octs = str(n % 8) + octs
        n = n // 8
    return octs

# Define a function to convert hexadecimal to decimal
def hexadecimal_to_decimal(n):
    """
    Convert a hexadecimal number to its decimal representation.
    
    Parameters:
    n (str): The hexadecimal number to be converted.
    
    Returns:
    int: The decimal representation of the hexadecimal number.
    """
    dec = 0
    power = 0
    while n != "":
        ch = n[-1]
        if ch.isdigit():
            ch = int(ch)
        else:
            ch = ord(ch.upper()) - ord('A') + 10
        dec = dec + ch * (16 ** power)
        n = n[:-1]
        power = power + 1
    return dec

# Define a function to convert decimal to hexadecimal
def decimal_to_hexadecimal(n):
    """
    Convert a decimal number to its hexadecimal representation.
    
    Parameters:
    n (int): The decimal number to be converted.
    
    Returns:
    str: The hexadecimal representation of the decimal number.
    """
    hex_characters = "0123456789ABCDEF"
    hexs = ""
    while n > 0:
        hexs = hex_characters[n % 16] + hexs
        n = n // 16
    return hexs

while True:
    # Print the menu
    print("The menu is as follows \n 1:change decimal to binary \n 2:change binary to decimal \n 3:oct to bin \n 4:bin to oct \n 5:hex to bin \n 6:bin to hex")

    # Get the user's choice
    choice = int(input("Enter the menu: "))

    # Perform the appropriate conversion based on the choice
    if choice == 1:
        n = int(input("Enter the number: "))
        binary_equiv = decimal_to_binary(n)
        print(f"Binary number: {binary_equiv}")
    elif choice == 2:
        n = int(input("Enter the number: "))
        decimal = binary_to_decimal(n)
        print(f"Decimal number: {decimal}")
    elif choice == 3:
        n = int(input("Enter the number: "))
        dec_oct = octal_to_decimal(n)
        octal_number = decimal_to_binary(dec_oct)
        print(f"Your binary number for corresponding octal is: {octal_number}")
    elif choice == 4:
        n = int(input("Enter the number: "))
        bin_dec = binary_to_decimal(n)
        octal = decimal_to_octal(bin_dec)
        print(f"Octal: {octal}")
    elif choice == 5:
        n = input("Enter the number: ")
        dec_hex = hexadecimal_to_decimal(n)
        hex_number = decimal_to_binary(dec_hex)
        print(f"Binary number: {hex_number}")
    elif choice == 6:
        n = int(input("Enter the number: "))
        dec_bin = binary_to_decimal(n)
        hex_val = decimal_to_hexadecimal(dec_bin)
        print(f"Hexadecimal number: {hex_val}")
    else:
        print("Enter only the number from 1-6")
    print("\n")
