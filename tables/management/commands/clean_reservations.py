import schedule
import time
from django.utils import timezone
from django.db.models import F
from tables.models import ReservedTable

def clean_expired_reservations():
    expired_reservations = ReservedTable.objects.filter(
        data__lt=timezone.now() - F('duration')
    )

    expired_reservations.delete()
    print('Expired reservations cleaned successfully.')

schedule.every(1).minutes.do(clean_expired_reservations)

print('run script')

while True:
    schedule.run_pending()
    time.sleep(1)
