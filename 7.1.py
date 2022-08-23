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
    men = BusinessContact(name=fake.name(), surname=fake.surname(), priv_phone=fake.priv_phone(), email=fake.email(),
              position_job=fake.position_job(), business=fake.business(), business_phone=fake.business_phone())


type_card = int(input("Wybierz typ wizytówki 1.prywatna 2.biznesowa:  "))
how_many = int(input("Podaj ilosc wizytowek:  "))
    
for i in range(how_many):
    if type_card == 1:
        contact = f"{fake.name()}, {fake.surname()}, {fake.priv_phone()}, {fake.email()}"
        print(contact)
    elif type_card == 2:
        contact = f"{fake.name()}, {fake.surname()}, {fake.business_phone()}, {fake.email()}, {fake.position_job}. {fake.business}"
        print(contact)

    
