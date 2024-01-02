import reflex as rx
from reflex_web.styles.styles import Size


def info_text(title:str, body:str) -> rx.Component:
    return rx.box(
        rx.span(title, Font_weight="bold",color="red"),
        f" {body}", font_size=Size.MEDIUM.value
    )