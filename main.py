from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
  return {"thing": "welcome to the new wold!"}