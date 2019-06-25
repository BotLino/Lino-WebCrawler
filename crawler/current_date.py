from datetime import timedelta, datetime


def get_first_day_week(signal):
    date_format = '%d' + signal + '%m' + signal + '%Y'

    today = datetime.today().date()
    today = today + timedelta(days=1)
    today = today.strftime('%d/%m/%Y')

    dt = datetime.strptime(today, '%d/%m/%Y')

    start = dt - timedelta(days=dt.weekday())
    start = start.strftime(date_format)

    return start
