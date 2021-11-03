#!/usr/bin/env python
 # -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect

def search4letters(phrase: str, letters: str = 'aeiou') -> set:
    """Return a set of the 'letters' found in 'phrase'."""
    return set(letters).intersection(set(phrase))

app = Flask(__name__)

@app.route('/')
def hello() -> '302':
    return redirect('/entry')

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

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')