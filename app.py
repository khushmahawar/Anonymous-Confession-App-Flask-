from flask import Flask, render_template,request, redirect, url_for, session, Response
import random
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")



@app.route('/',methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form.get('name')
        return redirect(url_for('main', name=username))#url_for takes the function name of your route, not the path
    return render_template('login.html')

@app.route('/main')
def main():
    return render_template('index3.html', name=request.args.get('name'))
    
    
@socketio.on('message')
def handle_message(name, msg):
    emit('message', f"<b>{name}</b>\n{msg}", broadcast=True)

@socketio.on('colour')
def handle_colour(colour):
    global num
    r = random.randint(128, 255)
    g = random.randint(128, 255)
    b = random.randint(128, 255)
    num=f"{r:02X}{g:02X}{b:02X}"
    emit('colour', str(num), broadcast=True)
   

if __name__ == '__main__':
    socketio.run(app, debug=True)
# To run this code, ensure you have Flask and Flask-SocketIO installed:
# pip install Flask Flask-SocketIO