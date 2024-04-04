import reflex as rx
from enum import Enum

# Constants
MAX_WIDTH = "560px"

# Sizes
class Size(Enum):
    SMALL = "0.5em",
    MEDIUM = "0.8em",
    DEFAULT= "1em",
    BIG= "2em",
    
class Spacing(Enum):
    ZERO = "0"
    VERY_SMALL = "1"
    SMALL = "3"
    DEFAULT = "4"
    LARGE = "5"
    BIG = "6"
    MEDIUM_BIG = "7"
    VERY_BIG = "9"

# Styles    
    
# Styles

BASE_STYLES = {
    rx.button: {
        "width": "100%",
        "height": "100%",
        "display": "block",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
    },
    rx.link : {
        "text_decoration":"none",
        "_hover": {}
    }
}   
title_style = dict(
    width = "100%",
    padding_top = Size.DEFAULT.value
)
    
button_tittle_style = dict(
    font_size = Size.DEFAULT.value
)    

button_body_style = dict(
    font_size = Size.MEDIUM.value
)    