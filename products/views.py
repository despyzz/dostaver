from django.views import View
from django.shortcuts import render
from django.http import JsonResponse

from products.models import Photos
from products.models import CallbackRequests
from products.models import InformationCircles
from products.models import Statistics
from products.models import InformationCards
from products.models import ImportantInformation
from products.models import ProcessesCards
from products.models import TableRows
from products.models import OtherLinks
from products.models import PrivacyBlocks
from products.models import ProcessesBlocks
from products.models import ChangeableInformation

# Create your views here.

class CommonContextMixin:
    @staticmethod
    def get_common_context():
        return {
            'Telegram': OtherLinks.objects.get(name='Telegram'),
            'Whatsapp': OtherLinks.objects.get(name='Whatsapp'),
            'Telephone': OtherLinks.objects.get(name='Telephone'),
            'schedule': ChangeableInformation.objects.get(name='schedule'),
            'success': ChangeableInformation.objects.get(name='success'),
            'period': ChangeableInformation.objects.get(name='period'),
            'ip': ChangeableInformation.objects.get(name='ip'),
            'inn': ChangeableInformation.objects.get(name='inn'),
        }


class IndexView(CommonContextMixin, View):
    def get(self, request):
        context = {
            'title': 'Dostaver',
            'OwnerPhoto': Photos.objects.get(description='owner').photo,
            'StatisticsPhoto': Photos.objects.get(description='statistics').photo,
            'InformationCircles': InformationCircles.objects.all(),
            'Statistics': Statistics.objects.first(),
            'InformationCards': InformationCards.objects.all(),
            'ImportantInformation': ImportantInformation.objects.all(),
            'ProcessesCards': ProcessesCards.objects.all(),
            'TableRows': TableRows.objects.order_by('order'),
        }
        context.update(self.get_common_context())
        return render(request, 'products/index.html', context)


class PrivacyView(CommonContextMixin, View):
    def get(self, request):
        context = {
            'title': 'Dostaver - Политика конфиденциальности',
            'PrivacyBlocks': PrivacyBlocks.objects.order_by('number')
        }
        context.update(self.get_common_context())
        return render(request, 'products/privacy.html', context)


class RulesView(CommonContextMixin, View):
    def get(self, request):
        context = {
            'title': 'Dostaver - Правила',
            'ProcessesBlocks': ProcessesBlocks.objects.order_by('number'),
        }
        context.update(self.get_common_context())
        return render(request, 'products/rules.html', context)


class NotFoundView(CommonContextMixin, View):
    def get(self, request):
        context = {
            'title': 'Error 404',
        }
        context.update(self.get_common_context())
        return render(request, 'products/error404.html', context)

def page_not_found_view(request, exception):
    return render(request, "products/error404.html", status=404)
