from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(WhyUs)
class WhyUserAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')
    search_fields = ('title',)
    list_filter = ('title',)


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_filter = ('title',)


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_filter = ('title',)


@admin.register(ServiceInfo)
class ServiceInfoAdmin(admin.ModelAdmin):
    list_display = ('service_name', 'description')
    search_fields = ('service_name',)
    list_filter = ('service_name',)


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('service_name', 'phone_number', 'full_name', 'is_checkout')
    search_fields = ('phone_number', 'full_name')
    list_filter = ('service_name',)


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Projects)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'service')
    search_fields = ('title',)
    list_filter = ('title', 'tags')


@admin.register(FaqType)
class FaqTypeAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_filter = ('title',)


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'faq_type')
    search_fields = ('question', 'answer')
    list_filter = ('question', 'faq_type')


@admin.register(Features)
class FeaturesAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_checkout')
    search_fields = ('title',)
    list_filter = ('title',)


@admin.register(PriceList)
class PriceListAdmin(admin.ModelAdmin):
    list_display = ('price', 'limit_user', 'limit_date')
    search_fields = ('price', 'limit_user', 'limit_date')
    list_filter = ('price', 'limit_user', 'limit_date')


@admin.register(Partners)
class PartnersAdmin(admin.ModelAdmin):
    list_display = ('image',)


@admin.register(Workers)
class WorkersAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'profession')
    search_fields = ('full_name', 'profession')
    list_filter = ('full_name', 'profession')


@admin.register(FeadBack)
class FeadBackAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'description', 'profession')
    search_fields = ('full_name',)
    list_filter = ('full_name', 'profession')


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'inform')
    search_fields = ('title',)
    list_filter = ('title',)
