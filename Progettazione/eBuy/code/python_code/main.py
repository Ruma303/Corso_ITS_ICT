import sys

from fastapi import FastAPI

app = FastAPI(title="eBuy API")

@app.get("/")
def home():
  return {"test": "ok", "health": "/health", "OpenAPI" : "/docs"}

@app.get("/health")
def health():
    return {"status": "ok"}

def main():
  home()
  return 0

if __name__ == "__main__":
  sys.exit(main())