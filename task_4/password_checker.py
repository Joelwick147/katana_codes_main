from flask import Flask, render_template, request

app = Flask(__name__)

def validate_password(password):
    if len(password) != 9:
        return "Password must be exactly 9 characters long."
    letter_count = 0
    alphanumeric_special_count = 0
    special_chars = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"
    for char in password:
        if char.isalpha():
            letter_count += 1
        if char.isalnum() or char in special_chars:
            alphanumeric_special_count += 1
    if letter_count < 4:
        return "Password must contain at least 4 letters."
    if letter_count < 2:
        return "Password must contain at least 2 letters." # This condition seems redundant and potentially incorrect.
    if alphanumeric_special_count < 3:
        return "Password must contain at least 3 alphanumeric or special characters."
    return "Success: Password is valid!"

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ''
    if request.method == 'POST':
        password = request.form.get('password', '')
        message = validate_password(password)
    return render_template('password_strength_indicator.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)