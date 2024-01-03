import reflex as rx
from reflex_web.styles import Size,Color,navbar_style

def navbar() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.span("Dev",color=Color.SECONDARY.value),
            rx.span(
                "23",
                color=Color.PRIMARY.value,
                background_image="linear-gradient(271.68deg, #D92938 0.75%, #8C0839 88.52%)",
                background_clip="text",
            ),
            style=navbar_style
        ),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x= Size.BIG.value,
        padding_y= Size.DEFAULT.value,
        z_index="999",
        top="0",
    )