import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE",'newpro.settings')

import django
django.setup()





from django.contrib.auth.models import User
from faker import Faker

fakecr=Faker()

def populate(N=5):
    for entry in range(N):
        fake_name=fakecr.name().split()
        fake_firstname=fake_name[0]
        fake_lastname=fake_name[1]
        fake_email=fakecr.email()

        user = User.objects.get_or_create(FirstName=fake_firstname,LastName=fake_lastname,Email=fake_email)[0]

if __name__ == '__main__':
        print("Populating the script")
        populate(20)
        print("Populating done!")
