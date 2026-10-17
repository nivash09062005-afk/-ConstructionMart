from django.test import TestCase, override_settings
from django.urls import reverse

from .models import Order, Product


@override_settings(STORAGES={
    "default": {"BACKEND": "django.core.files.storage.FileSystemStorage"},
    "staticfiles": {"BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage"},
})
class CheckoutPaymentMethodTests(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name="Demo cement",
            category="cement",
            price="450.00",
            stock=5,
        )
        session = self.client.session
        session["cart"] = {str(self.product.pk): 1}
        session.save()

    def checkout_data(self, payment_method):
        return {
            "customer_name": "Test Customer",
            "email": "customer@example.com",
            "phone": "9876543210",
            "delivery_address": "Test address",
            "payment_method": payment_method,
        }

    def test_available_methods_are_shown_on_checkout(self):
        response = self.client.get(reverse("checkout"))

        self.assertEqual(response.status_code, 200)
        for value, label in Order.PAYMENT_CHOICES:
            self.assertContains(response, label)
            self.assertContains(response, f'value="{value}"')

    def test_selected_payment_method_is_saved_with_order(self):
        for method, _label in Order.PAYMENT_CHOICES:
            with self.subTest(method=method):
                session = self.client.session
                session["cart"] = {str(self.product.pk): 1}
                session.save()
                response = self.client.post(
                    reverse("checkout"),
                    self.checkout_data(method),
                )

                self.assertEqual(response.status_code, 302)
                self.assertEqual(Order.objects.latest("pk").payment_method, method)

    def test_invalid_payment_method_does_not_create_order(self):
        response = self.client.post(
            reverse("checkout"),
            self.checkout_data("not-a-payment-method"),
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Order.objects.count(), 0)
        self.assertContains(response, "choose a payment method")
