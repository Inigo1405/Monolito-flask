from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def base():
    return render_template('index.html')

@app.post('/login')
def login():
    return render_template('login.html', subtitle="Login Page")

@app.post('/form')
def form():
    return render_template('form.html', name="Usuario")

@app.post('/products')
def products():
    return render_template('products.html', name="Usuario")

if __name__ == '__main__':
    app.run(debug=True)