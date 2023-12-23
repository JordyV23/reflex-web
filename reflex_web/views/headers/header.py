import reflex as rx


def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(name="Jordy Vargas", size="xl"),
        rx.text("@Dev23"),
        rx.text("Saludo"),
        rx.text("Presentacion")
    )