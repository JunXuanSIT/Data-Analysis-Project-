from flask import Flask, render_template
app = Flask(__name__)

# Defininig routes

# Home Page
@app.route('/')
def main():
    return render_template('main.html')

if __name__=='__main__':
    app.run(debug=True)