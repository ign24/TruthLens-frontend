<template>
  <div class="voice-assistant-container">
    <!-- Voice Assistant Button -->
    <div class="voice-button-wrapper" :class="{ 'active': isActive, 'listening': isListening, 'speaking': isSpeaking }">
      <!-- Animated Background Disc -->
      <div class="voice-disc">
        <div class="disc-gradient"></div>
        <div class="disc-shine"></div>
        
        <!-- Audio Level Rings (shown when speaking) -->
        <div v-if="isSpeaking" class="audio-rings">
          <div class="audio-ring" v-for="i in 3" :key="i" :style="{ animationDelay: `${i * 0.2}s` }"></div>
        </div>
        
        <!-- Pulse Effect (shown when listening) -->
        <div v-if="isListening" class="pulse-effect"></div>
      </div>
      
      <!-- Main Button -->
      <button
        @click="toggleVoiceChat"
        @mousedown="handleMouseDown"
        @mouseup="handleMouseUp"
        @mouseleave="handleMouseUp"
        :disabled="isConnecting"
        class="voice-button"
        :class="{
          'listening': isListening,
          'speaking': isSpeaking,
          'connecting': isConnecting,
          'error': hasError
        }"
        :aria-label="getButtonLabel()"
      >
        <!-- Icon Container -->
        <div class="button-icon">
          <!-- Microphone Icon (default state) -->
          <svg v-if="!isListening && !isSpeaking && !isConnecting" 
               class="icon-mic" 
               viewBox="0 0 24 24" 
               fill="none" 
               stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 
                  d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"/>
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 
                  d="M19 10v2a7 7 0 0 1-14 0v-2"/>
            <line stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 
                  x1="12" y1="19" x2="12" y2="23"/>
            <line stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 
                  x1="8" y1="23" x2="16" y2="23"/>
          </svg>
          
          <!-- Waveform Icon (listening state) -->
          <div v-else-if="isListening" class="icon-waveform">
            <div class="wave-bar" v-for="i in 5" :key="i" :style="{ animationDelay: `${i * 0.1}s` }"></div>
          </div>
          
          <!-- Speaker Icon (speaking state) -->
          <svg v-else-if="isSpeaking" 
               class="icon-speaker" 
               viewBox="0 0 24 24" 
               fill="none" 
               stroke="currentColor">
            <polygon stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 
                     points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/>
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 
                  d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"/>
          </svg>
          
          <!-- Loading Spinner (connecting state) -->
          <div v-else-if="isConnecting" class="icon-loading">
            <div class="loading-spinner"></div>
          </div>
        </div>
        
        <!-- Button Text -->
        <span class="button-text">{{ getButtonText() }}</span>
      </button>
    </div>
    
    <!-- Status Indicator -->
    <div v-if="statusMessage" class="status-message" :class="{ 'error': hasError }">
      {{ statusMessage }}
    </div>
    
    <!-- Connection Status -->
    <div class="connection-status" :class="connectionStatus">
      <div class="status-dot"></div>
      <span>{{ getConnectionStatusText() }}</span>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted, computed } from 'vue';

// State management
const isActive = ref(false);
const isListening = ref(false);
const isSpeaking = ref(false);
const isConnecting = ref(false);
const hasError = ref(false);
const statusMessage = ref('');
const connectionStatus = ref<'disconnected' | 'connecting' | 'connected' | 'error'>('disconnected');

// WebSocket and audio management
let websocket: WebSocket | null = null;
let mediaRecorder: MediaRecorder | null = null;
let audioStream: MediaStream | null = null;
let audioContext: AudioContext | null = null;
let audioChunks: Blob[] = [];

// Configuration
const WEBSOCKET_URL = `${import.meta.env.VITE_API_BASE_URL?.replace('http', 'ws') || 'ws://localhost:8000'}/ws/voice`;
const SAMPLE_RATE = 16000;

