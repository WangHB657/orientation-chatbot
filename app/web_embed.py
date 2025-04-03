# web_embed.py
from web_embedding_utils import build_web_embedding

SCHOOL_WEBSITES = [
    "https://www.jcu.edu.sg/courses-and-study/orientation/before-orientation",
    "https://www.jcu.edu.sg/courses-and-study/orientation/during-orientation",
    "https://www.jcu.edu.sg/courses-and-study/orientation/after-orientation",
    "https://www.jcu.edu.sg/events",
    "https://www.jcu.edu.sg/current-students/campus-maps-And-information",
    "https://www.jcu.edu.sg/current-students/accommodation/accommodation-faqs",
    "https://www.jcu.edu.sg/current-students/facilities",
    "https://www.jcu.edu.sg/current-students/calendars-and-timetables"
]

build_web_embedding(SCHOOL_WEBSITES)
