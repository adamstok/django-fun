from normalview.models import Messages

def get_messages(request):
    if Messages.objects.all():
        return {'mess':'You have messages'}
    else:
        return {'mess': "You don't have any messages"}