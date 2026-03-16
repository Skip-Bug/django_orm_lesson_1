import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402

if __name__ == '__main__':
    # Программируем здесь
    # print('Количество пропусков:', Passcard.objects.count())  # noqa: T001
    passcard = Passcard.objects.all()
    some_card = passcard[1]

    print("owner_name", some_card.owner_name)
    print("passcode", some_card.passcode)
    print("created_at", some_card.created_at)
    print("is_active", some_card.is_active)
