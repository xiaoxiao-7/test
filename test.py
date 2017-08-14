from flask import Flask, jsonify,request
from TfIdf import train_model


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello world'


# @app.route('/', methods=['POST','GET'])
# def login():
#     if request.method == 'POST':
#         print(request.headers)
#         print(request.form)
#         print(request.form['name'])
#         print(request.form.get('name'))
#         print(request.form.getlist('name'))
#         print(request.form.get('nickname', default='little apple'))
#         return 'fine'


@app.route('/', methods=['POST', 'GET'])
def get_score():
    s = str(request.form['query_string'])
    res = train_model(s)
    print(res)
    return jsonify(res)

if __name__ == '__main__':
    app.run(debug=True)


# tasks = [
#     {
#         'id': 1,
#         'title': u'Buy groceries',
#         'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
#         'done': False
#     },
#     {
#         'id': 2,
#         'title': u'Learn Python',
#         'description': u'Need to find a good Python tutorial on the web',
#         'done': False
#     }
# ]
#
# @app.route('/', methods=['GET'])
# def get_tasks():
#     return jsonify({'tasks':tasks})