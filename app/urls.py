from django.urls import path

from .views import *

urlpatterns = [
    path('why-us/', WhyUsView.as_view()),
    path('services/', OurServiceView.as_view()),
    path('service-info/<int:pk>/', ServiceInfoView.as_view()),
    path('service-category', ServiceCategoryView.as_view()),
    path('partners/', PartnersView.as_view()),
    path('prices/', PriceListView.as_view()),
    path('features/', FeaturesView.as_view()),
    path('workers/', WorkersView.as_view()),
    path('faq-type/', FaqTypeView.as_view()),
    path('faq/', FaqsView.as_view()),
    path('orders/', OrdersView.as_view()),
    path('order-create/', OrderCreateView.as_view()),
    path('feadbacks/', CommentsView.as_view()),
    path('feadback-create/', CommentCreateView.as_view()),
    path('projects/', ProductsView.as_view()),

]
