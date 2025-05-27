from pydantic import BaseModel, Field
from typing import Annotated


class CreateMeetingResponse(BaseModel):
    url_code: Annotated[str, Field(description="고유한 미팅 URL 코드 입니다.")]
