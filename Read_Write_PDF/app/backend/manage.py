# start point for the backend application
import flet as ft 
from gui import home_page

def run_app():
    ft.app(target=home_page)
#
if __name__ == "__main__":
    run_app()