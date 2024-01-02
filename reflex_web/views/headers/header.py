import reflex as rx


def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(name="Jordy Vargas", size="xl"),
        rx.text("@Dev23"),
        rx.text("Hola!✌️ Me llamo Jordy Vargas!🐏"),
        rx.text("Soy estudiante de ingeniería en tecnologías de la información, apasionado por la programación y ansioso por convertirme en un desarrollador full stack. Mi constante búsqueda de conocimiento me impulsa a aprender y crecer. ¡Bienvenido a mi viaje en el fascinante mundo de la programación!")
    )