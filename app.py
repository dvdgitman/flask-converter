from flask import Flask, render_template
from flask import request

app = Flask(__name__)


@app.route('/')
def button():
    return render_template("button.html")



@app.route('/about')
def about():
    return """ <center><b><p style="font-family:Tahoma;color:red;font-size: 15px">This WebApp was made by David Gitman<br/>
               The following Flask app will convert Celsius To Fahrenheit.<br/>
               In Order to run this flask app in a stand alone mode run app.py using 'python -m flask run' command.<br/>
               </center></b></p>"""


@app.route("/convert")
def hostname():
    return render_template("index.html")


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


@app.route('/stop')
def shutdown():
    shutdown_server()
    return "<center><b><p style='font-family:Tahoma;color:red;font-size: 15px'>Server Shutting Down....  </b>"


if __name__ == "__main__":
    app.run(debug=True, port=8080, host='0.0.0.0')