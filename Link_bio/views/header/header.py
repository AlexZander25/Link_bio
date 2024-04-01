import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(fallback="AA", variant="solid"),
        rx.text("@mouredev"),
        rx.text("Hola mi nombre es Alexander Arce"),
        rx.text("""Continuación del curso desde cero de 6 horas. 
                En esta sección más avanzada se aprenderán diferentes 
                conceptos relacionados con el desarrollo web con Python y Reflex: 
                Router, backend, APIs, eventos, estados, base de datos, Docker, y más...""")
    )