import reflex as rx
import datetime
from Link_bio.styles.styles import Size as Size

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="favicon.ico"),
        rx.link(
            f"© 2014-{datetime.date.today().year} MoureDev by Brais Moure v4.", 
            href="https://github.com/mouredev/python-web?tab=readme-ov-file",
            is_external=True
        ),
        rx.text("Logo GitHub BUILDING SOFTWARE WITH ♥ FROM GALICIA TO THE WORLD.",
                font_size=Size.MEDIUM.value),
        margin_botton=Size.BIG.value,
        margin_top="0px !important",
        align="center",
    )