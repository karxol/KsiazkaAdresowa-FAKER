from faker import Faker
fake = Faker("pl_PL")

class BaseContact:
    def __init__(self,name,surname,priv_phone,email):
        self.name= name
        self.surname= surname
        self.priv_phone= priv_phone
        self.email= email
    
    def contact(self):
        return f'Wybieram numer {self.priv_phone} i kontaktuje się z {self.name} {self.surname} '

    @property
    def label_lenght(self):
        return sum([len(self.first_name), len(self.last_name)])

class BusinessContact(BaseContact):
    def __init__(self, position_job, business, business_phone,  *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.position_job = position_job
       self.business = business
       self.business_phone = business_phone
       
    def contact_work(self):
        return f'Wybieram numer do {self.business_phone} i kontaktuje się z {self.name} {self.surname}'
    

    
