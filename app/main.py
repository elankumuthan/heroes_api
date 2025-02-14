from fastapi import FastAPI, Depends, HTTPException, Query, UploadFile, File
from fastapi.responses import FileResponse
from sqlmodel import Session, select
from app.database import create_db_and_tables, get_session, engine
from app.models import Hero
from typing import Annotated, Optional
import os

# Define dependency for session
SessionDep = Annotated[Session, Depends(get_session)]

# Create FastAPI app
app = FastAPI()

# Run database setup on startup
@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# Create a new hero
@app.post("/hero/", status_code=201)
def create_hero(hero: Hero, session: SessionDep):
    if not hero.name:
        raise HTTPException(status_code=400, detail="Hero name is required")
    if not hero.id:
        raise HTTPException(status_code=400, detail="Hero ID is required")
    if hero.id in {hero.id for hero in session.exec(select(Hero))}:
        raise HTTPException(status_code=400, detail="Hero ID already exists")

    session.add(hero)
    session.commit()
    session.refresh(hero)  

    return hero

# Read all heroes
@app.get("/heroes/")
def read_heroes(
    session: SessionDep,
    sortBy: Optional[str] = None,
    count: Optional[int] = Query(None, alias="count")
) -> list[Hero]:
    query = select(Hero)

    if sortBy in {"name", "age", "id", "gender"}:
        query = query.order_by(getattr(Hero, sortBy))
    
    heroes = session.exec(query).all()

    if count and count < len(heroes):
        heroes = heroes[:count]

    return heroes

# Read a specific hero by ID
@app.get("/heroes/{hero_id}")
def read_hero(hero_id: int, session: SessionDep) -> Hero:
    hero = session.get(Hero, hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    return hero

# Delete a hero by ID
@app.delete("/heroes/{hero_id}")
def delete_hero(hero_id: int, session: SessionDep):
    hero = session.get(Hero, hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    session.delete(hero)
    session.commit()
    return {"ok": True}

# Update hero by id
@app.put("/heroes/{hero_id}", response_model=Hero)
def update_hero(hero_id: int, hero_update: Hero, session: SessionDep):
    hero = session.get(Hero, hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")


    hero.name = hero_update.name or hero.name
    hero.age = hero_update.age or hero.age
    hero.secret_power = hero_update.secret_power or hero.secret_power
    hero.gender = hero_update.gender or hero.gender
    hero.real_name = hero_update.real_name or hero.real_name

    session.add(hero)
    session.commit()
    session.refresh(hero)

    return hero

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)): 
    upload_dir = "uploads"
    os.makedirs(upload_dir, exist_ok=True)
    file_path = os.path.join(upload_dir, file.filename)
    contents = await file.read()
    with open(file_path, "wb") as f:
            f.write(contents)
            
    return {
            "filename": file.filename,
            "size": len(contents),
            "file_type": file.content_type,
            "path": file_path
        }

@app.get("/image")
def return_image():
    file_path = "app/spiderman.jpg"
    return FileResponse(file_path, media_type="image/png")