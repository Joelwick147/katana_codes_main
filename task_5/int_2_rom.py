def integer_to_roman(num=None):

    #Define standard lists of Roman symbols and their corresponding integer values
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    #create an empty string for the result
    roman_num = ""

    #Loop through each value-symbol pair
    i = 0
    while num > 0:
        #Determine how many times the Roman symbol fits into the remaining number
        for _ in range(num // val[i]):
            #Add the corresponding symbol to the result
            roman_num += syms[i]
            #Subtract that value from the number
            num -= val[i]
        # Move to next Roman symbol
        i += 1
    return roman_num

    # If no number is passed, ask the user to input one
    while num is None:
        user_input = input("Enter an integer number between 1 and 3999: ")
        if user_input.isdigit():
            rom_num = int(user_input)
            if 1 <= rom_num  <= 3999:
                num = rom_num
            else:
                print("Please enter a number within the range 1-3999.")
        else:
            print("Invalid input. Please enter a valid integer.")





#sample:
print("Roman numeral:", integer_to_roman())