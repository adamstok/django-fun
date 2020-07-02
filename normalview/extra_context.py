from datetime import datetime,timedelta

def show_time(request):
    now = datetime.now()
    two_hours_timezone = datetime.now() + timedelta(hours=2)
    hour = '{:%H:%M}'.format(two_hours_timezone)
    return {'now':now.strftime("%Y-%m-%d"),'hour':hour}

