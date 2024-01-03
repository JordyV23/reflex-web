import reflex as rx
from reflex_web.components import navbar,footer
from reflex_web.views import header, links
from reflex_web.styles import styles

# class State(rx.State):
#     pass

def index() -> rx.component :
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=styles.Size.BIG.value,
                padding=styles.Size.BIG.value
            ),
        ),
        footer(),
    )
    
app = rx.App(
    style = styles.BASE_STYLE,
    stylesheets=[
        "fonts/fonts.css"
    ]
)
app.add_page(
    index,
    title="Dev23 | FullStack developer",
    description="Hola, mi nombre es Jordy Vargas, desarrollador FullStack e ingeniero en tecnologías de la información",
    image="/profile.png",
)
app.compile()