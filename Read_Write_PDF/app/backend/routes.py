# manage routes

from view import (
    home_view,
    nw_view,
)

def routes(page):
    def route_change(route):
        page.views.clear()

        if page.route == "/":
            page.views.append(home_view(page))
        elif page.route == "/new":
            page.views.append(nw_view(page))

        page.update()

    return route_change