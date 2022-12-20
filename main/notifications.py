from herald import registry
from herald.base import EmailNotification
from django.conf import settings

class Email(EmailNotification):
    template_name = 'email' 
    subject = 'welcome to quran_mail' 


    def __init__(self, ayah, tafseer, email, num_ayah, name_sura):  
        self.context = {'ayah':ayah, 'tafsser':tafseer, 'email':email,
         'sub':self.subject, 'num_ayah':num_ayah, 'name_sura':name_sura, 'domain':settings.DOMAIN}
        self.to_emails = [email]
    
    @staticmethod
    def get_demo_args():
        return 'test_ayah', 'test_tafseer', 'test@gmail.com', 'num_aya', 'name'

registry.register(Email)
