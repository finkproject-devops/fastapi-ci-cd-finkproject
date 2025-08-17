from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Writer": "see you in the next chapter! , Nxt-chapter"}
