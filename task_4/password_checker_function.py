def validate_password(password):
    if len(password) != 9:
        return "Error: Password must be exactly 9 characters long."
   
    letter_count = 0
    alphanumeric_special_count = 0
    special_chars = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"
   
    for char in password:
        if char.isalpha():
            letter_count += 1
        if char.isalnum() or char in special_chars:
            alphanumeric_special_count += 1
   
    if letter_count < 4:
        return "Error: Password must contain at least 4 letters."
    if letter_count < 2:
        return "Error: Password must contain at least 2 letters."
    if alphanumeric_special_count < 3:
        return "Error: Password must contain at least 3 alphanumeric or special characters."
   
    return "Success: Password is valid."

#sampling
password = input("Enter your password: ")
print(validate_password(password))