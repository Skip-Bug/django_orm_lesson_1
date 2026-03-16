import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402

if __name__ == '__main__':
    # Программируем здесь
    print('Количество пропусков:', Passcard.objects.count())  # noqa: T001
    some_cards = (Passcard.objects.all())

    active_passcards = []
    for some_card in some_cards:
        if some_card.is_active is True:
            active_passcards.append(some_card)
    print('Количество активных пропусков:', len(active_passcards))
