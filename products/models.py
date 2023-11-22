from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


# Create your models here.

class Photos(models.Model):
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='products_photos')

    class Meta:
        verbose_name_plural = 'Photos'

    def __str__(self):
        return f'[{self.id}] {self.description}'


class CallbackRequests(models.Model):
    telephone = models.TextField()

    class Meta:
        verbose_name_plural = 'CallbackRequests'

    def __str__(self):
        return f'[{self.id}] {self.telephone}'


class ProcessesCards(models.Model):
    title = CKEditor5Field()
    content = CKEditor5Field()
    link_title = models.TextField(blank=True)
    link_url = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'ProcessesCards'

    def __str__(self):
        return f'[{self.id}] {self.title}'


class ImportantInformation(models.Model):
    content = CKEditor5Field()

    class Meta:
        verbose_name_plural = 'ImportantInformation'

    def __str__(self):
        return f'[{self.id}] {self.content}'


class InformationCircles(models.Model):
    title = models.TextField()
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'InformationCircles'

    def __str__(self):
        return f'[{self.id}] {self.title}'


class OtherLinks(models.Model):
    name = models.TextField()
    url = models.TextField()
    display = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'OtherLinks'

    def __str__(self):
        return f'[{self.id}] {self.name}'


class Statistics(models.Model):
    title = models.TextField()
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'Statistics'

    def __str__(self):
        return f'{self.title}'


class InformationCards(models.Model):
    icon = models.TextField()
    title = models.TextField()
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'InformationCards'

    def __str__(self):
        return f'[{self.id}] {self.title}'


class TableRows(models.Model):
    name = models.TextField()
    order = models.IntegerField()
    first = models.TextField(blank=True)
    second = models.TextField(blank=True)
    third = models.TextField(blank=True)
    fourth = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'TableRows'

    def __str__(self):
        return f'[{self.id}] {self.name}'


class PrivacyBlocks(models.Model):
    title = models.TextField()
    content = CKEditor5Field(blank=True)
    number = models.IntegerField()

    class Meta:
        verbose_name_plural = 'PrivacyBlocks'

    def __str__(self):
        return f'[{self.id}] {self.title}'


class ProcessesBlocks(models.Model):
    title = CKEditor5Field(config_name='extends')
    content = CKEditor5Field(blank=True, config_name='extends')
    number = models.IntegerField()

    class Meta:
        verbose_name_plural = 'ProcessesBlocks'

    def __str__(self):
        return f'[{self.id}] {self.title}'


class ChangeableInformation(models.Model):
    name = models.TextField()
    info = CKEditor5Field(config_name='extends')

    class Meta:
        verbose_name_plural = 'ChangeableInformation'

    def __str__(self):
        return f'{self.name}'
