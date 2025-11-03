from flask import Flask, request, render_template_string

app = Flask(__name__)

def is_perfect_square(n):
    root = int(n**0.5)
    return root * root == n

def calculate_successors(n):
    successors = {i: [] for i in range(1, n + 1)}
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j and is_perfect_square(i + j):
                successors[i].append(j)
    return successors

def square_sums_row(n):
    if not (2 <= n <= 43):
        return None
    successors = calculate_successors(n)

    def backtrack(path, used):
        if len(path) == n:
            return True
        last = path[-1]
        for nxt in successors[last]:
            if nxt not in used:
                used.add(nxt)
                path.append(nxt)
                if backtrack(path, used):
                    return True
                path.pop()
                used.remove(nxt)
        return False

    for start in range(1, n + 1):
        path = [start]
        used = {start}
        if backtrack(path, used):
            return path
    return None

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    n = None
    if request.method == 'POST':
        n_str = request.form.get('n')
        if n_str and n_str.isdigit():
            n = int(n_str)
            if 2 <= n <= 43:
                result = square_sums_row(n)

    html = """
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <title>Square Sums Row Finder</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body class="bg-light">
        <div class="container mt-5">
            <div class="card shadow">
                <div class="card-body">
                    <h2 class="card-title text-center">Square Sums Row Finder</h2>
                    <form method="POST" class="mt-4">
                        <div class="mb-3">
                            <label for="inputN" class="form-label">Enter a number (2 to 43):</label>
                            <input type="number" name="n" id="inputN" min="2" max="43" class="form-control" required value="{{ n or '' }}">
                        </div>
                        <button type="submit" class="btn btn-primary w-100">Find Sequence</button>
                    </form>

                    {% if n %}
                        {% if result %}
                            <div class="alert alert-success mt-4">
                                Sequence for {{ n }}:<br>
                                {{ result | join(', ') }}
                            </div>
                        {% else %}
                            <div class="alert alert-warning mt-4">
                                No valid sequence found for n = {{ n }}.
                            </div>
                        {% endif %}
                    {% endif %}
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    return render_template_string(html, result=result, n=n)

if __name__ == "__main__":
    app.run(debug=True)