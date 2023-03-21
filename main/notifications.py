from herald import registry
from herald.base import EmailNotification
from django.conf import settings

class Email(EmailNotification):
    template_name = 'email' 
    subject = 'welcome to quran_mail' 


    def __init__(self, ayah, tafseer, user, num_ayah, name_sura):  
        self.context = {'ayah':ayah, 'tafsser':tafseer, 'user': user,
         'sub':self.subject, 'num_ayah':num_ayah, 'name_sura':name_sura, 'domain':settings.DOMAIN}
        self.to_emails = [user.email]
    
    @staticmethod
    def get_demo_args():
        return 'test_ayah', 'test_tafseer', 'test@gmail.com', 'num_aya', 'name'



class ContentEmail(EmailNotification):
    template_name = 'content_email'
    subject = 'from quran_mail'

    def __init__(self, name, description, email):
        self.context = {'name':name, 'description':description, 'email':email}
        self.to_emails = ['nitox34@gmail.com','ahmed0saber33@gmail.com']
    
    @staticmethod
    def get_demo_args():
        return 'name', 'email', 'description'
    
class SendMassage(EmailNotification):
    template_name = 'message' 
    subject = 'welcome to quran_mail' 

    def __init__(self, user) -> None:
        self.context = {'domain':settings.DOMAIN}
        self.to_emails = [user.email]
        
    @staticmethod
    def get_demo_args():
        return  'test@gmail.com'
    
