import reflex as rx
from reflex_web.styles.styles import Size,TextColor,Color

def info_text(title:str, body:str) -> rx.Component:
    return rx.box(
        rx.span(
            title, 
            Font_weight="bold",
            color=Color.PRIMARY.value,    
        ),
        f" {body}", 
        font_size=Size.DEFAULT.value,
        color= TextColor.BODY.value
    )