"""
FastAPI backend for TruthLens with voice assistant integration
"""

import os
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn

# Import the voice WebSocket handler
from voice_websocket import handle_voice_websocket

# Create FastAPI app
app = FastAPI(
    title="TruthLens API",
    description="Backend API for TruthLens with voice assistant capabilities",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check endpoint
@app.get("/api/v1/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "truthlens-api",
        "voice_assistant": "enabled" if os.getenv("ELEVENLABS_API_KEY") else "disabled"
    }

# Voice WebSocket endpoint
@app.websocket("/ws/voice")
async def voice_websocket_endpoint(websocket: WebSocket):
    """WebSocket endpoint for voice assistant"""
    await handle_voice_websocket(websocket)

# Existing analysis endpoint (placeholder - integrate with your existing backend)
@app.post("/api/v1/analyze")
async def analyze_text(request: dict):
    """Text analysis endpoint - integrate with your existing analysis logic"""
    # This should integrate with your existing analysis backend
    return JSONResponse({
        "factual_accuracy": 75,
        "bias": "neutral",
        "emotional_tone": "balanced",
        "recommendation": "Cross-reference with additional sources"
    })

# Chat endpoint (placeholder - integrate with your existing chat backend)
@app.post("/api/v1/chat")
async def chat_endpoint(request: dict):
    """Chat endpoint - integrate with your existing chat logic"""
    # This should integrate with your existing chat backend
    return JSONResponse({
        "response": "This is a placeholder response. Please integrate with your existing chat backend."
    })

if __name__ == "__main__":
    # Run the server
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )