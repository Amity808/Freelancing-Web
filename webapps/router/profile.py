from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from db.database import get_db
from models.gigs import Profile
from models.users import Users

router = APIRouter(include_in_schema=False)

templates = Jinja2Templates(directory="templates")


@router.get("/profile/{id}")
def profile_detail(request: Request, id: int, db: Session = Depends(get_db)):
    profile = db.query(Profile).filter(Profile.id == id).first()
    return templates.TemplateResponse(
        "profile_details.html", {"request": request, "profile": profile}
    )


@router.get("/profilecreate")
def create_gig(request: Request):
    return templates.TemplateResponse("profile_reg.html", {"request": request})


@router.post("/profilecreate")
async def create_gig(request: Request):
    form = await request.form()
    surname = form.get("surname")
    firstName = form.get("firstName")
    lastName = form.get("lastName")
    phone_no = form.get("phone_no")
    profileDescription = form.get("profileDescription")
    school = form.get("school")
    courseStudy = form.get("courseStudy")
    certificate = form.get("certificate")
    certificateBy = form.get("certificateBy")
    websiteUrl = form.get("websiteUrl")
    statusM = form.get("statusM")

    return templates.TemplateResponse("profile_reg.html", {"request": request})
