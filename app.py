from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    print("Server accessed the Home route")
    return("Welcome to my 'Home' page")

@app.route("/about")
def about():
    print("Server accessed the About route")
    return("Welcome to my 'About' Page")
    

if __name__ == "__main__":
    app.run(debug=True)
