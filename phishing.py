import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email and app password setup (use your Gmail app password here)
sender_email = "ashraf.cse.jnu@gmail.com"  # Replace with your Gmail address
app_password = "eopj eefe dggc asyi"     # Replace with your generated app password

# List of recipient emails and names (Replace with your actual list)
recipients = [
    {"name": "John Doe", "email": "ashraf@cse.jnu.ac.bd"},
    {"name": "Jane Smith", "email": "ashraf.cse.jnu@gmail.com"},
    {"name": "Bob Johnson", "email": "ashraf.uddin@ewubd.edu"}
]

# Email content (the phishing email template)
subject = "Urgent Action Required: Account Verification Needed"

# Function to generate email body with personalized recipient's name
def generate_email_body(name):
    return f"""
Dear {name},

We have detected unusual activity on your Facebook account. To secure your account, we need you to verify your login credentials.

Please click the link below to verify your account:
https://rashelashraf.github.io/fake-phishing-demo/

If you do not verify your account within 24 hours, your account may be temporarily suspended.

Thank you for your prompt action.

Sincerely,
Facebook Security Team
"""

# Function to send the email
def send_phishing_email(to_name, to_email):
    try:
        # Setup MIME
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = to_email
        msg['Subject'] = subject

        # Attach the personalized email body
        body = generate_email_body(to_name)
        msg.attach(MIMEText(body, 'plain'))

        # Create SMTP session for sending email
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Use TLS for security
            server.login(sender_email, app_password)  # Login with the app password
            text = msg.as_string()
            server.sendmail(sender_email, to_email, text)
            print(f"Email sent to {to_name} <{to_email}>")

    except Exception as e:
        print(f"Failed to send email to {to_name} <{to_email}>. Error: {e}")

# Send phishing emails to each recipient
for recipient in recipients:
    send_phishing_email(recipient['name'], recipient['email'])
