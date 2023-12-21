import reflex as rx

class State(rx.State):
    pass

def index() -> rx.component :
    return rx.text("Hola Reflex",color="blue")

app = rx.App()
app.add_page(index)
app.compile()