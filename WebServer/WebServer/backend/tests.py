from django.test import TestCase
from backend.models import User, Site
from backend.views import site_list_view
from django.urls import reverse

# Create your tests here.

class UserTestModel(TestCase):
    def test_str_method(self):
        user = User.objects.create(Username="PurplePingu",Password="PurplePingu", Email="PurplePingu@gmail.com")
        self.assertAlmostEqual(str(user),"PurplePingu")
        # Questo verifica che il metodo __str__ nel models restituisca il titolo come previsto. 
#
class SiteListViewTest(TestCase):
    def test_site_list_view(self):
        # esempio di oggetto per il modello Site, i valori sono casuali tranne per category e slug
        site1 = Site.objects.create(
            title="Uno", 
            description="Contenuto uno", 
            category="Info", # devo mettere dentro un valore preso dalla category_choices ==> tuple list
            paid=False, 
            url="https://esempio.com",
            slug="uno"
            )
        
        site2 = Site.objects.create(title="Due", description="Contenuto due", category="Info",paid=True,url="https://esempio.com",slug="due")

        response = self.client.get(reverse('site_list_view')) 

        self.assertEqual(response.status_code, 200)

        self.assertContains(response, "Uno")
        self.assertFalse(site1.paid)
        self.assertEqual(site2.url,"https://esempio.com")