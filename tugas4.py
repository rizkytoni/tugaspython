from flask import Flask, render_template
app = Flask(__name__)
@app.route('/jurusan')
def getjurusan():
 jurusan = 'T.Pemesinan, TITL, TKRO, T.LAS, RPL, T.Kimia, TOI, Perhotelan '
 return render_template('syndicate1963_1.html', jurusan = jurusan)
if __name__ == '__main__':
 app.run(debug=True)