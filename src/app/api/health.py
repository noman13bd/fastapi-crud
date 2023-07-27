""" health api """
from fastapi import APIRouter, Response
from starlette import status

router = APIRouter()


@router.get("/health",
            status_code=status.HTTP_204_NO_CONTENT,
            response_class=Response
            )
async def health_api():
    """ health check api """
    return Response(status_code=status.HTTP_204_NO_CONTENT)