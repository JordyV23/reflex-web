import reflex as rx
from enum import Enum
from .colors import Color,TextColor
from .fonts import Font

# Constantes
MAX_WIDTH = "600px"

# Sizes
class Size(Enum):
    ZERO="0px !important" 
    SMALL="0.5em"
    MEDIUM="0.8em"
    DEFAULT="1em"
    LARGE="1.5em"
    BIG="2em"
    
# Styles
BASE_STYLE = {
    "font_family":Font.DEFAULT.value,
    "background_color":Color.BACKGROUND.value,
    rx.Button: {
        "width": "100%",
        "height": "100%",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
        "color":TextColor.HEADER.value,
        "background_color":Color.CONTENT.value,
        "white_space":"normal",
        "text_align":"start",
        "_hover": {
            "background_color":Color.SECONDARY.value,            
        }       
    },
    rx.Link: {
        "text_decoration":"none",
        "_hover":{},
    }
}

navbar_style = dict(
    font_size = Size.BIG.value,
    font_family= Font.LOGO.value
)

title_style = dict(
    width="100%",
    padding_top=Size.DEFAULT.value,
    color=TextColor.HEADER.value,
)

button_title_style = dict(
    font_family = Font.TITLE.value,
    font_size = Size.DEFAULT.value,
    color = TextColor.HEADER.value,
)

button_body_style = dict(
    font_size = Size.MEDIUM.value,
    color = TextColor.BODY.value,

)