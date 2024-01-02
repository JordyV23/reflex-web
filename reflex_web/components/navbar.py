import reflex as rx
from reflex_web.styles import Size,Color

def navbar() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.span("Dev",color=Color.SECONDARY.value),
            rx.span("23",color=Color.PRIMARY.value),        
        ),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x= Size.BIG.value,
        padding_y= Size.DEFAULT.value,
        z_index="999",
        top="0",
    )