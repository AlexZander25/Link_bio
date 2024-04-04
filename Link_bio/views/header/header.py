import reflex as rx
from Link_bio.components.link_icon import link_icon
from Link_bio.components.info_text import info_text
from Link_bio.styles.styles import Spacing as Spacing

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(fallback="AA", size="6"),
            rx.vstack(
                rx.heading(
                    "Alexander Arce", 
                    size="6"
                    ),
                rx.text(
                    "@mouredev", 
                    size="3",
                    margin_top="0px !important"
                    ),
                rx.hstack(
                    link_icon("https://github.com/mouredev/python-web?tab=readme-ov-file"),
                    link_icon("https://github.com/mouredev/python-web?tab=readme-ov-file"),
                    link_icon("https://github.com/mouredev/python-web?tab=readme-ov-file"),
                ),
                align_items="start"
                
            ),
            spacing=Spacing.DEFAULT.value,          
        ),
        
        rx.flex(
            info_text("+13", "Anios de experiencia"), 
            rx.spacer(),           
            info_text("+13", "Anios de experiencia"),
            rx.spacer(),            
            info_text("+13", "Anios de experiencia"),
            width="100%"           
        ),
        
        rx.text("""Continuación del curso desde cero de 6 horas. 
                En esta sección más avanzada se aprenderán diferentes 
                conceptos relacionados con el desarrollo web con Python y Reflex: 
                Router, backend, APIs, eventos, estados, base de datos, Docker, y más..."""),
        spacing=Spacing.BIG.value,
        align_items="start"
    )