import reflex as rx
from reflex_web.styles import styles, Size

def link_icon(url:str, img:str) -> rx.Component:
    return rx.link(
        rx.image(
            src="icons/"+img,
            width=Size.LARGE.value,
            height=Size.LARGE.value,
        ),
        href=url,
        is_external=True,
    )