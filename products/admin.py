from django.contrib import admin

from products.models import Photos
from products.models import ImportantInformation
from products.models import InformationCircles
from products.models import OtherLinks
from products.models import ProcessesCards
from products.models import Statistics
from products.models import InformationCards
from products.models import TableRows
from products.models import PrivacyBlocks
from products.models import ProcessesBlocks
from products.models import ChangeableInformation

# Register your models here.
admin.site.register(Photos)
admin.site.register(TableRows)
admin.site.register(ImportantInformation)
admin.site.register(InformationCircles)
admin.site.register(OtherLinks)
admin.site.register(ProcessesCards)
admin.site.register(Statistics)
admin.site.register(InformationCards)
admin.site.register(PrivacyBlocks)
admin.site.register(ProcessesBlocks)
admin.site.register(ChangeableInformation)
