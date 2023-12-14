#“Say your program encounters an error.
# If the alert system is the console, we print the error.
# If the alert system is an email, we send it according to the severity of the error.
# If the alert system is anything other than console or email, we don't know what to do, 
# therefore we do nothing. 

# Let's put this into code:


def send_email(*a):
    print (*a)
    
    
alert_system = 'console'
error_severity = 'critical'
error_message = 'OMG Something terrible happened'

if alert_system == 'console':
    print(error_message)
elif alert_system == 'email':
     if error_severity == 'critical':
         send_email('augustine21@gmail.com',error_message)
     elif error_severity =='medium':
         send_email('admin@mycompany.com',error_message)
     else:
          send_email('syre12@outlook.com',error_message)
         