// Computed properties
const getButtonLabel = () => {
  if (isConnecting.value) return 'Connecting to voice assistant';
  if (isListening.value) return 'Listening - Click to stop';
  if (isSpeaking.value) return 'AI is speaking';
  return 'Start voice conversation';
};

const getButtonText = () => {
  if (isConnecting.value) return 'Connecting...';
  if (isListening.value) return 'Listening...';
  if (isSpeaking.value) return 'Speaking...';
  return 'Call AI agent';
};

const getConnectionStatusText = () => {
  switch (connectionStatus.value) {
    case 'connecting': return 'Connecting...';
    case 'connected': return 'Connected';
    case 'error': return 'Connection Error';
    default: return 'Disconnected';
  }
};

// WebSocket management
const connectWebSocket = async (): Promise<boolean> => {
  return new Promise((resolve) => {
    try {
      connectionStatus.value = 'connecting';
      websocket = new WebSocket(WEBSOCKET_URL);
      
      websocket.onopen = () => {
        console.log('Voice WebSocket connected');
        connectionStatus.value = 'connected';
        hasError.value = false;
        statusMessage.value = '';
        resolve(true);
      };
      
      websocket.onmessage = async (event) => {
        try {
          const data = JSON.parse(event.data);
          
          if (data.type === 'audio_response') {
            await playAudioResponse(data.audio);
          } else if (data.type === 'error') {
            handleError(data.message);
          } else if (data.type === 'status') {
            statusMessage.value = data.message;
          }
        } catch (error) {
          console.error('Error processing WebSocket message:', error);
          handleError('Error processing voice response');
        }
      };
      
      websocket.onerror = (error) => {
        console.error('WebSocket error:', error);
        connectionStatus.value = 'error';
        handleError('Connection error. Please try again.');
        resolve(false);
      };
      
      websocket.onclose = () => {
        console.log('Voice WebSocket disconnected');
        connectionStatus.value = 'disconnected';
        websocket = null;
      };
      
      // Timeout for connection
      setTimeout(() => {
        if (connectionStatus.value === 'connecting') {
          handleError('Connection timeout. Please try again.');
          resolve(false);
        }
      }, 10000);
      
    } catch (error) {
      console.error('Error creating WebSocket:', error);
      connectionStatus.value = 'error';
      handleError('Failed to connect to voice service');
      resolve(false);
    }
  });
};

// Audio management
const initializeAudio = async (): Promise<boolean> => {
  try {
    audioStream = await navigator.mediaDevices.getUserMedia({
      audio: {
        sampleRate: SAMPLE_RATE,
        channelCount: 1,
        echoCancellation: true,
        noiseSuppression: true,
        autoGainControl: true
      }
    });
    
    audioContext = new AudioContext({ sampleRate: SAMPLE_RATE });
    
    mediaRecorder = new MediaRecorder(audioStream, {
      mimeType: 'audio/webm;codecs=opus'
    });
    
    mediaRecorder.ondataavailable = (event) => {
      if (event.data.size > 0) {
        audioChunks.push(event.data);
      }
    };
    
    mediaRecorder.onstop = async () => {
      if (audioChunks.length > 0) {
        const audioBlob = new Blob(audioChunks, { type: 'audio/webm;codecs=opus' });
        await sendAudioToServer(audioBlob);
        audioChunks = [];
      }
    };
    
    return true;
  } catch (error) {
    console.error('Error initializing audio:', error);
    handleError('Microphone access denied. Please allow microphone access and try again.');
    return false;
  }
};

const sendAudioToServer = async (audioBlob: Blob) => {
  if (!websocket || websocket.readyState !== WebSocket.OPEN) {
    handleError('Not connected to voice service');
    return;
  }
  
  try {
    const arrayBuffer = await audioBlob.arrayBuffer();
    const base64Audio = btoa(String.fromCharCode(...new Uint8Array(arrayBuffer)));
    
    websocket.send(JSON.stringify({
      type: 'audio_input',
      audio: base64Audio,
      format: 'webm'
    }));
    
    statusMessage.value = 'Processing your message...';
  } catch (error) {
    console.error('Error sending audio:', error);
    handleError('Failed to send audio. Please try again.');
  }
};

