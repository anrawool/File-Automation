# File for experimentation
# import smtplib
# from email.message import EmailMessage

# # Set up connection to SMTP server
# s = smtplib.SMTP('smtp.gmail.com', 587)
# s.starttls()

# # Log in to SMTP server
# email_address = 'sarthakrawool09@gmail.com'
# password = ''
# s.login(email_address, password)

# # Create email message
# msg = EmailMessage()
# msg['Subject'] = 'Intro Email'
# msg['From'] = email_address
# msg['To'] = 'mail2shubham23@gmail.com'
# msg.set_content('This is a test email sent using Python. Hello!!')

# # Send email message
# s.send_message(msg)

# # Close connection to SMTP server
# s.quit()


a = int(input("Enter an number: "))
print(a**2)
