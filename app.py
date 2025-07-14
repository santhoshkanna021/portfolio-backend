from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message
from config import Config  # ✅ Fixed this line

app = Flask(__name__)
app.config.from_object(Config)

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    subject = request.form['subject']
    message = request.form['message']

    msg = Message(subject=f"Contact from Portfolio: {subject}",
                  sender=email,
                  recipients=[app.config['MAIL_USERNAME']])
    msg.body = f"""
    Name: {name}
    Email: {email}
    Phone: {phone}
    Subject: {subject}
    Message: {message}
    """

    try:
        mail.send(msg)
        flash("Message sent successfully!", "success")
    except Exception as e:
        flash(f"Failed to send message: {e}", "danger")

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
