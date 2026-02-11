from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional


app = FastAPI(
    title="Libra - Job Scraping API",
    version="1.0",
    description=(
        "Libra is a FastAPI-powered job scraping API by Austin Dwomoh. "
        "It provides read-only access to scraped job listings with filtering "
        "options for company, sponsorship, and keyword search. "
        "Use /docs for interactive Swagger UI or /redoc for ReDoc documentation."
    )
)


# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    """API home endpoint with documentation"""
    
    return {
        "api": {
            "name": "Libra",
            "version": "1.0",
            "description": "Libra - Job Scraping API powered by FastAPI",
            "author": "Austin Dwomoh",
            "base_url": "/"
        },
        "endpoints": {
            "GET /": "API documentation and metadata",
            "GET /jobs": "Retrieve jobs with optional query parameters: limit(?limit=10)",
            "GET /jobs/company/{company_name}": "Get jobs by company name with optional limit",
            "GET /jobs/search/{keyword}": "Search jobs by keyword in title or company",
            "GET /jobs/sponsor": "Get all jobs with likely sponsorship"
        },
        "notes": [
            "All data is read-only and updated by background scrapers.",
            "Query parameters are case-insensitive where applicable.",
            "Use /docs for interactive Swagger UI and /redoc for ReDoc documentation."
        ]
    }

# Error handling in FastAPI is via exceptions
@app.exception_handler(404)
def not_found(request, exc):
    return JSONResponse(
        status_code=404,
        content={"success": False, "detail": "Endpoint not found"}
    )

@app.exception_handler(500)
def internal_error(request, exc):
    return JSONResponse(
        status_code=500,
        content={"success": False, "detail": "Internal server error"}
    )

#uvicorn main:app --host 0.0.0.0 --port 5000 --reload