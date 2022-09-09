from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from schemas.gigs import BasicBase, BasicRes, PremiumBase, PremiumRes, StandardBase, StandardRes
from models.gigs import Basicpackage, Standardpackage, Premiumpackage


def create_new_basic(basic: BasicBase, db: Session):
    price = Basicpackage(**basic.dict())
    db.add(price)
    db.commit()
    db.refresh(price)
    return price


def list_AllBasic(db: Session):
    price = db.query(Basicpackage).all()
    return price


def retrieve_GigId(id: int, db: Session):
    price = db.query(Basicpackage).filter(Basicpackage.id == id).first()
    if not price:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"The price package with the id {id} not found")
    return price


def update_basicId(id: int, basic: BasicBase, db: Session):
    existing_price = db.query(Basicpackage).filter(Basicpackage.id == id)
    if not existing_price:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"The details with the id {id} does not exist")
    basic.__dict__.update(id=id)
    existing_price.update(basic.__dict__)
    db.commit()
    return existing_price


def delete_basicId(id: int, db: Session):
    existing_price = db.query(Basicpackage).filter(Basicpackage.id == id)
    if not existing_price.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"The details with the id {id} does not exist")
    existing_price.delete(synchronize_session=False)
    db.commit()
    return {"details": f"Sucessfully Deleted {existing_price}"}
