from flask import Flask, render_template_string, request

app = Flask(__name__)

def validate_password(password):
    # (Keep your existing password validation logic here)
    if len(password) != 9:
        return "Password must be exactly 9 characters long."

    letter_count = 0
    digit_count = 0
    special_count = 0
    special_chars = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"

    for char in password:
        if char.isalpha():
            letter_count += 1
        elif char.isdigit():
            digit_count += 1
        elif char in special_chars:
            special_count += 1

    if letter_count < 4:
        return "Password must contain at least 4 letters."
    if digit_count < 2:
        return "Password must contain at least 2 figures/numbers."
    if special_count != 3:
        return "Password must contain exactly 3 special characters."

    return "Success: Password is valid!"


@app.route('/', methods=['GET', 'POST'])
def index():
    message = ''
    if request.method == 'POST':
        password = request.form.get('password', '')
        message = validate_password(password)

    html_content = """
      <!doctype html>
      <html lang="en">
        <head>
          <meta charset="UTF-8" />
          <meta name="viewport" content="width=device-width, initial-scale=1" />
          <title>Password Strength Indicator</title>
          <link
            href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css"
            rel="stylesheet"
          />
          <style>
            #strengthMessage {
              font-weight: bold;
            }
          </style>
        </head>
        <body class="p-3">
          <div class="container">
            <h3>Password Strength Checker</h3>
            <input
              type="password"
              id="passwordField"
              class="form-control"
              placeholder="Enter password"
            />
            <button id="toggleBtn" class="btn btn-secondary mt-2">Show</button>
            <div id="strengthMessage" class="mt-2">{{ message }}</div>  <!-- Display message here -->
            <div class="progress mt-1" style="height: 10px">
              <div
                id="strengthBar"
                class="progress-bar"
                role="progressbar"
                style="width: 0%"
              ></div>
            </div>
          </div>

          <script>
            const passwordField = document.getElementById("passwordField");
            const strengthBar = document.getElementById("strengthBar");
            const strengthMessage = document.getElementById("strengthMessage");
            const toggleBtn = document.getElementById("toggleBtn");

            passwordField.oninput = () => {
              const pwd = passwordField.value;
              let score = 0;
              let letters = pwd.match(/[a-zA-Z]/g) || [];
              let alnumSpecial =
                pwd.match(/[a-zA-Z0-9!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/g) || [];

              if (pwd.length === 9) score++;
              if (letters.length >= 4) score++;
              if (alnumSpecial.length >= 3) score++;

              const percent = (score / 3) * 100;

              strengthBar.style.width = percent + "%";

              if (score === 0) {
                strengthBar.className = "progress-bar bg-danger";
                strengthMessage.textContent = "Too Weak";
              } else if (score === 1) {
                strengthBar.className = "progress-bar bg-warning";
                strengthMessage.textContent = "Weak";
              } else if (score === 2) {
                strengthBar.className = "progress-bar bg-info";
                strengthMessage.textContent = "Moderate";
              } else if (score === 3) {
                strengthBar.className = "progress-bar bg-success";
                strengthMessage.textContent = "Strong";
              }
            };

            toggleBtn.addEventListener("click", function () {
              if (passwordField.type === "password") {
                passwordField.type = "text";
                toggleBtn.textContent = "Hide";
              } else {
                passwordField.type = "password";
                toggleBtn.textContent = "Show";
              }
            });
          </script>
        </body>
      </html>
    """
    return render_template_string(html_content, message=message)

if __name__ == '__main__':

    app.run(debug=True)