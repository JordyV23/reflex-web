import reflex as rx
from reflex_web.components import navbar,footer
from reflex_web.views import header, links

class State(rx.State):
    pass

def index() -> rx.component :
    return rx.vstack(
        navbar(),
        header(),
        links(),
        footer(),
    )
    
app = rx.App()
app.add_page(index)
app.compile()