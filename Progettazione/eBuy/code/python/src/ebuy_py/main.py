from fastapi import FastAPI

app = FastAPI(title="eBuy API")

@app.get("/")
def home():
  return {"test": "ok", "health": "/health", "OpenAPI" : "/docs"}

@app.get("/health")
def health():
    return {"status": "ok"}

def main() -> int:
    """Entry point della console UI (script `ebuy`)."""
    print("eBuy - console UI (in sviluppo)")
    return 0
