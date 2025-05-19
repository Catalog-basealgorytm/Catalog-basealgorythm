from flask import Flask, render_template
from models import db, Algorithm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

@app.route('/')
def index():
    algorithms = Algorithm.query.all()
    return render_template('index.html', algorithms=algorithms)

@app.route('/algorithm/<int:id>')
def algorithm(id):
    algo = Algorithm.query.get_or_404(id)
    return render_template('algorithm.html', algo=algo)

if __name__ == '__main__':
    print("Flask стартує...")
    app.run(debug=True)
