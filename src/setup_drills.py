"""pydatnic drill scutrure with coalories, time take effort, image of cone laout and text desciption$ and title"""

import pydantic


class ConeLayoutDrawer(pydantic.BaseModel):
    cone_positions: list[tuple[int, int]]
    calories: int
    time_taken: int
    effort: str
    filename: str

    class Config:
        arbitrary_types_allowed = True