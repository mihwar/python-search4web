from flask import Flask, render_template, request
from vsearch import search4letters

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'

@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    return render_template('results.html',
                           the_title=title,
                           the_results=results,
                           the_phrase=phrase,
                           the_letters=letters,
                           )

@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to seatch4letters on the web!')

app.run(debug=True)