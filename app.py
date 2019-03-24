from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author':'Nenyalote',
        'title':'Blog Post 1',
        'content':'First post content',
        'date_posted':'March 24,2019'
    },
    {
        'author': 'Tanya',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'March 25,2019'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return  render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',title='About')

if __name__ == "__main__":
    app.run(debug=True,host='127.0.0.1', port=5000)