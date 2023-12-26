import reflex as rx
import datetime

year = datetime.date.today().year

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="favicon.ico"),
        rx.text(f"© {year} Dev23 by Jordy Vargas"),
        rx.text("All Made With Passion")
    )