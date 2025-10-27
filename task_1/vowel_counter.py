from flask import Flask, request, render_template_string

app = Flask(__name__)

def count_vowels(sentence):
    # convert sentences into small letters
    sentence = sentence.lower()
    vowels = ["a", "e", "i", "o", "u"]
    # create an empty dictionary
    counts = {vowel: 0 for vowel in vowels}

    for vowel in vowels:
        if vowel in sentence:
            for char in sentence:
                if char == vowel:
                    counts[vowel] += 1
    return counts

@app.route('/', methods=['GET', 'POST'])
def index():
    counts = {}
    if request.method == 'POST':
        sentence = request.form.get('sentence', '')
        counts = count_vowels(sentence)

    html_template = """
    <!DOCTYPE html>
<html>
<head>
    <title>Vowel Counter</title>
    <style>
        body {
            font-family: sans-serif;
            background-color: #f4f4f4;
            color: #333;
            padding: 20px;
        }
        .container {
            max-width: 600px;
            margin: 0 auto;
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1, h2 {
            color: #0056b3; 
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        input[type="text"] {
            width: 100%;
            padding: 8px;
            box-sizing: border-box;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            background-color: #007bff; 
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }
        button:hover {
            background-color: #0056b3;
        }
        ul {
            list-style: none;
            padding: 0;
        }
        li {
            background-color: #e9ecef; 
            margin-bottom: 5px;
            padding: 10px;
            border-radius: 4px;
            border: 1px solid #dee2e6;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Vowel Counter</h1>
        <form method="POST">
            <div class="form-group">
                <label for="sentence">Enter a sentence:</label>
                <input type="text" id="sentence" name="sentence">
            </div>
            <button type="submit">Count Vowels</button>
        </form>

        {% if counts %}
            <h2>Vowel Counts:</h2>
            <ul>
                {% for vowel, count in counts.items() %}
                    <li>{{ vowel }}: {{ count }}</li>
                {% endfor %}
            </ul>
        {% endif %}
    </div>
</body>
</html>
    """
    return render_template_string(html_template, counts=counts)

if __name__ == '__main__':
    app.run(debug=True)