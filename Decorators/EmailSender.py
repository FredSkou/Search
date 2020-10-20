import smtplib,ssl

# Set sender_email to he Email you want to use and everything should be good to go

def sendEmail(message, receiver_email,subject):
    port = 465

    sender_email = "fredsemailtests@gmail.com"
    password = "adcommodo2020"


    subject ="Subject:"+subject+"\n\n"
    email = subject + message

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com",port,context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, email)


