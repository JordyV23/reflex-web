import reflex as rx
from reflex_web.components import link_icon, info_text
from reflex_web.styles.styles import Size, TextColor, Color
from reflex_web.constants import GITHUB

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                name="Jordy Vargas", 
                size="xl",
                color=TextColor.HEADER.value,
                src="profile.png",
                bg=Color.CONTENT.value,
                border="4px",
                border_color=Color.PRIMARY.value
            ),
            rx.vstack(
                rx.heading(
                    "Hola!✌️ Me llamo Jordy Vargas!🐏",
                    size="md",
                    color=TextColor.HEADER.value,
                ),
                rx.text(
                    "@Dev23",
                    margin_top="0px !important",
                    color=TextColor.BODY.value,
                ),
                rx.hstack(
                    link_icon(GITHUB,"github.svg"),  
                ),
                align_items="start",
            ),
            spacing=Size.DEFAULT.value, 
        ),
        rx.flex(
          info_text("Mobile","Development"),
          rx.spacer(),  
          info_text("Data","Bases"),
          rx.spacer(),  
          info_text("Web","Development"),
          rx.spacer(),  
          info_text("Data","Science"),
          width="100%",
        ),
        rx.text(
            "Soy estudiante de ingeniería en tecnologías de la información, apasionado por la programación y ansioso por convertirme en un desarrollador full stack. Mi constante búsqueda de conocimiento me impulsa a aprender y crecer. ¡Bienvenido a mi viaje en el fascinante mundo de la programación!",
            color=TextColor.BODY.value
        )
        ,spacing=Size.BIG.value
        ,align_items="start"
    )