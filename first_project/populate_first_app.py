import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

import random
from first_app.models import Topic, Webpage, AccessRecord
from faker import Faker

fakegen = Faker()

topics = ['Social', 'News', 'Games', 'Marketplace', 'Search']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(n=5):
    for _ in range(n):
        top = add_topic()

        fake_name = fakegen.company()
        fake_date = fakegen.date()
        fake_url = fakegen.url()

        webpg = Webpage.objects.get_or_create(topic=top, name=fake_name, url=fake_url)[0]
        webpg.save()

        access_record = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]
        access_record.save()



if __name__=='__main__':
    print('populating ...')
    populate(20)
    print('populating done !...')

