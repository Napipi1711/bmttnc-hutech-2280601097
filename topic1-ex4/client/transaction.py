class Transaction:
    def __init__(self, sender_account, receiver_name, amount):
        self.sender = sender_account
        self.receiver = receiver_name
        self.amount = amount
        self.signature = None
        self.sent = False
        self.confirmed = False

    def info(self):
        sig_status = "Signed" if self.signature else "Not signed"
        sent_status = "Sent" if self.sent else "Not sent"
        conf_status = "Confirmed" if self.confirmed else "Not confirmed"
        return f"{self.sender.name} -> {self.receiver} : {self.amount} | {sig_status} | {sent_status} | {conf_status}"