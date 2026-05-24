from pydantic import BaseModel, HttpUrl
from typing import Optional
from datetime import datetime


class SlideShareItem(BaseModel):

    title: str

    url: HttpUrl

    author: Optional[str] = None

    description: Optional[str] = None

    views: Optional[int] = None

    upload_date: Optional[str] = None

    page: int

    extracted_at: datetime