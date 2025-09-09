# Local Lumo AI

A self-hosted, privacy-first conversational AI that mimics Lumo.

## Project Structure

```
local-lumo-ai/
├── backend/
│   ├── app/
│   │   ├── main.py       # FastAPI application entry point
│   │   ├── router.py     # API route definitions
│   │   ├── config.py     # Configuration loader
│   │   └── config.yaml   # Application configuration
│   ├── models/           # AI models and data models
│   └── plugins/          # Plugin system for extensibility
├── frontend/             # Web interface (future implementation)
├── requirements.txt      # Python dependencies
└── run_server.py        # Server startup script
```

## Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Start the server:**
   ```bash
   python run_server.py
   ```

3. **Test the API:**
   ```bash
   curl http://localhost:8000/
   curl -X POST http://localhost:8000/api/v1/chat \
     -H "Content-Type: application/json" \
     -d '{"message": "Hello, Local Lumo AI!"}'
   ```

## API Endpoints

- `GET /` - Health check
- `GET /health` - Service health status
- `GET /api/v1/models` - List available AI models
- `POST /api/v1/chat` - Send chat message
- `GET /api/v1/conversations` - List conversations
- `DELETE /api/v1/conversations/{id}` - Delete conversation
- `GET /api/v1/system/status` - System status and metrics

## Configuration

The application configuration is managed through `backend/app/config.yaml`. Key settings include:

- **Server**: Host, port, and worker configuration
- **CORS**: Cross-origin resource sharing settings
- **Models**: AI model configuration
- **Privacy**: Data storage and encryption settings
- **Plugins**: Plugin system configuration

## Development

The project uses FastAPI for the backend API with the following features:

- **Privacy-first**: Local processing, no external API calls
- **Extensible**: Plugin system for adding new capabilities
- **Configurable**: YAML-based configuration management
- **RESTful API**: Standard HTTP endpoints for integration
- **Self-hosted**: Complete control over your conversational AI

## Future Enhancements

- Frontend web interface
- Multiple AI model support
- User authentication and sessions
- Conversation persistence
- Plugin marketplace
- Docker containerization
