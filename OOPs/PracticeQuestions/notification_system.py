class Notification:
    def send(self,msg):
        pass

class EmailNotification(Notification):
    def send(self, msg):
        print(f"Sending Email: {msg}")

class SmsNotification(Notification):
    def send(self, msg):
        print(f"Sending SMS: {msg}")

class Notifier:
    def __init__(self, n ):
        self.service = n
    
    def notify(self,msg):
        self.service.send(msg)
n= EmailNotification()
n2= SmsNotification()
notifier = Notifier(n)
notifier2 =Notifier(n2)
notifier.notify("Karan")
notifier2.notify("kk")
        