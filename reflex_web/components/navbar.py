import reflex as rx

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "Dev23",
            height="40px"
        ),
        position="sticky",
        bg="#FF5733",
        padding="16px",
        z_index="999"
    )