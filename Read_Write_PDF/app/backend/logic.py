# manage the events: manage the events of the gui
# ex: click on a button "read pdf" and recall the logic to read the pdf file
from flet import ControlEvent

def on_click_btn_nw(event: ControlEvent):
    event.page.go("/new")
#
def on_click_btn_mp(event: ControlEvent):
    event.page.go("/")
#