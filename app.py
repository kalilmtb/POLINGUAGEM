from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/noticias')
def noticias():
    return render_template('noticias.html')

@app.route('/variedades')
def variedades():
    return render_template('variedades.html')

@app.route('/exclusivas')
def exclusivas():
    return render_template('exclusivas.html')

if __name__ == '__main__':
    app.run(debug=True)
