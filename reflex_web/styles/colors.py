from enum import Enum

class Color(Enum):
    PRIMARY = "#D92938"
    SECONDARY = "#087ec4"
    BACKGROUND = "#0c151D" 
    CONTENT = "#171F26"
    GRADIENT = "conic-gradient(from 0deg at 50% 50%, #D92938 0.75%, #8C0839 88.52%)"
    
class TextColor(Enum):
    HEADER = "#F1F2F4"
    BODY = "#C3C7C8"
    FOOTER = "#A3ABB2"