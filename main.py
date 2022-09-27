from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    nim: int

data_mahasiswa = {
    1: {
        "Nama": "Tes",
        "NIM": 18220200
    }
}

@app.get("/get-by-nim")
def get_mahasiswa(nim: int):
    for item_id in data_mahasiswa:
        if data_mahasiswa[item_id]["NIM"] == nim:
            return data_mahasiswa[item_id]
    return {"Data": "Not Found"}

@app.post("/add-mahasiswa/{item_id}")
def add_mahasiswa(item_id: int, item: Item):
    if item_id in data_mahasiswa:
        return {"Error": "Data Mahasiswa sudah ada"}

    data_mahasiswa[item_id] = {"nama": item.name, "NIM":item.nim}
    return data_mahasiswa[item_id]