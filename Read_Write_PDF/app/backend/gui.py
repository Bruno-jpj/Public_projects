# manage the gui 
# create different windows 
import flet as ft
from routes import routes

def home_page(page: ft.Page):
    page.title = "Read and Write PDF"
    page.window_width = 800
    page.window_height = 600
    page.window_resizable = True
    page.window_min_width = 800
    page.window_min_height = 600
    #
    # collega il gestore delle route
    page.on_route_change = routes(page)

    # attiva la route iniziale
    page.go(page.route)

#