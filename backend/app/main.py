"""
Main entry point for the local-lumo-ai backend application.
A self-hosted, privacy-first conversational AI that mimics Lumo.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from .router import api_router
from .config import load_config

app = FastAPI(
    title="Local Lumo AI",
    description="A self-hosted, privacy-first conversational AI",
    version="1.0.0"
)

# Load configuration
config = load_config()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=config.get("cors", {}).get("origins", ["http://localhost:3000"]),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
async def root():
    """Health check endpoint."""
    return {"message": "Local Lumo AI is running", "version": "1.0.0"}

@app.get("/health")
async def health_check():
    """Health check endpoint for monitoring."""
    return {"status": "healthy", "service": "local-lumo-ai"}

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=config.get("server", {}).get("host", "0.0.0.0"),
        port=config.get("server", {}).get("port", 8000),
        reload=config.get("server", {}).get("reload", True)
    )