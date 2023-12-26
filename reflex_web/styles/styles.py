import reflex as rx
from enum import Enum

# Constantes
MAX_WIDTH = "600px"

# Sizes
class Size(Enum): 
    SMALL="0.5em"
    DEFAULT="1em"
    BIG="2em"
    
# Styles
BASE_STYLE = {
    rx.Button: {
        "width": "100%",
        "height": "100%",
        "display":"block",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value
    }
}