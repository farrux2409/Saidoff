from modeltranslation.translator import translator, TranslationOptions
from .models import *


class WhyUsTranslation(TranslationOptions):
    fields = ('title', 'description')


class CertificateTranslation(TranslationOptions):
    fields = ('title', 'inform')


class FeedBackTranslation(TranslationOptions):
    fields = ('description', 'full_name', 'profession')


class FAQTranslation(TranslationOptions):
    fields = ('answer', 'question')


class FAQTypeTranslation(TranslationOptions):
    fields = ('title',)


class PricePlanTranslation(TranslationOptions):
    fields = ('limit_date', 'limit_user', 'price')


class FeatureTranslation(TranslationOptions):
    fields = ('title',)


class ServiceTranslation(TranslationOptions):
    fields = ('title',)


class OrderTranslation(TranslationOptions):
    fields = ('full_name', 'message')


class WorkersTranslation(TranslationOptions):
    fields = ('full_name', 'profession')


class ProductTranslation(TranslationOptions):
    fields = ('title',)


class TagsTranslation(TranslationOptions):
    fields = ('title',)


for a, b in [(Certificate, CertificateTranslation), (WhyUs, WhyUsTranslation), (FeadBack, FeedBackTranslation),
             (Faq, FAQTranslation), (PriceList, PricePlanTranslation), (Features, FeatureTranslation),
             (Services, ServiceTranslation), (FaqType, FAQTypeTranslation), (Orders, OrderTranslation),
             (Projects, ProductTranslation), (Tags, TagsTranslation), (Workers, WorkersTranslation)]:
    translator.register(a, b)
