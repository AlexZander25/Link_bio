import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(fallback="AA", size="6"),
            rx.vstack(
                rx.text("Alexander Arce", size="4"),
                rx.text("@mouredev", size="3"),
            )
            
        ),
        rx.text("""Continuación del curso desde cero de 6 horas. 
                En esta sección más avanzada se aprenderán diferentes 
                conceptos relacionados con el desarrollo web con Python y Reflex: 
                Router, backend, APIs, eventos, estados, base de datos, Docker, y más...""")
    )