from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles


def create_application():
    application = FastAPI()

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
