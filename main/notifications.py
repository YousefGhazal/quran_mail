from herald import registry
from herald.base import EmailNotification

class Email(EmailNotification):
    template_name = 'email' 
    subject = 'welcome to quran_mail' 


    def __init__(self, ayah, tafseer, email):  
        self.context = {'ayah':ayah, 'tafsser':tafseer, 'email':email, 'sub':self.subject}
        self.to_emails = [email]
    
    @staticmethod
    def get_demo_args():
        return 'test_ayah', 'test_tafseer', 'test@gmail.com'

registry.register(Email)
