import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.routes.product_router import product_router
from app.routes.category_router import category_router
from app.routes.media_storage_router import media_router


def create_application():
    application = FastAPI()
    if not os.path.exists("uploads"):
        os.makedirs("uploads")
    # Serve the 'uploads' directory as static files
    application.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

    application.include_router(product_router)
    application.include_router(category_router)
    application.include_router(media_router)

    return application


class MainApp:
    def __init__(self):
        self.app = create_application()
        self.configure_cors()
        self.add_routes()

    def configure_cors(self):
        origins = [
            "http://localhost:3000",
        ]

        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=origins,  # Allows requests from these origins
            allow_credentials=True,  # Allows cookies to be sent in cross-origin requests
            allow_methods=["*"],  # Allows all HTTP methods
            allow_headers=["*"],  # Allows all headers to be sent in requests
        )

    def add_routes(self):
        @self.app.get("/", include_in_schema=False)
        async def root():
            return {"message": "ok"}


main_app = MainApp()
app = main_app.app
