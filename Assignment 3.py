class Upi:
    def payment(self):
        print("Payment by Upi")

class Creditcard:
    def payment(self):
        print("Payment by Creditcard")

class Debitcard:
    def payment(self):
        print("Payment by Debitcard")

class Cash:
    def payment(self):
        print("Payment by Cash")

class Payment:
    def __init__(self, mode ):
        self.mode = mode

    def start(self):
        self.mode.payment()

p = Payment(Upi())
p.start()

p = Payment(Creditcard())
p.start()

p = Payment(Debitcard())
p.start()

p = Payment(Cash())
p.start()
