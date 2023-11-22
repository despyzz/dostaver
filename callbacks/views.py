from django.views import View
from django.http import JsonResponse

from callbacks.models import CallbackRequests


# Create your views here.

class ReceiveFormView(View):
    @staticmethod
    def post(request):
        telephone = request.POST.get('telephone')
        callback_type = request.POST.get('callback-type')

        new_request = CallbackRequests(telephone=telephone, callback_type=callback_type)
        new_request.save()

        return JsonResponse({'status': 'ok'}, status=200)
