import smtplib
from email.message import EmailMessage

# Function to send email notification
def send_email(subject, message, sender_email, receiver_email, password):
    msg = EmailMessage()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.set_content(message)

    try:
        # Establish a secure connection with the SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)

        # Send the email
        server.send_message(msg)
        print("Email notification sent successfully!")
    except Exception as e:
        print("Failed to send email notification:", str(e))
    finally:
        server.quit()



# Testing 
#def send_email(subject, message, sender_email, receiver_email, password):
#    print(subject)
#    print(message)