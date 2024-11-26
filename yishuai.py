class iPhone:
    def __init__(self, name, version, phone_number, color, model): # constructor
        self.name = name
        self.ios_version = version
        self.phone_number = phone_number
        self.color = color
        self.model = model
        self.files = []
        self.messages = []
    
    def check_messages(self):
        print(f"Here are the messages you received.'")
    
    def call(self, number):
        pass

    def airdrop(self, filename, recipient):
        print(f"Dropping %s to %s" % (filename, recipient.name))
        recipient.airreceive(message, self.name)

        
    def airreceive(self, message, sender):
        self.messages.append(message)
        print(f"%s has received a message from %s" % (self.name, sender.name))


    def set_name(self, new_name):
        if len(new_name) < 3:
            print("Invalid input. Please enter more than 3 characters.")
        self.name = new_name
class iPhone:
    def __init__(self, name, version, phone_number, color, model): # constructor
        self.name = name
        self.ios_version = version
        self.phone_number = phone_number
        self.color = color
        self.model = model
        self.files = []
        self.messages = []
    
    def check_messages(self):
        print(f"Here are the messages you received.'")
        
    
    def call(self, number):
        pass

    def airdrop(self, filename, recipient):
        print(f"Dropping %s to %s" % (filename, recipient.name))
        recipient.airreceive(filename, self)

        
    def airreceive(self, message, sender):
        self.messages.append(message)
        print(f"%s has received a message from %s" % (self.name, sender.name))


    def set_name(self, new_name):
        if len(new_name) < 3:
            print("Invalid input. Please enter more than 3 characters.")
        self.name = new_name



yishuais_iphone = iPhone(name="yishuai's iPhone",
                     version = "18",
                     phone_number = "123-123-1234",
                     color = "purple",
                     model = "iPhone 14")

print(yishuais_iphone.name)

yuzhes_iphone = iPhone(name="yuzhe's iPhone",
                     version = "15",
                     phone_number = "123-123-5678",
                     color = "black",
                     model = "iPhone 15")

yishuais_iphone.set_name("yishuai's new iPhone")
print(yishuais_iphone.name)


yishuais_iphone.airdrop("Hello", recipient = yuzhes_iphone)

yuzhes_iphone.check_messages()
