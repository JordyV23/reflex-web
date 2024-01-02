import reflex as rx
from reflex_web.components import link_button,title
from reflex_web.styles.styles import Size
from reflex_web.constants import TWITTER,LINKEDIN,REPOS

def links() -> rx.Component:
    return rx.vstack(
        title("Comunidad"),
        link_button(
            "GitHub"
            ,"Echale un vistazo a mis repositorios"
            ,REPOS
        ),
        link_button(
            "Twitter"
            ,"Contactame por medio de Redes Sociales"
            ,TWITTER
        ),
        link_button(
            "LinkedIn"
            ,"Que tal si conectamos? :)"
            ,LINKEDIN
        ),
        width="100%",
        spacing=Size.MEDIUM.value
    )