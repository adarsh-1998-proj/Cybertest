from flask import Flask, render_template, request, redirect, url_for, session
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

@app.route('/')
def index():
    session.clear()
    return render_template('index.html')

@app.route('/level1', methods=['GET', 'POST'])
def level1():
    if request.method == 'POST':
        choice = request.form.get('choice')
        if choice == 'B':
            return redirect(url_for('level2'))
        else:
            return render_template('game_over.html', 
                                   message="You fell for a phishing scam. Game Over.")
    return render_template('level1.html')

@app.route('/level2', methods=['GET', 'POST'])
def level2():
    if request.method == 'POST':
        choice = request.form.get('choice')
        if choice == 'B':
            return redirect(url_for('level3'))
        else:
            return render_template('game_over.html', 
                                   message="Weak password! Your account gets hacked. Game Over.")
    return render_template('level2.html')

@app.route('/level3', methods=['GET', 'POST'])
def level3():
    if request.method == 'POST':
        answer = request.form.get('answer', '').strip().lower()
        if answer == "hack!!":
            return render_template('victory.html')
        else:
            return render_template('game_over.html', 
                                   message="Wrong decryption. The FBI traces your IP. Game Over.")
    return render_template('level3.html')

@app.route('/hint')
def hint():
    return render_template('hint.html')

if __name__ == "__main__":
    # Debug disabled for safety
    app.run(host='0.0.0.0', port=5000)
