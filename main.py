import os
from django.utils.timezone import localtime
import django
from datetime import timedelta
from datacenter.models import Passcard, Visit  # noqa: E402
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()


def format_duration(duration):
    """Форматирует timedelta в строку Ч:М:С."""
    total_seconds = int(duration.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return f"{hours}:{minutes:02d}:{seconds:02d}"


def get_duration(visit):
    entered = localtime(visit.entered_at)
    if visit.leaved_at is None:
        now = localtime()
        duration = now - entered
    else:
        leaved = localtime(visit.leaved_at)
        duration = leaved - entered
    return duration, entered


def is_visit_long(visit, minutes=60):
    duration, entered = get_duration(visit)
    return duration > timedelta(minutes=minutes)


if __name__ == '__main__':
    # Программируем здесь
    # print('Количество пропусков:', Passcard.objects.count())  # noqa: T001
    # print('Количество активных пропусков:',
    #       Passcard.objects.filter(is_active=True).count()
    #       )
    # any_passcard = Passcard.objects.all()
    # print(any_passcard)
    # visits_passcard = Visit.objects.filter(passcard=any_passcard)
    # print('Визиты', visits_passcard)
    #     visits = Visit.objects.filter(
    #         passcard__is_active=True, leaved_at__isnull=False)
    # visits = Visit.objects.filter(passcard__is_active=True)
    # #        passcard__is_active=True,

    # all_visits = Visit.objects.filter(
    #     passcard__is_active=True).select_related('passcard')

    # long_visits = []
    # for visit in all_visits:
    #     if is_visit_long(visit, minutes=60):
    #         long_visits.append(visit)

    # print("Визиты дольше 60 мин", long_visits)
    # # for visit in visits:
    # #     duration, entered = get_duration(visit)
    # #     is_long = is_visit_long(visit)
    # #     print(
    # #         f"{visit.passcard.owner_name}\n"
    # #         "Зашёл в хранилище, время по Москве:\n"
    # #         f"{entered}\n\n"
    # #         "Находился в хранилище\n"
    # #         f"{format_duration(duration)}\n"
    # #     )
    # #     if is_long:
    # #         print("Подозрительная активность\n")
