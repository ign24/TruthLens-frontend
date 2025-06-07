"""
Voice WebSocket handler for TruthLens
Integrates with ElevenLabs for real-time voice AI conversations
"""

import asyncio
import json
import logging
import os
import base64
import websockets
from typing import Optional, Dict, Any
import aiohttp
from fastapi import WebSocket, WebSocketDisconnect
from fastapi.websockets import WebSocketState

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class VoiceAssistantManager:
    """Manages voice assistant connections and ElevenLabs integration"""
    
    def __init__(self):
        self.elevenlabs_api_key = os.getenv("ELEVENLABS_API_KEY")
        self.elevenlabs_agent_id = os.getenv("ELEVENLABS_AGENT_ID")
        self.elevenlabs_base_url = "https://api.elevenlabs.io/v1"
        self.model_id = "flash_v2.5"  # Low-latency model
        
        # System prompt for the voice assistant
        self.system_prompt = """You are Alex, the voice assistant for TruthLens. 
        Speak in short, friendly, helpful sentences. 
        Respond in Spanish if the user speaks Spanish, otherwise respond in English. 
        Ask for clarification if something is unclear.
        Keep responses under 50 words for natural conversation flow.
        You help users understand news analysis, bias detection, and fact-checking."""
        
        if not self.elevenlabs_api_key:
            logger.warning("ELEVENLABS_API_KEY not found in environment variables")
        if not self.elevenlabs_agent_id:
            logger.warning("ELEVENLABS_AGENT_ID not found in environment variables")
    
    async def handle_websocket_connection(self, websocket: WebSocket):
        """Handle a new WebSocket connection for voice chat"""
        await websocket.accept()
        logger.info("Voice WebSocket connection established")
        
        try:
            # Send connection confirmation
            await websocket.send_text(json.dumps({
                "type": "status",
                "message": "Voice assistant connected and ready"
            }))
            
            # Main message loop
            while True:
                try:
                    # Receive message from client
                    data = await websocket.receive_text()
                    message = json.loads(data)
                    
                    if message.get("type") == "audio_input":
                        await self._process_audio_input(websocket, message)
                    elif message.get("type") == "ping":
                        await websocket.send_text(json.dumps({"type": "pong"}))
                    else:
                        logger.warning(f"Unknown message type: {message.get('type')}")
                        
                except json.JSONDecodeError:
                    logger.error("Invalid JSON received from client")
                    await websocket.send_text(json.dumps({
                        "type": "error",
                        "message": "Invalid message format"
                    }))
                except Exception as e:
                    logger.error(f"Error processing message: {e}")
                    await websocket.send_text(json.dumps({
                        "type": "error",
                        "message": "Error processing your request"
                    }))
                    
        except WebSocketDisconnect:
            logger.info("Voice WebSocket client disconnected")
        except Exception as e:
            logger.error(f"WebSocket error: {e}")
        finally:
            if websocket.client_state != WebSocketState.DISCONNECTED:
                await websocket.close()
    
    async def _process_audio_input(self, websocket: WebSocket, message: Dict[str, Any]):
        """Process audio input from the client"""
        try:
            audio_data = message.get("audio")
            audio_format = message.get("format", "webm")
            
            if not audio_data:
                await websocket.send_text(json.dumps({
                    "type": "error",
                    "message": "No audio data received"
                }))
                return
            
            # Send status update
            await websocket.send_text(json.dumps({
                "type": "status",
                "message": "Processing your voice..."
            }))
            
            # Process with ElevenLabs
            response_audio = await self._process_with_elevenlabs(audio_data, audio_format)
            
            if response_audio:
                # Send audio response back to client
                await websocket.send_text(json.dumps({
                    "type": "audio_response",
                    "audio": response_audio
                }))
            else:
                await websocket.send_text(json.dumps({
                    "type": "error",
                    "message": "Failed to generate voice response"
                }))
                
        except Exception as e:
            logger.error(f"Error processing audio input: {e}")
            await websocket.send_text(json.dumps({
                "type": "error",
                "message": "Error processing your voice input"
            }))
    
    async def _process_with_elevenlabs(self, audio_data: str, audio_format: str) -> Optional[str]:
        """Process audio with ElevenLabs and return response audio"""
        try:
            if not self.elevenlabs_api_key or not self.elevenlabs_agent_id:
                logger.error("ElevenLabs credentials not configured")
                return None
            
            # Decode base64 audio
            audio_bytes = base64.b64decode(audio_data)
            
            # Use ElevenLabs Conversational AI endpoint
            url = f"{self.elevenlabs_base_url}/convai/conversation"
            
            headers = {
                "xi-api-key": self.elevenlabs_api_key,
                "Content-Type": "application/json"
            }
            
            # Prepare the request payload
            payload = {
                "agent_id": self.elevenlabs_agent_id,
                "audio": audio_data,
                "audio_format": audio_format,
                "model_id": self.model_id,
                "voice_settings": {
                    "stability": 0.5,
                    "similarity_boost": 0.8,
                    "style": 0.3,
                    "use_speaker_boost": True
                },
                "generation_config": {
                    "chunk_length_schedule": [120, 160, 250, 290]
                }
            }
            
            async with aiohttp.ClientSession() as session:
                async with session.post(url, headers=headers, json=payload) as response:
                    if response.status == 200:
                        response_data = await response.json()
                        
                        # Extract audio from response
                        if "audio" in response_data:
                            return response_data["audio"]
                        else:
                            logger.error("No audio in ElevenLabs response")
                            return None
                    else:
                        error_text = await response.text()
                        logger.error(f"ElevenLabs API error {response.status}: {error_text}")
                        return None
                        
        except Exception as e:
            logger.error(f"Error calling ElevenLabs API: {e}")
            return None
    
    async def _fallback_text_to_speech(self, text: str) -> Optional[str]:
        """Fallback text-to-speech using ElevenLabs TTS endpoint"""
        try:
            if not self.elevenlabs_api_key:
                return None
            
            # Use a default voice if agent_id is not available
            voice_id = self.elevenlabs_agent_id or "21m00Tcm4TlvDq8ikWAM"  # Default voice
            
            url = f"{self.elevenlabs_base_url}/text-to-speech/{voice_id}"
            
            headers = {
                "Accept": "audio/mpeg",
                "Content-Type": "application/json",
                "xi-api-key": self.elevenlabs_api_key
            }
            
            payload = {
                "text": text,
                "model_id": "eleven_multilingual_v2",
                "voice_settings": {
                    "stability": 0.5,
                    "similarity_boost": 0.8,
                    "style": 0.3,
                    "use_speaker_boost": True
                }
            }
            
            async with aiohttp.ClientSession() as session:
                async with session.post(url, headers=headers, json=payload) as response:
                    if response.status == 200:
                        audio_bytes = await response.read()
                        return base64.b64encode(audio_bytes).decode('utf-8')
                    else:
                        error_text = await response.text()
                        logger.error(f"ElevenLabs TTS error {response.status}: {error_text}")
                        return None
                        
        except Exception as e:
            logger.error(f"Error in fallback TTS: {e}")
            return None

# Global instance
voice_manager = VoiceAssistantManager()

async def handle_voice_websocket(websocket: WebSocket):
    """FastAPI WebSocket endpoint handler"""
    await voice_manager.handle_websocket_connection(websocket)