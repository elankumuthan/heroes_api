from fastapi import FastAPI, Depends, HTTPException, Query, Header
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

ADMIN_TOKEN = os.getenv("ADMIN_TOKEN")

# Read a specific hero by ID
@app.get("/heroes/{hero_id}")
def read_hero(hero_id: int, session: SessionDep) -> Hero:
    hero = session.get(Hero, hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    return hero

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

@app.delete("/heroes/delete_all")
def delete_all(session: SessionDep, authorization: str = Header(None)):
    if not ADMIN_TOKEN:
        raise HTTPException(status_code=500, detail="Admin token not set on the server")

    if authorization != f"Bearer {ADMIN_TOKEN}":
        raise HTTPException(status_code=403, detail="Unauthorized")

    heroes = session.exec(select(Hero)).all()

    if not heroes:
        return {"message": "No heroes in the database to delete"}

    deleted_ids = [hero.id for hero in heroes]

    for hero in heroes:
        session.delete(hero)

    session.commit()
    return {"message": f"Deleted heroes with IDs {deleted_ids}"}

# Make sure this route comes **after** /heroes/delete_all
@app.delete("/heroes/{hero_id}")
def delete_hero(hero_id: int, session: SessionDep, authorization: str = Header(None)):
    if not ADMIN_TOKEN:
        raise HTTPException(status_code=500, detail="Admin token not set on the server")

    if authorization != f"Bearer {ADMIN_TOKEN}":
        raise HTTPException(status_code=403, detail="Unauthorized")

    hero = session.get(Hero, hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")

    session.delete(hero)
    session.commit()
    return {"message": f"Hero with ID {hero_id} deleted"}


@app.post("/heroes/reset_all")
def reset_all(session: SessionDep, authorization: str = Header(None)):
    if not ADMIN_TOKEN:
        raise HTTPException(status_code=500, detail="Admin token not set on the server")
    if authorization != f"Bearer {ADMIN_TOKEN}":
        raise HTTPException(status_code=403, detail="Unauthorized")

    # Predefined superheroes
    heroes = [
        Hero(id=1, name="Superman", age=35, secret_power="Flight", gender="Male", real_name="Clark Kent"),
        Hero(id=2, name="Batman", age=40, secret_power="Genius", gender="Male", real_name="Bruce Wayne"),
        Hero(id=3, name="Wonder Woman", age=5000, secret_power="Super Strength", gender="Female", real_name="Diana Prince"),
        Hero(id=4, name="Iron Man", age=45, secret_power="Advanced Armor", gender="Male", real_name="Tony Stark"),
        Hero(id=5, name="Spider-Man", age=18, secret_power="Wall Climbing", gender="Male", real_name="Peter Parker"),
    ]

    # Check if heroes already exist
    existing_heroes = session.exec(select(Hero)).all()
    if existing_heroes:
        return {"message": "Heroes already exist in the database"}

    # Insert heroes into the database
    session.add_all(heroes)
    session.commit()

    return {"message": "Default heroes added successfully", "added_heroes": [hero.id for hero in heroes]}
