from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.database import get_db
from backend.tools.order_tools import check_order_status


router = APIRouter()


@router.get("/orders/{order_id}")
def get_order(
    order_id: str,
    db: Session = Depends(get_db)
):
    result = check_order_status(
        order_id=order_id,
        db=db
    )

    if not result["success"]:
        raise HTTPException(
            status_code=404,
            detail=result["message"]
        )

    return result