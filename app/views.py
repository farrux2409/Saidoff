from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, ListCreateAPIView
from rest_framework.permissions import AllowAny

from .serializers import *


class WhyUsView(ListAPIView):
    serializer_class = AboutModelSerializer
    queryset = WhyUs.objects.all()
    permission_classes = (AllowAny,)


class OurServiceView(ListAPIView):
    serializer_class = ServiceModelSerializer
    queryset = Services.objects.all()
    permission_classes = (AllowAny,)


class ServiceCategoryView(ListAPIView):
    serializer_class = ServiceCategoryModelSerializer
    queryset = ServiceCategory.objects.all()
    permission_classes = (AllowAny,)


class ServiceInfoView(RetrieveAPIView):
    serializer_class = ServiceInfoModelSerializer
    queryset = ServiceInfo.objects.all()
    permission_classes = (AllowAny,)
    lookup_field = 'pk'


class PartnersView(ListAPIView):
    serializer_class = PartnersModelSerializer
    queryset = Partners.objects.all()
    permission_classes = (AllowAny,)


class FeaturesView(ListAPIView):
    serializer_class = FeatureModelSerializer
    queryset = Features.objects.all()
    permission_classes = (AllowAny,)


class PriceListView(ListAPIView):
    serializer_class = PriceListModelSerializer
    queryset = PriceList.objects.all()
    permission_classes = (AllowAny,)


class WorkersView(ListAPIView):
    serializer_class = WorkersModelSerializer
    queryset = Workers.objects.all()
    permission_classes = (AllowAny,)


class FaqTypeView(ListAPIView):
    serializer_class = FaqTypeModelSerializer
    queryset = FaqType.objects.all()
    permission_classes = (AllowAny,)


class FaqsView(ListAPIView):
    serializer_class = FaqModelSerializer
    queryset = Faq.objects.all()
    permission_classes = (AllowAny,)


class CertificateView(ListAPIView):
    serializer_class = CertificatesModelSerializer
    queryset = Certificate.objects.all()
    permission_classes = (AllowAny,)


class OrdersView(ListAPIView):
    serializer_class = OrdersModelSerializer
    queryset = Orders.objects.all()
    permission_classes = (AllowAny,)


class OrderCreateView(CreateAPIView):
    serializer_class = OrdersModelSerializer
    queryset = Orders.objects.all()
    permission_classes = (AllowAny,)


class ProductsView(ListAPIView):
    serializer_class = ProjectsModelSerializer
    queryset = Projects.objects.all()
    permission_classes = (AllowAny,)


class TagsView(ListAPIView):
    serializer_class = TagsModelSerializer
    queryset = Tags.objects.all()
    permission_classes = (AllowAny,)


class CommentsView(ListAPIView):
    serializer_class = CommentsModelSerializer
    queryset = FeadBack.objects.all()
    permission_classes = (AllowAny,)


class CommentCreateView(ListCreateAPIView):
    serializer_class = CommentsModelSerializer
    queryset = FeadBack.objects.all()
    permission_classes = (AllowAny,)
