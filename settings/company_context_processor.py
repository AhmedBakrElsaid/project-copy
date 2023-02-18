
from .models import Company


def get_info(request):
    info = Company.objects.last()
    return {'info': info}
    