import reflex as rx
from reflex_web.components import link_button,title
from reflex_web.styles.styles import Size
import reflex_web.constants  as const

def links() -> rx.Component:
    return rx.vstack(
        title("Comunidad"),
        link_button(
            "GitHub"
            ,"Echale un vistazo a mis repositorios"
            ,const.REPOS
            ,"github.svg"
        ),
        link_button(
            "Twitter"
            ,"Contactame por medio de Redes Sociales"
            ,const.TWITTER
            ,"x.svg"
        ),
        link_button(
            "LinkedIn"
            ,"Que tal si conectamos? :)"
            ,const.LINKEDIN
            ,"linkedin.svg"
        ),
        width="100%",
        spacing=Size.MEDIUM.value
    )