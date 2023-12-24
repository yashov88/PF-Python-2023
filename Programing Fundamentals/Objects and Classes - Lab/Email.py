class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.isSent = False

    def send(self):
        self.isSent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.isSent}"


emails = []

data = input()

while data != "Stop":
    sender, receiver, content = data.split()
    email = Email(sender, receiver, content)
    emails.append(email)
    data = input()

idx_of_emails = [int(el) for el in input().split(", ")]

for index, email in enumerate(emails):
    if index in idx_of_emails:
        emails[index].send()
    print(f"{email.sender} says to {email.receiver}: {email.content}. Sent: {email.isSent}")