const playAudioResponse = async (base64Audio: string) => {
  try {
    isSpeaking.value = true;
    statusMessage.value = 'AI is responding...';
    
    const audioData = atob(base64Audio);
    const audioArray = new Uint8Array(audioData.length);
    for (let i = 0; i < audioData.length; i++) {
      audioArray[i] = audioData.charCodeAt(i);
    }
    
    const audioBlob = new Blob([audioArray], { type: 'audio/mpeg' });
    const audioUrl = URL.createObjectURL(audioBlob);
    const audio = new Audio(audioUrl);
    
    audio.onended = () => {
      isSpeaking.value = false;
      statusMessage.value = '';
      URL.revokeObjectURL(audioUrl);
    };
    
    audio.onerror = () => {
      isSpeaking.value = false;
      handleError('Error playing audio response');
      URL.revokeObjectURL(audioUrl);
    };
    
    await audio.play();
  } catch (error) {
    console.error('Error playing audio response:', error);
    isSpeaking.value = false;
    handleError('Error playing voice response');
  }
};

// Main voice chat toggle
const toggleVoiceChat = async () => {
  if (isListening.value) {
    stopListening();
    return;
  }
  
  if (isSpeaking.value) {
    // Can't interrupt while speaking
    return;
  }
  
  await startVoiceChat();
};

const startVoiceChat = async () => {
  try {
    isConnecting.value = true;
    hasError.value = false;
    statusMessage.value = 'Initializing voice assistant...';
    
    // Connect WebSocket if not connected
    if (!websocket || websocket.readyState !== WebSocket.OPEN) {
      const connected = await connectWebSocket();
      if (!connected) {
        isConnecting.value = false;
        return;
      }
    }
    
    // Initialize audio if not initialized
    if (!audioStream) {
      const audioInitialized = await initializeAudio();
      if (!audioInitialized) {
        isConnecting.value = false;
        return;
      }
    }
    
    isConnecting.value = false;
    startListening();
    
  } catch (error) {
    console.error('Error starting voice chat:', error);
    isConnecting.value = false;
    handleError('Failed to start voice chat. Please try again.');
  }
};

const startListening = () => {
  if (!mediaRecorder) return;
  
  try {
    isListening.value = true;
    isActive.value = true;
    statusMessage.value = 'Listening... Click to stop';
    
    audioChunks = [];
    mediaRecorder.start(1000); // Collect data every second
  } catch (error) {
    console.error('Error starting recording:', error);
    handleError('Failed to start recording');
  }
};

const stopListening = () => {
  if (!mediaRecorder || !isListening.value) return;
  
  try {
    isListening.value = false;
    isActive.value = false;
    statusMessage.value = 'Processing...';
    
    mediaRecorder.stop();
  } catch (error) {
    console.error('Error stopping recording:', error);
    handleError('Error stopping recording');
  }
};

// Error handling
const handleError = (message: string) => {
  hasError.value = true;
  statusMessage.value = message;
  isListening.value = false;
  isSpeaking.value = false;
  isConnecting.value = false;
  isActive.value = false;
  
  // Clear error after 5 seconds
  setTimeout(() => {
    if (hasError.value) {
      hasError.value = false;
      statusMessage.value = '';
    }
  }, 5000);
};

// Button interaction handlers
const handleMouseDown = () => {
  if (!isListening.value && !isSpeaking.value && !isConnecting.value) {
    // Add press effect
  }
};

const handleMouseUp = () => {
  // Remove press effect
};

