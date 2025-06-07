# TruthLens Voice Assistant Backend

This backend provides WebSocket-based voice assistant functionality using ElevenLabs for real-time voice conversations.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure environment variables:
```bash
cp .env.example .env
# Edit .env with your ElevenLabs credentials
```

3. Run the server:
```bash
python main.py
```

## Environment Variables

- `ELEVENLABS_API_KEY`: Your ElevenLabs API key
- `ELEVENLABS_AGENT_ID`: Your ElevenLabs agent ID (optional, will use default voice)

## API Endpoints

- `GET /api/v1/health`: Health check
- `WS /ws/voice`: Voice assistant WebSocket
- `POST /api/v1/analyze`: Text analysis (integrate with existing backend)
- `POST /api/v1/chat`: Chat endpoint (integrate with existing backend)

## WebSocket Protocol

### Client to Server:
```json
{
  "type": "audio_input",
  "audio": "base64_encoded_audio",
  "format": "webm"
}
```

### Server to Client:
```json
{
  "type": "audio_response",
  "audio": "base64_encoded_audio"
}
```

## Integration Notes

- The voice assistant uses ElevenLabs Conversational AI for speech-to-text, LLM processing, and text-to-speech
- Audio is processed in real-time with low latency using the `flash_v2.5` model
- The system prompt configures the assistant as "Alex" for TruthLens
- Fallback TTS is available if the conversational AI endpoint fails