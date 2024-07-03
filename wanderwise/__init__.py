from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        field1 = request.form['field1']
        field2 = request.form['field2']
        return f'You entered: {field1} and {field2}'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)