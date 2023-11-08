from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class DogType(str, Enum):
    terrier = "terrier"
    bulldog = "bulldog"
    dalmatian = "dalmatian"


class Dog(BaseModel):
    name: str
    pk: int
    kind: DogType


class Timestamp(BaseModel):
    id: int
    timestamp: int


dogs_db = {
    0: Dog(name='Bob', pk=0, kind='terrier'),
    1: Dog(name='Marli', pk=1, kind="bulldog"),
    2: Dog(name='Snoopy', pk=2, kind='dalmatian'),
    3: Dog(name='Rex', pk=3, kind='dalmatian'),
    4: Dog(name='Pongo', pk=4, kind='dalmatian'),
    5: Dog(name='Tillman', pk=5, kind='bulldog'),
    6: Dog(name='Uga', pk=6, kind='bulldog')
}

post_db = [
    Timestamp(id=0, timestamp=12),
    Timestamp(id=1, timestamp=10)
]


@app.get('/')
def root():
    return "Hi!"

@app.post('/post')
def post():
    return "Hi"

@app.get('/add')
def new_dog(name:str, pk:int, kind:str):
    num = len(dogs_db)
    dogs_db[num] = Dog(name = name, pk = pk, kind = kind)
    
@app.get('/takedogs')
def take_dogs():
    dogs = []
    for i in dogs_db:
        dogs.append(dogs_db[i].name)
    return dogs

@app.post('/takedogsid/{id}')
def take_dog_id(id:int):
    return dogs_db[id]
         
@app.get('/takedogstype/{ty}')
def take_dog_type(ty:str):
    dogs = []
    for i in dogs_db:
        if dogs_db[i].kind == ty:
            dogs.append(dogs_db[i].name)
    return dogs

@app.get('/takedogstype/{ty}')
         