# manage views

import flet as ft

from logic import (
    on_click_btn_nw,
    on_click_btn_mp
)

def home_view(page: ft.Page) -> ft.View:
    return ft.View(
        route = "/", # main route of the application
        controls = [ # page controls
            ft.Text("Main Window"),
            ft.ElevatedButton("New Window, click on me", on_click = on_click_btn_nw),
        ]
    )
#
def nw_view(page: ft.Page) -> ft.View:
    return ft.View(
        route = "/new",
        controls = [
            ft.Text("New Window"),
            ft.ElevatedButton("Back to Main Window", on_click=on_click_btn_mp),
        ]
    )