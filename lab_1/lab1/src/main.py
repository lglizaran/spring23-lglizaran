from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
async def read_main():
    raise HTTPException(status_code=501)

@app.get("/hello")
async def read_name(name: str | None = None):
    if not name:
        raise HTTPException(status_code=400, detail="Name must be specified, please type /hello?name={name}")
    return {"message": f"Hello {name}"}

# health check to ensure app is up
@app.get('/healthcheck')
def perform_healthcheck():
    return {'healthcheck': 'Everything OK!'}