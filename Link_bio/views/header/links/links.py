import reflex as rx
from Link_bio.components.link_buttom import link_buttom
from Link_bio.components.title import title
from Link_bio.styles.styles import Spacing as Spacing


def links() -> rx.Component:
    return rx.vstack(
        title("Comunidad"),
        link_buttom("twitch", 
                    "Directos de lunes a viernes",
                    "https://github.com/mouredev/python-web?tab=readme-ov-file"
                    ),
        link_buttom("Youtube", 
                    "Directos de lunes a viernes",
                    "https://github.com/mouredev/python-web?tab=readme-ov-file"
                    ),
        link_buttom("Youtube (Canal secundario)", 
                    "Directos de lunes a viernes",
                    "https://github.com/mouredev/python-web?tab=readme-ov-file"
                    ),
        link_buttom("Discord", 
                    "Directos de lunes a viernes",
                    "https://github.com/mouredev/python-web?tab=readme-ov-file"
                    ),
        title("Comunidad"),
        link_buttom("twitch", 
                    "Directos de lunes a viernes",
                    "https://github.com/mouredev/python-web?tab=readme-ov-file"
                    ),
        link_buttom("Youtube", 
                    "Directos de lunes a viernes",
                    "https://github.com/mouredev/python-web?tab=readme-ov-file"
                    ),
        link_buttom("Youtube (Canal secundario)", 
                    "Directos de lunes a viernes",
                    "https://github.com/mouredev/python-web?tab=readme-ov-file"
                    ),
        link_buttom("Discord", 
                    "Directos de lunes a viernes",
                    "https://github.com/mouredev/python-web?tab=readme-ov-file"
                    ),
        width="100%",
        spacing=Spacing.SMALL.value,
        
    )