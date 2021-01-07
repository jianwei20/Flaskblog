from flask import Flask,render_template
app = Flask(__name__)

posts = [
    {
        'author': 'WillySu',
        'title': 'First post content',
        'content': 'Hello my blog',
        'date_post': '12/3,2020',

    },
    {
        'author': 'WillySu1',
        'title': 'Second post content',
        'content': 'Hello my blog1',
        'date_post': '12/4,2020',

    }

]

@app.route('/home')
@app.route('/')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='about')


if __name__ == '__main__':
    app.run(debug=True)
