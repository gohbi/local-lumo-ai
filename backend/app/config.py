"""
Configuration loader for local-lumo-ai application.
"""
import yaml
import os
from pathlib import Path

def load_config(config_path: str = None) -> dict:
    """
    Load configuration from YAML file.
    
    Args:
        config_path: Path to configuration file. If None, uses default path.
    
    Returns:
        Dictionary containing configuration settings.
    """
    if config_path is None:
        # Default path relative to this file
        config_path = Path(__file__).parent / "config.yaml"
    
    try:
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
        return config
    except FileNotFoundError:
        # Return default configuration if file not found
        return get_default_config()
    except yaml.YAMLError as e:
        print(f"Error parsing config file: {e}")
        return get_default_config()

def get_default_config() -> dict:
    """
    Get default configuration when config file is not available.
    
    Returns:
        Dictionary containing default configuration settings.
    """
    return {
        "server": {
            "host": "0.0.0.0",
            "port": 8000,
            "reload": True,
            "workers": 1
        },
        "cors": {
            "origins": [
                "http://localhost:3000",
                "http://127.0.0.1:3000",
                "http://localhost:8080"
            ]
        },
        "models": {
            "default": {
                "name": "Default Model",
                "type": "echo",
                "enabled": True,
                "max_tokens": 2048,
                "temperature": 0.7
            }
        },
        "logging": {
            "level": "INFO"
        },
        "privacy": {
            "store_conversations": True,
            "encrypt_data": False,
            "retention_days": 30
        }
    }