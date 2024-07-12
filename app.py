from flask import Flask, render_template , send_from_directory

app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html')
  
@app.route('/form.html')
def form(): 
  return render_template('form.html')

# Route to serve publication.json
@app.route('/publication.json')
def get_publication():
    return send_from_directory('.', 'publication.json')


if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')
