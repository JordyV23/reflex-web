import reflex as rx
from reflex_web.components import link_button,title

def links() -> rx.Component:
    return rx.vstack(
        title("Comunidad"),
        link_button(
            "GitHub"
            ,"Echale un vistazo a mis repositorios"
            ,"https://github.com/JordyV23"
        ),
        link_button(
            "Twitter"
            ,"Contactame por medio de Redes Sociales"
            ,"https://twitter.com/Jordy_Dev23"
        ),
        link_button(
            "LinkedIn"
            ,"Que tal si conectamos? :)"
            ,"https://www.linkedin.com/in/jordy-jhv/"
        ),
        width="100%"
    )