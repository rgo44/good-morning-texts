from flask import Flask, render_template, request, redirect, url_for, session
from send_sms import start_text, stop_text
import uuid

app = Flask(__name__)
app.secret_key = 'ertgd345tgf2qsxcvg5rfc2tfw234tfw456ygvce567ijh'

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/schedule', methods=['POST'])
def schedule():

    sid = str(uuid.uuid4())
    msg = request.form['msgVal']
    receiver = request.form['receiverNum']
    sender = request.form['twilioNum']
    sched_time = request.form['timeSent']
    reps = request.form['reps']

    session['sid'] = sid
    session['msg'] = msg
    session['receiver'] = receiver
    session['sender'] = sender
    session['sched_time'] = sched_time
    session['reps'] = reps

    print(session.items())

    return render_template("schedule.html", msg=msg, 
                                            recepient=receiver, 
                                            sched_time=sched_time,
                                            reps=reps)


@app.route('/start')
def start():
    print("starting...")
    start_text(session['msg'], session['receiver'], session['sender'], session['sched_time'], session['reps'], session['sid'])
    
    return "starting..."

@app.route('/stop')
def stop():
    print("stopping...")
    stop_text(session['sid'])
    session.pop('sid')
    session.pop('msg')
    session.pop('receiver')
    session.pop('sender')
    session.pop('sched_time')
    session.pop('reps')

    return "stopping..."


if __name__ == "__main__":
    app.run(debug=True)