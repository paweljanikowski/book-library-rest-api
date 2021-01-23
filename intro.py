from flask import Flask, request, jsonify

POSTS = [
    {
        'id': 1,
        'title': 'Title 1',
        'text': 'text 1'
    },
    {
        'id': 2,
        'title': 'Title 2',
        'text': 'text 2'
    },
    {
        'id': 3,
        'title': 'Title 1',
        'text': 'text 3'
    }
]

app = Flask(__name__)


@app.route('/posts', methods=['GET', 'POST'])
def get_posts():
    response_data = {
        'success': True,
        'data': []
    }
    if request.method == 'GET':
        response_data['data'] = POSTS
        return jsonify(response_data)
    elif request.method == 'POST':
        data = request.json
        if 'id' not in data or 'title' not in data or 'text' not in data:
            response_data['success'] = False
            response_data['error'] = 'Please provide all required fields!'
            response = jsonify(response_data)
            response.status_code = 400
        else:
            POSTS.append(data)
            response_data['data'] = POSTS
            response = jsonify(response_data)
            response.status_code = 201
        return response


@app.route('/posts/<int:post_id>')
def get_post(post_id):
    response_data = {
        'success': True,
        'data': []
    }

    try:
        item = [post for post in POSTS if post['id'] == post_id][0]
    except IndexError:
        response_data['success'] = False
        response_data['error'] = 'Not found!'
        response = jsonify(response_data)
        response.status_code = 404
    else:
        response_data['data'] = item
        response = jsonify(response_data)

    return response


@app.errorhandler(404)
def not_found(error):
    response_data = {
        'success': False,
        'data': [],
        'error': str(error)
    }
    response = jsonify(response_data)
    response.status_code = 404

    return response


@app.route('/')
def index():
    # REQUEST:
    # print(request.headers)
    # print(request.headers['Test-One'])
    # print(request.method)
    # print(request.path)
    # print(request.url)
    # print(request.json)
    # print(request.json['name'])

    # RESPONSE
    # Import make_response - does not handle list body :(
    # response = make_response({'id': 1, 'title': "Test"}, 200)  # default is 200, we can omit that
    # Import jsonify to handle every kind of body, even list
    # response = jsonify([{'id': 1, 'title': "Test"}], 200)  # default is 200, we can omit that
    # response.headers['Content-Type'] = 'application/json'  # default when using jsonify, we can omit that
    response = jsonify({'error': 'Not found!'})
    response.status_code = 404
    return response


if __name__ == '__main__':
    app.run(debug=True)
