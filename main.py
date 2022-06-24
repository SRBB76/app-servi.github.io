from typing import Union

from fastapi import Depends, FastAPI, HTTPException

from sqlalchemy.orm import Session
import crud, models, schema
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/registro", response_model=schema.User)
def registro(user: schema.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@app.get("/iniciar_sesion")
def iniciar_sesion():
    return {"has iniciado sesion"}

@app.get("/registro_servicio")
def registro_servicio():
    return {"servicio registrado"}

@app.get("/consultar_servicio")
def consultar_servicio():
    return {"consulta de servicio"}


#@app.get("/items/{item_id}")
#def read_item(item_id: int, q: Union[str, None] = None):
 #   return {"item_id": item_id, "q": q}
 #estuve revisando y para mostrar los ejemplos de python mas facil
