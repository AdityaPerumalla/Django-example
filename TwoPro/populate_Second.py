import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','TwoPro.settings')

import django
django.setup()

import random
from Second.models import Topic,AccessRecord,WebPage
from faker import Faker
fakegen=Faker()
topics=['Social','Search','News','Games','Marketplace']

def add_topic():
    t=Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):

    for entry in range(N):
        top=add_topic()

        fake_url=fakegen.url()
        fake_date=fakegen.date()
        fake_name=fakegen.company()

        webpg=WebPage.objects.get_or_create(name=fake_name,url=fake_url)[0]
        acc=AccessRecord.objects.get_or_create(date=fake_date)[0]

if __name__ == '__main__':
    print('populate Script!')
    populate(10)
    print('populate Completed')
