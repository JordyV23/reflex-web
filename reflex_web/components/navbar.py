import reflex as rx
from reflex_web.styles.styles import Size

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "Dev23",
        ),
        position="sticky",
        bg="lightgray",
        padding_x= Size.DEFAULT.value,
        padding_y= Size.DEFAULT.value,
        z_index="999",
        top="0",
    )