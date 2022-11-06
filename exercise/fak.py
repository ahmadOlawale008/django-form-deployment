import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'exercise.settings')
import django
django.setup()
from faker import Faker
fakegen = Faker()
import random
from base.models import User
def add_topic(n):
    for entry in range(n):
        names = fakegen.name()
        first_name, second_name = names.split()
        t= User.objects.get_or_create(first_name= first_name, last_name=second_name, email=fakegen.email())[0]
        t.save()
        return t

if __name__ == '__main__':
    print('Processing...........')
    add_topic(1000)
    print('Completed')