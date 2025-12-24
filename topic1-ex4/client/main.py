
import sys
from PyQt5 import QtWidgets, uic
from transaction import Transaction
from signer import sign_transaction
from sender import send_transaction
from verifier import verify_transaction
from rsa_utils import generate_keys



class Account:
    def __init__(self, name, balance=1000):
        self.name = name
        self.balance = balance
        self.private_key, self.public_key = generate_keys()


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("secureTransaction.ui", self)

        self.hung = Account("Hung", balance=1000)
        self.transaction = None

        
        self.btnCreate.clicked.connect(self.create_transaction)
        self.btnSignTx.clicked.connect(self.sign_transaction)
        self.btnSendTx.clicked.connect(self.send_transaction)
        self.btnVerifyTx.clicked.connect(self.verify_transaction)

        
        self.log(f"Account {self.hung.name} balance: {self.hung.balance}")

    def log(self, message):
        self.textEdit.append(message)

    
    def create_transaction(self):
        receiver = self.txtReceiver.text()
        amount = self.txtAmount.text()

        if not receiver or not amount:
            self.log(" Receiver and Amount must be provided")
            return

        self.transaction = Transaction(sender_account=self.hung, receiver_name=receiver, amount=amount)
        self.log(f"[1] Create transaction: {self.transaction.info()}")
        
        self.log(f"Sender public key: {self.hung.public_key}\n")
        self.log(f"Transaction state: Signed={bool(self.transaction.signature)}, Sent={self.transaction.sent}, Confirmed={self.transaction.confirmed}\n")

    
    def sign_transaction(self):
        if not self.transaction:
            self.log(" Transaction not created yet")
            return

        sign_transaction(self.transaction, self.hung.private_key)
        self.log(f"[2] Transaction signed by {self.hung.name}: {self.transaction.info()}")
        
        sig_hex = self.transaction.signature.hex()
        self.log(f"Transaction signature (first 64 chars): {sig_hex[:64]}...\n")
        self.log(f"Transaction state: Signed={bool(self.transaction.signature)}, Sent={self.transaction.sent}, Confirmed={self.transaction.confirmed}\n")

    
    def send_transaction(self):
        if not self.transaction:
            self.log(" Transaction not created yet")
            return

        
        self.log(f"[3] Sender balance before transaction: {self.hung.balance}")

        if send_transaction(self.transaction):
            self.log(f" Transaction sent and confirmed: {self.transaction.info()}")
            self.log(f" Sender balance after transaction: {self.hung.balance}\n")
            self.log(f"Transaction state: Signed={bool(self.transaction.signature)}, Sent={self.transaction.sent}, Confirmed={self.transaction.confirmed}\n")
        else:
            self.log(" Transaction must be signed before sending OR not enough balance")

    
    def verify_transaction(self):
        if not self.transaction:
            self.log(" Transaction not created yet")
            return

        if verify_transaction(self.transaction, self.hung.public_key):
            self.log(" Verify signature: VALID")
        else:
            self.log(" Verify signature: INVALID")
        self.log(f"Transaction state at verify: Signed={bool(self.transaction.signature)}, Sent={self.transaction.sent}, Confirmed={self.transaction.confirmed}\n")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
