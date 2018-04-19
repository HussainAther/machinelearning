from flask import Flask, render_template
from flask import make_response, request, abort
from flask import jsonify

from analysis import precalculate_models, get_results

app = Flask(__name__)


@app.route('/')
def start():
    """
    Default route that shown index.html page
    """
    name = request.args.get('name')
    return render_template('index.html', name=name)


@app.route('/get_json')
def get_json_data():
    """
    Route that returns data in JSON format: [{x, y, label}, {x, y, label}, ...]
    """
    results = get_results()
    return jsonify(results)


if __name__ == '__main__':
    # Program starts here
    precalculate_models()
    app.run(debug=True)
