
from rest_framework import serializers

from .models import *


class AboutModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhyUs
        fields = ['title', 'image', 'description']


class ServiceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = ['title', ]


class ServiceCategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = ['title', 'service']


class ServiceInfoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceInfo
        fields = ['service_name', 'description', 'service_cat']


class ProjectsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['title', 'image', 'link', 'service', 'tags']


class FaqTypeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaqType
        fields = ['title', ]


class FaqModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = ['question', 'answer', 'faq_type']


class FeatureModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Features
        fields = ['title', 'is_checkout', 'price_list']


class PriceListModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceList
        fields = ['title', 'price', 'limit_date', 'limit_user']


class PartnersModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partners
        fields = ['image', ]


class WorkersModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workers
        fields = ['full_name', 'image', 'profession']


class CommentsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeadBack
        fields = ['full_name', 'profession', 'description', 'image']


class CertificatesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ['title', 'image', 'inform']


class OrdersModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ['full_name', 'phone_number', 'service_name', 'message', 'is_checkout']


class TagsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ['title', ]
