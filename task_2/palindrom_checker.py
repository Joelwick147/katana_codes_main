from flask import Flask,render_template,request

app =Flask(__name__)
history=[]

def is_palindrome(text):
    clean_sample=''.join(char.lower() for char in text if char.isalnum())
    return clean_sample ==clean_sample[::-1]

@app.route("/", methods=['GET','POST'])

def index(text):
    result =None
    message =""
    if request.method =="POST":
        user_input=request.form["text"]
        result = is_palindrome(user_input)
        message =f'"{text}"is a palindrome' if result else f'"{text}" is not a palindrome.'
        history.insert(0, message)
        history[:]=history[:5]
        return render_template("index.html",result = result, message=message,history=history)    

def handler(environ, start_response):
    return app(environ,start_response)
        
#if __name__=="__main__":
#    app.run(debug=True)