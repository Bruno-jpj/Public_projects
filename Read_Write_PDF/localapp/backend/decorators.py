from django.http import HttpRequest
from django.contrib import messages
from django.shortcuts import redirect, render

from pathlib import Path
from functools import wraps

FOLDERPATH = r'localapp\pdf'

def show_pdf(func):
    @wraps(func)
    def wrapper(self, request, *args, **kwargs):
        try:
            folder = Path(FOLDERPATH)
            pdf_files = [f.name for f in folder.glob("*.pdf") if f.is_file()]
        except Exception as e:
            messages.info(request, f"Errore nella ricerca PDF: {e}")
            pdf_files = []
        # Inserisci pdf_files dentro request per passarli alla view
        request.pdf_files = pdf_files 
        return func(self, request, *args, **kwargs)
    return wrapper
#           