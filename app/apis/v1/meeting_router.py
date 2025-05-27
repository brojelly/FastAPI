from fastapi import APIRouter

from app.dtos.create_meeting_response import CreateMeetingResponse

router = APIRouter(prefix="/v1/meetings", tags=["Meeting"])


@router.post("", description="미팅 생성 dummy API 입니다.")
async def create_meeting() -> CreateMeetingResponse:
    return CreateMeetingResponse(url_code="abc123")
