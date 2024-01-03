import reflex as rx
from reflex_web.styles import Size,styles,Color

def link_button(title:str, body:str, url:str, img:str) -> rx.Component :
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src= "icons/" + img,
                    width= Size.BIG.value,
                    height= Size.BIG.value,
                    margin= Size.MEDIUM.value,
                    color= Color.PRIMARY.value,
                ),
                rx.vstack(
                    rx.text(title, 
                        style=styles.button_title_style
                    )
                    ,rx.text(body, 
                        style=styles.button_body_style
                    ),
                    spacing=Size.SMALL.value,
                    align_items="start",
                    margin=Size.ZERO.value
                ),
            )
        ),
        href=url,
        is_external=True,
        width="100%",
    )