from flask import Flask
app = Flask(__name__)
@app.route('/nama/<string:nama>')
def getnama(nama):
 return "nama saya adalah {}".format(nama)

if __name__ == '__main__':
 app.run(debug=True)