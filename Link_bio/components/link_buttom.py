import reflex as rx
import Link_bio.styles.styles as styles


def link_buttom(tittle: str, body: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag="arrow_right",
                    width=styles.Size.BIG.value,
                    height=styles.Size.DEFAULT.value,
                ),
                rx.vstack(
                    rx.text(tittle, style=styles.button_tittle_style),
                    rx.text(body, style=styles.button_body_style),
                    aling_itmes="start"
                )
                
            )
        ),
        href=url,
        is_external=True,
        width="100%",
        text_decoration="none"
    )
    
