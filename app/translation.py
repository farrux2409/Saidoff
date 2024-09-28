from modeltranslation.translator import translator, TranslationOptions
from .models import *


class WhyUsTranslation(TranslationOptions):
    fields = ('title', 'description')


class CertificateTranslation(TranslationOptions):
    fields = ('title', 'inform')


class FeedBackTranslation(TranslationOptions):
    fields = ('description',)


class FAQTranslation(TranslationOptions):
    fields = ('answer', 'question')


class PricePlanTranslation(TranslationOptions):
    fields = ('limit_date', 'limit_user', 'price')


class FeatureTranslation(TranslationOptions):
    fields = ('title',)


class ServiceTranslation(TranslationOptions):
    fields = ('title',)


for a, b in [(Certificate, CertificateTranslation), (WhyUs, WhyUsTranslation), (FeadBack, FeedBackTranslation),
             (Faq, FAQTranslation), (PriceList, PricePlanTranslation), (Features, FeatureTranslation),
             (Services, ServiceTranslation)]:
    translator.register(a, b)
