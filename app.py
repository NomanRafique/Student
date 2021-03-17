from flask import Flask, render_template, jsonify,request
app = Flask(__name__)


@app.route('/hello')
def hello_world():
    return 'Hello, World!'


@app.route('/')
def Form():
    return render_template('student.html')


@app.route('/result', methods=['POST', 'GET'])
def Respond():
    if request.method == 'POST':
      result = request.form
    print(result)
    return render_template('result.html',result=result)


if __name__ == '__main__':
    app.run(debug=True)
