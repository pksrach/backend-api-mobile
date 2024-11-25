from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi


def custom_openapi(app: FastAPI):
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="E-Furniture API",
        version="0.1.0",
        description="API documentation for E-Furniture platform, providing access to backend and frontend operations for managing products, users, and more.",
        routes=app.routes,
    )
    openapi_schema["tags"] = [
        {
            "name": "Category API",
            "description": "Endpoints for managing categories in the backend.",
        },
        {
            "name": "Product API",
            "description": "Endpoints for managing products in the backend.",
        },
        {
            "name": "Media Storage API",
            "description": "Endpoints for managing media Storages in the backend.",
        },
        # Default tag
        {
            "name": "Default",
            "description": "Default operations provided by the system.",
        },
    ]

    openapi_schema["info"]["contact"] = {
        "name": "SETEC Institute",
        "url": "https://www.setecu.com",
    }
    openapi_schema["externalDocs"] = {
        "description": "Additional information can be found here.",
        "url": "https://fastapi.tiangolo.com",
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema
