from flask import Flask, request, render_template

app=Flask(__name__)
def count_vowels(sentence):
    #convert sentences into small letters
    sentence=sentence.lower()
    vowels =["a","e","i","o","u"]
    #create an empty dictionary
    counts={vowel:0 for vowel in vowels}

    for vowel in vowels:
        if vowel in sentence:
            for char in sentence:
                if char == vowel:
                    counts[vowel] += 1
    return counts


@app.route('/', methods=['GET','POST'])

def index():
    counts={}
    if request.method =='POST':
        sentence =request.form.get('sentence','')
        counts = count_vowels(sentence)
    return render_template('index.html',counts=counts)

if __name__ =='__main__':
    app.run(debug=True)