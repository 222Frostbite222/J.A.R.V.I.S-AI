
# Importing required libraries
import pyttsx3
import time
import threading

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Configure voice settings
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)

# Voice interaction function
def voice_interaction(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

# Alerts and Notifications function
def send_alert(alert_text, delay=0):
    def _alert():
        time.sleep(delay)
        alert = f"Alert, sir: {alert_text}"
        print(alert)
        engine.say(alert)
        engine.runAndWait()
    threading.Thread(target=_alert).start()

# Notification Queue
notification_queue = []

def add_to_queue(notification):
    notification_queue.append(notification)
    process_queue()

# Process notification queue
def process_queue():
    while notification_queue:
        next_notification = notification_queue.pop(0)
        send_alert(next_notification)
