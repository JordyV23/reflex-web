import reflex as rx
import datetime
from reflex_web.styles.styles import Size,TextColor,Color

year = datetime.date.today().year

def footer() -> rx.Component:
    return rx.vstack(
        rx.text(
            f"Powered By", 
            font_size=Size.MEDIUM.value
        ),
        rx.image(
            src="favicon.ico",
        ),
        rx.text(
            f"© {year} Dev23 by Jordy Vargas",
            font_size=Size.DEFAULT.value
        ),
        rx.image(
            src="Dev23.ico",
            width="100px",
            height="auto",
            border_radius="15px 50px",
            border= f"5px solid {Color.PRIMARY.value}",
            box_shadow="lg",
        ),
        rx.text(
            "All Made With Passion",
            font_size=Size.MEDIUM.value
        ),
        padding_bottom=Size.BIG.value,
        margin_bottom=Size.BIG.value,
        padding_x=Size.BIG.value,
        spacing=Size.DEFAULT.value,
        color=TextColor.FOOTER.value
    )