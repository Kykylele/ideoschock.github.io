from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key-change-it'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/quiz/<test_name>')
def quiz(test_name):
    return render_template(f'{test_name}.html')


@app.route('/three_buttons')
def three_buttons():
    return render_template('three_buttons.html')


@app.route('/revolution_vs_tradition')
def revolution_vs_tradition_res():
    return render_template('revolution_vs_tradition.html')


@app.route('/libertad_vs_fascismo')
def libertad_vs_fascismo_res():
    return render_template('libertad_vs_fascismo.html')


@app.route('/monarchy_vs_theocracy')
def monarchy_vs_theocracy_res():
    return render_template('monarchy_vs_theocracy.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
