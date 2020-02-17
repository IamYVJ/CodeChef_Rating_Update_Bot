import smtplib
import email.message

def sendEmail(username, data, email_ID, sender_email_ID, sender_email_ID_password):
    print("D", data)
    message = """Hey {user}! <br> <br>
                Your CodeChef Ratings have been updated. <br> <br>
                Your CodeChef Rating has changed to <b> {rating_new} </b> from {rating_old}. <br> 
                Your Junior Rating has changed to <b> {junior_new} </b> from {junior_old}. <br> <br>
                Thank you. <br> <br>
                Sincerely, <br>
                <b>YVJ Systems</b>""".format( user=username, 
                                            rating_new = data[0],
                                            rating_old = data[2],
                                            junior_new = data[1],
                                            junior_old = data[3] )
    
    msg = email.message.Message()
    msg['Subject'] = 'CodeChef Rating Update - YVJ Systems'
    msg['From'] = sender_email_ID
    msg['To'] = email_ID
    msg.add_header('Content-Type','text/html')
    msg.set_payload(message)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(sender_email_ID,
            sender_email_ID_password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string())
    s.quit()