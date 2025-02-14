
from restoapp.models import Menu




def links(request):
    m=Menu.objects.all()
    context={'links':m}
    return context

