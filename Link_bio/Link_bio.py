import reflex as rx
from Link_bio.components.navbar import navbar
from Link_bio.components.footer import footer
from Link_bio.views.header.header import header
from Link_bio.views.header.links.links import links
import Link_bio.styles.styles as styles
from Link_bio.styles.styles import Size as Size

class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value
            )
        ),
        footer()
    )    

app = rx.App(
    style=styles.BASE_STYLES)
app.add_page(index) 