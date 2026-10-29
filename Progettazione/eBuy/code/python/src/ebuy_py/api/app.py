from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

# from python_code.api.routers import utenti, post


def create_app() -> FastAPI:
    app = FastAPI(title="eBuy API", version="0.1.0")

    # Frontend Vite in sviluppo
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:5173"],
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.get("/", include_in_schema=False)
    def home():
        return RedirectResponse("/docs")

    @app.get("/health", tags=["system"])
    def health():
        return {"status": "ok"}

    # app.include_router(utenti.router, prefix="/utenti", tags=["utenti"])
    # app.include_router(post.router, prefix="/post", tags=["post"])

    return app


app = create_app()