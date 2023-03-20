import os

from django.conf import settings

smd_folder = os.path.join(settings.FROM_HOSTING, 'pages', 'smd')


def clear_data(smd_text):
    print(smd_text[:10])


def import_firm():
    pass


def import_smd():
    for root, dirs, files in os.walk(smd_folder): # пройти по директории рекурсивно
        for name in files:
            full_name = os.path.join(root, name)
            if os.path.isfile(full_name):
                with open(full_name, 'r') as smd_text:
                    data = clear_data(smd_text.read())
    print('ok')

