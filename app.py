from flask import Flask, request, make_response, redirect, render_template
from markupsafe import escape

app = Flask(__name__)

#todos = ['APRENDER PYTHON', 'APRENDER DJANGO', 'APRENDER FLASK']

@app.route('/')
def index():
    return "Hello, world"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

#@app.route('/')
#def index():
#    user_ip = escape(request.remote_addr)
#    response = make_response(redirect('/hello'))
#    response.set_cookie('user_ip',user_ip)
#
#    return response
#
#
#
#@app.route('/hello')
#def hello():
#    user_ip = request.cookies.get('user_ip')
#    context = {
#        'user_ip': user_ip,
#        'todos': todos
#    }
#    
#    return render_template('hello.html', **context)  #'Hello Daniel, welcome to Flask Project, your IP is {}.'.format(user_ip)