from flask import Flask, render_template, jsonify, request
from flask_cors import CORS, cross_origin
import processor


app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

app.config['SECRET_KEY'] = 'app_secret_key'


@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', **locals())


@cross_origin(origin='*')
@app.route('/chatbot', methods=["GET", "POST"])
def chatbotResponse():

    if request.method == 'POST':
        the_question = request.form['question']

        response = processor.chatbot_response(the_question)

    return jsonify({"response": response })



if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888', debug=True)
