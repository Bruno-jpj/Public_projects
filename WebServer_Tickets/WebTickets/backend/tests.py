from django.test import TestCase
from backend.models import (
    Bigliettoabbonamento,
    Metodopagamento,
    Stazione,
    Tratta,
    Treno,
    Trenostazione,
    Utente
)
from django.urls import reverse

# Create your tests here.
# test HomeLogic
class HomeLogicTestCase(TestCase):
    def setUp(self):
        # Create test data
        print()