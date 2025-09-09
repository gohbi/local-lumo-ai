#!/usr/bin/env python3
"""
Simple script to run the Local Lumo AI backend server.
"""
import sys
import os

# Add the backend directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

if __name__ == "__main__":
    import uvicorn
    from backend.app.config import load_config
    
    config = load_config()
    server_config = config.get("server", {})
    
    # Use the app import string for reload to work properly
    uvicorn.run(
        "backend.app.main:app",
        host=server_config.get("host", "0.0.0.0"),
        port=server_config.get("port", 8000),
        reload=server_config.get("reload", False)  # Disable reload for testing
    )