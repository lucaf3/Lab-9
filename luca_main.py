def encode_password(password):
    encoded_password =" "
    for digit in password:
        new_digit = str((int(digit)+3)%10)
        encoded_password += new_digit
    return encoded_password

def decode_password(password):
    decoded_password =" "
    for digit in password:
        new_digit = str((int(digit)-3)%10)
        decoded_password += new_digit
    return decoded_password
