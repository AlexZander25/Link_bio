import reflex as rx
from Link_bio.styles.styles import Size as Size

def navbar() -> rx.Component:
    return rx.vstack(
        rx.text(
            "Alexander",
        ),
        position="sticky",
        bg="lightgray",
        padding_x=Size.DEFAULT.value,
        padding_y=Size.SMALL.value,
        z_index="999",
        top="0"
    )
    