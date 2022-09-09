from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core import oauth
from schemas.gigs import PremiumBase, PremiumRes

from db.database import get_db
from api.repo.repo_premium import create_new_premium, list_AllPremium, \
    retrieve_PremiumId, delete_PremiumId, update_PremiumId


router = APIRouter()


@router.post("/create-premiumprice")
def create_PremiumPrice(premium: PremiumBase, db: Session = Depends(get_db), current_user=Depends(oauth.get_current_user)):
    price = create_new_premium(premium, db)
    return price


@router.get("/get-all-premiumprice")
def all_premiumprice(db: Session = Depends(get_db)):
    price = list_AllPremium(db)
    return price


@router.get("/standardprice/{id}")
def premiumId(id: int, db: Session = Depends(get_db), current_user=Depends(oauth.get_current_user)):
    price = retrieve_PremiumId(id, db)
    return price


@router.put("/premiumprice/{id}")
def updateId(id: int, premium: PremiumBase, db: Session = Depends(get_db), current_user=Depends(oauth.get_current_user)):
    price = update_PremiumId(id, premium, db)
    return {"Details": "Successfully update the details with the id {id}"}


@router.delete("/premiumprice/{id}")
def delete_Id(id: int, db: Session = Depends(get_db), current_user=Depends(oauth.get_current_user)):
    price = delete_PremiumId(id, db)
    return {"details": f"Suceessfully deleted"}

