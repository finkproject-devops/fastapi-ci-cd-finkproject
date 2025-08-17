from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
  return {"message": "Worwelcome to the new woldd!"}