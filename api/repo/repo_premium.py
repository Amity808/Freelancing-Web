from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from schemas.gigs import PremiumBase, PremiumRes
from models.gigs import Premiumpackage


def create_new_premium(premium: PremiumBase, db: Session):
    price = Premiumpackage(**premium.dict())
    db.add(price)
    db.commit()
    db.refresh(price)
    return price


def list_AllPremium(db: Session):
    price = db.query(Premiumpackage).all()
    return price


def retrieve_PremiumId(id: int, db: Session):
    price = db.query(Premiumpackage).filter(Premiumpackage.id == id).first()
    if not price:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"The price package with the id {id} not found")
    return price


def update_PremiumId(id: int, premium: PremiumBase, db: Session):
    existing_price = db.query(Premiumpackage).filter(Premiumpackage.id == id)
    if not existing_price:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"The details with the id {id} does not exist")
    premium.__dict__.update(id=id)
    existing_price.update(premium.__dict__)
    db.commit()
    return existing_price


def delete_PremiumId(id: int, db: Session):
    existing_price = db.query(Premiumpackage).filter(Premiumpackage.id == id)
    if not existing_price.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"The details with the id {id} does not exist")
    existing_price.delete(synchronize_session=False)
    db.commit()
    return {"details": f"Sucessfully Deleted {existing_price}"}
