import reflex as rx
import datetime
from reflex_web.styles.styles import Size,TextColor

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
        rx.text(
            "All Made With Passion",
            font_size=Size.MEDIUM.value
        ),
        padding_bottom=Size.BIG.value,
        margin_bottom=Size.BIG.value,
        color=TextColor.FOOTER.value
    )