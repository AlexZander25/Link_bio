import reflex as rx
from Link_bio.components.navbar import navbar
from Link_bio.components.footer import footer
from Link_bio.views.header.header import header
from Link_bio.views.header.links.links import links

class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.vstack(
        navbar(),
        header(),
        links(),
        footer(),
    )
    

app = rx.App()
app.add_page(index) 