from msilib import Feature

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


class ServiceInfoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceInfo
        fields = ['service_name', 'description', 'services']


class ProjectsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'


class FaqTypeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaqType
        fields = '__all__'


class FaqModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = '__all__'


class FeatureModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Features
        fields = '__all__'


class PriceListModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceList
        fields = '__all__'


class PartnersModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partners
        fields = '__all__'


class WorkersModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workers
        fields = '__all__'


class PortfolioModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = '__all__'


class CommentsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeadBack
        fields = '__all__'


class CertificatesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = '__all__'


class OrdersModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'


class TagsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = '__all__'
