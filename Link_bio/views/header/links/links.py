import reflex as rx
from Link_bio.components.link_buttom import link_buttom


def links() -> rx.Component:
    return rx.vstack(
        link_buttom("twitch", "https://github.com/mouredev/python-web?tab=readme-ov-file"),
        link_buttom("Youtube", "https://github.com/mouredev/python-web?tab=readme-ov-file"),
        link_buttom("Youtube (Canal secundario)", "https://github.com/mouredev/python-web?tab=readme-ov-file"),
        link_buttom("Discord", "https://github.com/mouredev/python-web?tab=readme-ov-file"),
    )