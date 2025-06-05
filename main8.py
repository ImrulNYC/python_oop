class EmailService:


    def _connect(self):
        print("Connecting to email server")


    def _authenticate(self,username,password):
        print("auth")

    def send_email(self):
        self._connect()
        self._authenticate()
        print("sending the email")
        self._disconnect()
    
    def _disconnect(self):
        print("disconnecting from email server")



email1=EmailService()

email1.send_email()

