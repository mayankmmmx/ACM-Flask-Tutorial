from flask import Flask, request, jsonify

application = Flask(__name__)

@application.route('/')
@application.route('/index')
def index():
    return "Welcome to the ACM Tutorial's RESTful API!"

@application.route('/add')
def add():
    api_key = request.args.get("api_key")
    if api_key != "acm":
        return jsonify ({
            'output': 'error', 
            'response_code': -1
        })

    first_num = int(request.args.get('first_num'))
    second_num = int(request.args.get('second_num'))
    total = first_num + second_num
    return jsonify ({
        'output': total, 
        'response_code': 0
    })

@application.route('/subtract')
def subtract():
    api_key = request.args.get("api_key")
    if api_key != "acm":
        return jsonify ({
            'output': 'error', 
            'response_code': -1
        })
    first_num = int(request.args.get('first_num'))
    second_num = int(request.args.get('second_num'))
    total = first_num - second_num
    return jsonify ({
        'output': total, 
        'response_code': 0
    })

@application.route('/multiply')
def multiply():
    api_key = request.args.get("api_key")
    if api_key != "acm":
        return jsonify ({
            'output': 'error', 
            'response_code': -1
        })
    first_num = int(request.args.get('first_num'))
    second_num = int(request.args.get('second_num'))
    total = first_num * second_num
    return jsonify ({
        'output': total, 
        'response_code': 0
    })

@application.route('/divide')
def divide():
    api_key = request.args.get("api_key")
    if api_key != "acm":
        return jsonify ({
            'output': 'error', 
            'response_code': -1
        })
    first_num = int(request.args.get('first_num'))
    second_num = int(request.args.get('second_num'))
    total = first_num / second_num
    return jsonify ({
        'output': total, 
        'response_code': 0
    })

if __name__ == "__main__":
    application.run(debug=True)