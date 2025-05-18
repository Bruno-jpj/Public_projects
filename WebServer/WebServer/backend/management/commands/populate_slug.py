from django.core.management.base import BaseCommand
from backend.models import Site
from django.utils.text import slugify

class Command(BaseCommand):
    # help fornisce una breve descrizione del comando che può essere visualizzata quando si esegue python manage.py help.
    help = 'Popola gli slug per i siti che non ce l\'hanno'

    def handle(self, *args, **kwargs):

        count = 0

        for site in Site.objects.all():
            if not site.slug:
                # Lo slug viene creato usando slugify(site.title), che genera uno slug a partire dal titolo del sito.
                original_slug = slugify(site.title)

                slug = original_slug
                num = 1

                # assicura che lo slug sia unico
                while Site.objects.filter(slug=slug).exists():
                    # prima cicla e controlla se esiste, poi...
                    # aggiunge un numero progressivo se non esiste, es: site-title-1 -> site-title-2 -> etc
                    slug = f"{original_slug}-{num}"
                    num += 1
                #
                # slug del sito = slug univoco
                site.slug = slug
                # slug viene salvato e assegnato al sito nel db
                site.save()
                
                self.stdout.write(self.style.SUCCESS(f"✔ Slug creato per: {site.title} → {slug}"))
                count += 1

        if count == 0:
            self.stdout.write("✅ Tutti i siti hanno già uno slug.")
        else:
            self.stdout.write(f"✅ {count} slug creati.")
