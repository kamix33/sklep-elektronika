import os
import django
from django.core.management import call_command
import io

def dumpdata_utf8():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sklep.settings')
    django.setup()

    out = io.StringIO()
    call_command(
        'dumpdata',
        exclude=['auth.permission', 'contenttypes', 'admin.logentry', 'sessions'],
        stdout=out,
    )
    data = out.getvalue()

    with open('dane.json', 'w', encoding='utf-8') as f:
        f.write(data)

if __name__ == '__main__':
    dumpdata_utf8()