// Cleanup
const cleanup = () => {
  if (mediaRecorder && mediaRecorder.state !== 'inactive') {
    mediaRecorder.stop();
  }
  
  if (audioStream) {
    audioStream.getTracks().forEach(track => track.stop());
    audioStream = null;
  }
  
  if (audioContext) {
    audioContext.close();
    audioContext = null;
  }
  
  if (websocket) {
    websocket.close();
    websocket = null;
  }
  
  mediaRecorder = null;
  audioChunks = [];
};

// Lifecycle
onMounted(() => {
  // Check for required APIs
  if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
    handleError('Voice features not supported in this browser');
  }
});

onUnmounted(() => {
  cleanup();
});
</script>

<style scoped>
.voice-assistant-container {
  position: fixed;
  bottom: 2rem;
  right: 50%;
  transform: translateX(50%);
  z-index: 50;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
}

.voice-button-wrapper {
  position: relative;
  width: 200px;
  height: 200px;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* Animated Background Disc */
.voice-disc {
  position: absolute;
  inset: 0;
  border-radius: 50%;
  overflow: hidden;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.disc-gradient {
  position: absolute;
  inset: 0;
  background: conic-gradient(
    from 0deg,
    #1e40af 0deg,
    #3b82f6 60deg,
    #06b6d4 120deg,
    #0ea5e9 180deg,
    #3b82f6 240deg,
    #1e40af 300deg,
    #1e40af 360deg
  );
  border-radius: 50%;
  animation: rotate 8s linear infinite;
}

.disc-shine {
  position: absolute;
  inset: 0;
  background: radial-gradient(
    circle at 30% 30%,
    rgba(255, 255, 255, 0.3) 0%,
    rgba(255, 255, 255, 0.1) 30%,
    transparent 70%
  );
  border-radius: 50%;
}

/* Audio Level Rings */
.audio-rings {
  position: absolute;
  inset: 0;
  border-radius: 50%;
}

.audio-ring {
  position: absolute;
  inset: 0;
  border: 2px solid rgba(59, 130, 246, 0.6);
  border-radius: 50%;
  animation: audioRing 1.5s ease-out infinite;
}

/* Pulse Effect */
.pulse-effect {
  position: absolute;
  inset: -10px;
  border: 3px solid rgba(6, 182, 212, 0.5);
  border-radius: 50%;
  animation: pulse 2s ease-in-out infinite;
}

/* Main Button */
.voice-button {
  position: relative;
  z-index: 10;
  width: 140px;
  height: 140px;
  border-radius: 50%;
  background: rgba(15, 23, 42, 0.95);
  border: 2px solid rgba(59, 130, 246, 0.3);
  color: white;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  cursor: pointer;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  backdrop-filter: blur(10px);
  box-shadow: 
    0 0 30px rgba(59, 130, 246, 0.2),
    inset 0 2px 4px rgba(255, 255, 255, 0.1);
}

.voice-button:hover {
  transform: scale(1.05);
  border-color: rgba(59, 130, 246, 0.5);
  box-shadow: 
    0 0 40px rgba(59, 130, 246, 0.3),
    inset 0 2px 4px rgba(255, 255, 255, 0.15);
}

.voice-button:active {
  transform: scale(0.98);
}

.voice-button:disabled {
  cursor: not-allowed;
  opacity: 0.7;
}

/* Button States */
.voice-button.listening {
  border-color: rgba(6, 182, 212, 0.6);
  background: rgba(6, 182, 212, 0.1);
  box-shadow: 
    0 0 50px rgba(6, 182, 212, 0.4),
    inset 0 2px 4px rgba(255, 255, 255, 0.2);
}

.voice-button.speaking {
  border-color: rgba(34, 197, 94, 0.6);
  background: rgba(34, 197, 94, 0.1);
  box-shadow: 
    0 0 50px rgba(34, 197, 94, 0.4),
    inset 0 2px 4px rgba(255, 255, 255, 0.2);
}

.voice-button.connecting {
  border-color: rgba(251, 191, 36, 0.6);
  background: rgba(251, 191, 36, 0.1);
}

.voice-button.error {
  border-color: rgba(239, 68, 68, 0.6);
  background: rgba(239, 68, 68, 0.1);
  box-shadow: 
    0 0 30px rgba(239, 68, 68, 0.3),
    inset 0 2px 4px rgba(255, 255, 255, 0.1);
}

/* Button Content */
.button-icon {
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.icon-mic,
.icon-speaker {
  width: 100%;
  height: 100%;
  stroke-width: 2;
}

.icon-waveform {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 2px;
  height: 100%;
}

.wave-bar {
  width: 3px;
  height: 20px;
  background: currentColor;
  border-radius: 2px;
  animation: waveform 1s ease-in-out infinite;
}

.icon-loading {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.loading-spinner {
  width: 24px;
  height: 24px;
  border: 2px solid rgba(255, 255, 255, 0.3);
  border-top: 2px solid currentColor;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

.button-text {
  font-size: 0.875rem;
  font-weight: 500;
  text-align: center;
  line-height: 1.2;
}

/* Status Message */
.status-message {
  padding: 0.5rem 1rem;
  background: rgba(15, 23, 42, 0.9);
  border: 1px solid rgba(59, 130, 246, 0.3);
  border-radius: 0.5rem;
  color: white;
  font-size: 0.875rem;
  text-align: center;
  backdrop-filter: blur(10px);
  max-width: 200px;
}

.status-message.error {
  border-color: rgba(239, 68, 68, 0.5);
  background: rgba(239, 68, 68, 0.1);
  color: #fca5a5;
}

/* Connection Status */
.connection-status {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.25rem 0.75rem;
  background: rgba(15, 23, 42, 0.8);
  border-radius: 1rem;
  font-size: 0.75rem;
  color: #94a3b8;
  backdrop-filter: blur(10px);
}

.status-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #64748b;
  transition: background-color 0.3s;
}

.connection-status.connecting .status-dot {
  background: #f59e0b;
  animation: pulse 1s ease-in-out infinite;
}

.connection-status.connected .status-dot {
  background: #10b981;
}

.connection-status.error .status-dot {
  background: #ef4444;
}

/* Animations */
@keyframes rotate {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

@keyframes pulse {
  0%, 100% { 
    opacity: 1;
    transform: scale(1);
  }
  50% { 
    opacity: 0.7;
    transform: scale(1.1);
  }
}

@keyframes audioRing {
  0% {
    transform: scale(1);
    opacity: 1;
  }
  100% {
    transform: scale(1.5);
    opacity: 0;
  }
}

@keyframes waveform {
  0%, 100% { height: 8px; }
  50% { height: 24px; }
}

@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

/* Responsive Design */
@media (max-width: 768px) {
  .voice-assistant-container {
    bottom: 2rem;
    right: 50%;
    transform: translateX(50%);
  }
  
  .voice-button-wrapper {
    width: 160px;
    height: 160px;
  }
  
  .voice-button {
    width: 120px;
    height: 120px;
  }
  
  .button-icon {
    width: 28px;
    height: 28px;
  }
  
  .button-text {
    font-size: 0.75rem;
  }
}

/* Active state animations */
.voice-button-wrapper.active .disc-gradient {
  animation-duration: 3s;
}

.voice-button-wrapper.listening .disc-gradient {
  background: conic-gradient(
    from 0deg,
    #0891b2 0deg,
    #06b6d4 60deg,
    #22d3ee 120deg,
    #67e8f9 180deg,
    #06b6d4 240deg,
    #0891b2 300deg,
    #0891b2 360deg
  );
}

.voice-button-wrapper.speaking .disc-gradient {
  background: conic-gradient(
    from 0deg,
    #059669 0deg,
    #10b981 60deg,
    #34d399 120deg,
    #6ee7b7 180deg,
    #10b981 240deg,
    #059669 300deg,
    #059669 360deg
  );
  animation-duration: 2s;
}
</style>