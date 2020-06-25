from normalview.models import Messages

def get_messages(request):
    if Messages.objects.all():
        return {'mess':'Masz wiadomośi'}
    else:
        return {'mess': 'Nie masz wiadomości'}