from flask import Flask, render_template
from flask import make_response, request, abort

# import all the app logic
from analysis import get_logo

# Initialize Flask web application
app = Flask(__name__)


@app.route('/')
def index():
    """ This is our home page """
    name = request.args.get('name')
    return render_template('index.html', name=name)


@app.route('/logo/<name>.png')
def logo(name):
    """
    Gene name parameter is passed along as part of the image name requested
    Generate logo as an image
    """
    if len(name) == 0:
        abort(404)

    logo_data = None
    try:
        logo_data = get_logo(name)
    except:
        abort(500)

    if logo_data is None:
        abort(404)

    response = make_response(logo_data)
    response.headers['Content-Type'] = 'image/png'
    # response.headers['Content-Disposition'] = 'attachment; filename=logo.png'
    return response


if __name__ == '__main__':
    """ 
      Application entry point
      This web application has a built-in web server 
    """
    app.run(debug=True)
