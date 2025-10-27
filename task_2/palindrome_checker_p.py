from flask import Flask,render_template_string,request

app =Flask(__name__)
history=[]

def is_palindrome(text):
    clean_sample=''.join(char.lower() for char in text if char.isalnum())
    return clean_sample ==clean_sample[::-1]

@app.route("/", methods=['GET','POST'])
def index():
    html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Palindrome Checker</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-dark text-white">
<div class="container mt-5">
    <div class="card bg-secondary shadow-lg">
        <div class="card-body">
            <h2 class="card-title text-center">Palindrome Checker</h2>
            <form method="post" class="mt-4">
                <div class="mb-3">
                    <input type="text" class="form-control" name="text" placeholder="Enter text here" required>
                </div>
                <button type="submit" class="btn btn-light w-100">Check</button>
            </form>
            {% if result is not none %}
                <div class="alert mt-4 {{ 'alert-success' if result else 'alert-danger' }}">
                    <strong>{{ message }}</strong>
                </div>
            {% endif %}
        </div>
        {% if history %}
    <div class="mt-4">
        <h5>Recent Checks:</h5>
        <ul class="list-group">
            {% for item in history %}
                <li class="list-group-item bg-dark text-white">{{ item }}</li>
            {% endfor %}
        </ul>
    </div>
{% endif %}
    </div>
</div>
</body>
</html>
"""
    result =None
    message =""
    if request.method =="POST":
        user_input=request.form["text"]
        result = is_palindrome(user_input)
        message =f'"{user_input}" is a palindrome' if result else f'"{user_input}" is not a palindrome.'
        history.insert(0, message)
        history[:]=history[:5]
        return render_template_string(html_template,result = result, message=message,history=history)

    return render_template_string(html_template, result=None, message="", history=history)


def handler(environ, start_response):
    return app(environ,start_response)

if __name__=="__main__":
   app.run(debug=True)