def validate_email(email):
    import re
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

def format_message(subject, body, sender, recipient):
    return f"From: {sender}\nTo: {recipient}\nSubject: {subject}\n\n{body}"