from django.test import TestCase
from .models import Orders, Services
from .validatorsfile import uzbek_phone_validator


class OrdersModelTestCase(TestCase):

    def setUp(self):
        # Creating a service instance for the order
        self.service = Services.objects.create(title='Test Service')

        # Creating an order instance
        self.order = Orders.objects.create(
            full_name='Farrux',
            phone_number='+998974707980',
            service_name=self.service,
            message='Test message',
            is_checkout=False
        )

    def test_order_creation(self):
        self.assertEqual(self.order.full_name, 'Farrux')
        self.assertEqual(self.order.phone_number, '+998974707980')
        self.assertEqual(self.order.service_name, self.service)
        self.assertEqual(self.order.message, 'Test message')
        self.assertFalse(self.order.is_checkout)

    def test_order_str_method(self):
        self.assertEqual(str(self.order), 'Farrux')
