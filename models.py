
from typing import Optional

from pydantic import BaseModel


class Repo(BaseModel):
    name: str
    url: Optional[str]



class Release(BaseModel):
    name: str
    chart_name: Optional[str]