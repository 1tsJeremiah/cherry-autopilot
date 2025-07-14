from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Cherry Autopilot Agent API Alive"}
