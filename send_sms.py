# Download the helper library from https://www.twilio.com/docs/python/install
import os, random, schedule, time
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID'] 
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

# send message
def send_message(data):
    message = client.messages \
                .create(
                    body= data[0],
                    from_= data[1],
                    to= data[2]
                )

    print(message.sid)

def start_text(msg, receiver, sender, sched_time, reps, sid): 
    msg_info = [msg, sender, receiver]

    # scheduling...

    # for testing
    #schedule.every(1).minutes.do(send_message, data=msg_info).tag(sid)

    #daily
    if reps=="daily":
        schedule.every().day.at(sched_time).do(send_message, data=msg_info).tag(sid)
        print("daily")
    #weekly
    elif reps=="weekly":
         schedule.every(7).days.at(sched_time).do(send_message, data=msg_info).tag(sid)
         print("weekly")
    #montly
    elif reps=="monthly":
        schedule.every(30).days.at(sched_time).do(send_message, data=msg_info).tag(sid)
        print("monthly")
    #yearly
    else:
        schedule.every(365).days.at(sched_time).do(send_message, data=msg_info).tag(sid)
        print("yearly")

    while True:
        schedule.run_pending()
        time.sleep(1)


def stop_text(sid):
    schedule.clear(sid)