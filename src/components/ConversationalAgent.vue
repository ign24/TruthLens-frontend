<script setup lang="ts">
import { ref, computed, nextTick, watch, onMounted } from 'vue';

interface Message {
  id: string;
  role: 'user' | 'assistant';
  content: string;
  timestamp: Date;
  language: string;
  audioUrl?: string;
  isPlaying?: boolean;
}

const messages = ref<Message[]>([]);
const userInput = ref('');
const selectedLanguage = ref('en');
const isLoading = ref(false);
const isGeneratingAudio = ref(false);
const messagesContainer = ref<HTMLElement | null>(null);
const inputRef = ref<HTMLInputElement | null>(null);

// Language options with native names and voice configurations
const languages = [
  { code: 'en', name: 'English', nativeName: 'English', voice: 'Rachel' },
  { code: 'es', name: 'Spanish', nativeName: 'Español', voice: 'Domi' },
  { code: 'fr', name: 'French', nativeName: 'Français', voice: 'Charlotte' },
  { code: 'de', name: 'German', nativeName: 'Deutsch', voice: 'Freya' },
  { code: 'it', name: 'Italian', nativeName: 'Italiano', voice: 'Matilda' },
  { code: 'pt', name: 'Portuguese', nativeName: 'Português', voice: 'Camila' },
  { code: 'ru', name: 'Russian', nativeName: 'Русский', voice: 'Bella' },
  { code: 'ja', name: 'Japanese', nativeName: '日本語', voice: 'Takuya' },
  { code: 'ko', name: 'Korean', nativeName: '한국어', voice: 'Seraphina' },
  { code: 'zh', name: 'Chinese', nativeName: '中文', voice: 'Xiaoxiao' },
  { code: 'ar', name: 'Arabic', nativeName: 'العربية', voice: 'Layla' },
  { code: 'hi', name: 'Hindi', nativeName: 'हिन्दी', voice: 'Aditi' },
  { code: 'nl', name: 'Dutch', nativeName: 'Nederlands', voice: 'Laura' },
  { code: 'pl', name: 'Polish', nativeName: 'Polski', voice: 'Ewa' },
  { code: 'tr', name: 'Turkish', nativeName: 'Türkçe', voice: 'Defne' },
  { code: 'sv', name: 'Swedish', nativeName: 'Svenska', voice: 'Astrid' },
  { code: 'no', name: 'Norwegian', nativeName: 'Norsk', voice: 'Ida' },
  { code: 'da', name: 'Danish', nativeName: 'Dansk', voice: 'Naja' },
  { code: 'fi', name: 'Finnish', nativeName: 'Suomi', voice: 'Suvi' },
  { code: 'el', name: 'Greek', nativeName: 'Ελληνικά', voice: 'Athena' },
  { code: 'he', name: 'Hebrew', nativeName: 'עברית', voice: 'Tamar' },
  { code: 'th', name: 'Thai', nativeName: 'ไทย', voice: 'Premwadee' },
  { code: 'vi', name: 'Vietnamese', nativeName: 'Tiếng Việt', voice: 'Chi' },
  { code: 'id', name: 'Indonesian', nativeName: 'Bahasa Indonesia', voice: 'Gadis' },
  { code: 'ms', name: 'Malay', nativeName: 'Bahasa Melayu', voice: 'Yasmin' },
  { code: 'tl', name: 'Filipino', nativeName: 'Filipino', voice: 'Blessica' },
  { code: 'uk', name: 'Ukrainian', nativeName: 'Українська', voice: 'Polina' },
  { code: 'cs', name: 'Czech', nativeName: 'Čeština', voice: 'Tereza' },
  { code: 'sk', name: 'Slovak', nativeName: 'Slovenčina', voice: 'Viktoria' },
  { code: 'hu', name: 'Hungarian', nativeName: 'Magyar', voice: 'Tamas' },
  { code: 'ro', name: 'Romanian', nativeName: 'Română', voice: 'Oana' },
  { code: 'bg', name: 'Bulgarian', nativeName: 'Български', voice: 'Gergana' },
  { code: 'hr', name: 'Croatian', nativeName: 'Hrvatski', voice: 'Gabrijela' },
  { code: 'sr', name: 'Serbian', nativeName: 'Српски', voice: 'Milica' },
  { code: 'sl', name: 'Slovenian', nativeName: 'Slovenščina', voice: 'Petra' },
  { code: 'et', name: 'Estonian', nativeName: 'Eesti', voice: 'Kaia' },
  { code: 'lv', name: 'Latvian', nativeName: 'Latviešu', voice: 'Everita' },
  { code: 'lt', name: 'Lithuanian', nativeName: 'Lietuvių', voice: 'Ona' }
];

const currentLanguage = computed(() => {
  return languages.find(lang => lang.code === selectedLanguage.value) || languages[0];
});

const canSend = computed(() => {
  return userInput.value.trim().length > 0 && !isLoading.value;
});

// Scroll to bottom of messages
const scrollToBottom = () => {
  if (messagesContainer.value) {
    nextTick(() => {
      messagesContainer.value!.scrollTop = messagesContainer.value!.scrollHeight;
    });
  }
};

// Generate unique message ID
const generateMessageId = () => {
  return Date.now().toString(36) + Math.random().toString(36).substr(2);
};

// Get language-specific system prompt
const getSystemPrompt = (languageCode: string, languageName: string) => {
  return `You are a friendly, helpful, and culturally aware multilingual conversational assistant. You are fluent in 35+ languages and designed to help users practice languages or communicate across language barriers.

CRITICAL INSTRUCTIONS:
- You MUST respond ONLY in ${languageName} (${languageCode}) unless the user explicitly requests a different language
- Be conversational, engaging, and culturally appropriate for ${languageName} speakers
- Help users practice the language by using natural, everyday expressions
- If the user makes language mistakes, gently correct them in a helpful way
- Adapt your personality and communication style to be culturally appropriate for ${languageName}
- Keep responses concise but engaging (1-3 sentences typically)
- Use appropriate greetings, expressions, and cultural references for ${languageName}

Remember: Always respond in ${languageName} unless explicitly told otherwise!`;
};

// Send message to OpenAI
const sendMessage = async () => {
  if (!canSend.value) return;

  const userMessage: Message = {
    id: generateMessageId(),
    role: 'user',
    content: userInput.value.trim(),
    timestamp: new Date(),
    language: selectedLanguage.value
  };

  messages.value.push(userMessage);
  const currentInput = userInput.value;
  userInput.value = '';
  isLoading.value = true;
  scrollToBottom();

  try {
    // Prepare conversation history for OpenAI
    const conversationHistory = messages.value.map(msg => ({
      role: msg.role,
      content: msg.content
    }));

    // Add system message
    const systemMessage = {
      role: 'system' as const,
      content: getSystemPrompt(selectedLanguage.value, currentLanguage.value.name)
    };

    const response = await fetch('https://api.openai.com/v1/chat/completions', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${import.meta.env.VITE_OPENAI_API_KEY}`
      },
      body: JSON.stringify({
        model: 'gpt-4o',
        messages: [systemMessage, ...conversationHistory],
        max_tokens: 500,
        temperature: 0.7
      })
    });

    if (!response.ok) {
      throw new Error(`OpenAI API error: ${response.status}`);
    }

    const data = await response.json();
    const assistantResponse = data.choices[0]?.message?.content || 'I apologize, but I couldn\'t generate a response.';

    const assistantMessage: Message = {
      id: generateMessageId(),
      role: 'assistant',
      content: assistantResponse,
      timestamp: new Date(),
      language: selectedLanguage.value
    };

    messages.value.push(assistantMessage);
    scrollToBottom();

  } catch (error) {
    console.error('Error sending message:', error);
    
    const errorMessage: Message = {
      id: generateMessageId(),
      role: 'assistant',
      content: 'I apologize, but I encountered an error. Please check your API configuration and try again.',
      timestamp: new Date(),
      language: selectedLanguage.value
    };

    messages.value.push(errorMessage);
    scrollToBottom();
  } finally {
    isLoading.value = false;
    nextTick(() => {
      inputRef.value?.focus();
    });
  }
};

// Generate and play audio using ElevenLabs
const playAudio = async (message: Message) => {
  if (message.isPlaying) return;

  try {
    isGeneratingAudio.value = true;
    message.isPlaying = true;

    // If audio URL already exists, just play it
    if (message.audioUrl) {
      const audio = new Audio(message.audioUrl);
      audio.onended = () => {
        message.isPlaying = false;
      };
      await audio.play();
      return;
    }

    // Generate new audio
    const voiceId = currentLanguage.value.voice;
    const response = await fetch(`https://api.elevenlabs.io/v1/text-to-speech/${voiceId}`, {
      method: 'POST',
      headers: {
        'Accept': 'audio/mpeg',
        'Content-Type': 'application/json',
        'xi-api-key': import.meta.env.VITE_ELEVENLABS_API_KEY
      },
      body: JSON.stringify({
        text: message.content,
        model_id: 'eleven_multilingual_v2',
        voice_settings: {
          stability: 0.5,
          similarity_boost: 0.5,
          style: 0.5,
          use_speaker_boost: true
        }
      })
    });

    if (!response.ok) {
      throw new Error(`ElevenLabs API error: ${response.status}`);
    }

    const audioBlob = await response.blob();
    const audioUrl = URL.createObjectURL(audioBlob);
    message.audioUrl = audioUrl;

    const audio = new Audio(audioUrl);
    audio.onended = () => {
      message.isPlaying = false;
    };
    await audio.play();

  } catch (error) {
    console.error('Error playing audio:', error);
    message.isPlaying = false;
    alert('Error generating audio. Please check your ElevenLabs API configuration.');
  } finally {
    isGeneratingAudio.value = false;
  }
};

// Clear conversation
const clearConversation = () => {
  messages.value = [];
  // Clean up audio URLs
  messages.value.forEach(msg => {
    if (msg.audioUrl) {
      URL.revokeObjectURL(msg.audioUrl);
    }
  });
};

// Handle Enter key
const handleKeyPress = (event: KeyboardEvent) => {
  if (event.key === 'Enter' && !event.shiftKey) {
    event.preventDefault();
    sendMessage();
  }
};

// Initialize with welcome message
onMounted(() => {
  const welcomeMessage: Message = {
    id: generateMessageId(),
    role: 'assistant',
    content: 'Hello! I\'m your multilingual conversational companion. Select a language and start chatting with me! 🌍',
    timestamp: new Date(),
    language: 'en'
  };
  messages.value.push(welcomeMessage);
});

// Watch language changes and add notification
watch(selectedLanguage, (newLang, oldLang) => {
  if (oldLang && newLang !== oldLang) {
    const langInfo = languages.find(l => l.code === newLang);
    const notificationMessage: Message = {
      id: generateMessageId(),
      role: 'assistant',
      content: `Language switched to ${langInfo?.name} (${langInfo?.nativeName}). I'll respond in ${langInfo?.name} from now on!`,
      timestamp: new Date(),
      language: newLang
    };
    messages.value.push(notificationMessage);
    scrollToBottom();
  }
});
</script>

<template>
  <div class="max-w-4xl mx-auto p-6 space-y-6">
    <!-- Header -->
    <div class="text-center space-y-4">
      <h2 class="text-3xl font-bold bg-gradient-to-r from-cyan-300 via-blue-500 to-cyan-300 bg-clip-text text-transparent">
        Multilingual Conversational Agent
      </h2>
      <p class="text-blue-200/80">
        Practice languages and communicate across barriers with AI-powered conversations
      </p>
    </div>

    <!-- Language Selector -->
    <div class="flex flex-col sm:flex-row items-center gap-4 p-4 bg-slate-800/50 rounded-xl border border-white/10">
      <label class="text-blue-200 font-medium whitespace-nowrap">
        Conversation Language:
      </label>
      <div class="relative flex-1 max-w-xs">
        <select 
          v-model="selectedLanguage"
          class="w-full bg-slate-900 border border-blue-500/50 rounded-lg px-4 py-2 text-white focus:outline-none focus:ring-2 focus:ring-cyan-400 appearance-none pr-10"
        >
          <option v-for="lang in languages" :key="lang.code" :value="lang.code">
            {{ lang.name }} ({{ lang.nativeName }})
          </option>
        </select>
        <div class="absolute right-3 top-1/2 transform -translate-y-1/2 pointer-events-none">
          <svg class="w-4 h-4 text-blue-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
          </svg>
        </div>
      </div>
      <button
        @click="clearConversation"
        class="px-4 py-2 bg-slate-700/50 text-slate-300 rounded-lg hover:bg-slate-600/50 transition-colors text-sm"
      >
        Clear Chat
      </button>
    </div>

    <!-- Chat Messages -->
    <div 
      ref="messagesContainer"
      class="h-96 overflow-y-auto space-y-4 p-4 bg-slate-900/50 rounded-xl border border-white/10 scroll-smooth"
    >
      <div
        v-for="message in messages"
        :key="message.id"
        class="flex"
        :class="message.role === 'user' ? 'justify-end' : 'justify-start'"
      >
        <div
          class="max-w-[80%] rounded-2xl p-4 space-y-2"
          :class="[
            message.role === 'user' 
              ? 'bg-gradient-to-r from-blue-600 to-blue-700 text-white' 
              : 'bg-slate-800/80 text-white border border-white/10'
          ]"
        >
          <div class="flex items-start gap-2">
            <div class="flex-1">
              <p class="text-sm leading-relaxed">{{ message.content }}</p>
            </div>
            
            <!-- Audio button for assistant messages -->
            <button
              v-if="message.role === 'assistant'"
              @click="playAudio(message)"
              :disabled="isGeneratingAudio || message.isPlaying"
              class="flex-shrink-0 p-2 rounded-lg bg-slate-700/50 hover:bg-slate-600/50 transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
              :title="message.isPlaying ? 'Playing...' : 'Listen'"
            >
              <svg 
                v-if="!message.isPlaying" 
                class="w-4 h-4 text-blue-300" 
                fill="none" 
                stroke="currentColor" 
                viewBox="0 0 24 24"
              >
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.536 8.464a5 5 0 010 7.072m2.828-9.9a9 9 0 010 14.142M8 21l4-4H5a2 2 0 01-2-2V9a2 2 0 012-2h7l4-4v18z" />
              </svg>
              <div v-else class="w-4 h-4 flex items-center justify-center">
                <div class="w-2 h-2 bg-blue-300 rounded-full animate-pulse"></div>
              </div>
            </button>
          </div>
          
          <div class="flex items-center justify-between text-xs opacity-70">
            <span>{{ message.timestamp.toLocaleTimeString() }}</span>
            <span v-if="message.role === 'assistant'" class="text-blue-300">
              {{ languages.find(l => l.code === message.language)?.nativeName }}
            </span>
          </div>
        </div>
      </div>

      <!-- Loading indicator -->
      <div v-if="isLoading" class="flex justify-start">
        <div class="bg-slate-800/80 rounded-2xl p-4 border border-white/10">
          <div class="flex items-center space-x-2">
            <div class="flex space-x-1">
              <div class="w-2 h-2 bg-blue-400 rounded-full animate-bounce"></div>
              <div class="w-2 h-2 bg-blue-400 rounded-full animate-bounce delay-100"></div>
              <div class="w-2 h-2 bg-blue-400 rounded-full animate-bounce delay-200"></div>
            </div>
            <span class="text-sm text-slate-300">Thinking...</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Input Area -->
    <div class="flex gap-3 p-4 bg-slate-800/50 rounded-xl border border-white/10">
      <input
        ref="inputRef"
        v-model="userInput"
        @keypress="handleKeyPress"
        type="text"
        placeholder="Type your message in any language..."
        class="flex-1 bg-slate-900 border border-blue-500/50 rounded-lg px-4 py-3 text-white placeholder-blue-200/50 focus:outline-none focus:ring-2 focus:ring-cyan-400"
        :disabled="isLoading"
      />
      <button
        @click="sendMessage"
        :disabled="!canSend"
        class="px-6 py-3 bg-gradient-to-r from-cyan-400 to-blue-500 text-white rounded-lg font-medium transition-all duration-300 hover:scale-105 active:scale-95 disabled:opacity-50 disabled:cursor-not-allowed disabled:hover:scale-100"
      >
        <svg v-if="!isLoading" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8" />
        </svg>
        <div v-else class="w-5 h-5 border-2 border-white border-t-transparent rounded-full animate-spin"></div>
      </button>
    </div>

    <!-- API Configuration Notice -->
    <div class="p-4 bg-yellow-900/20 border border-yellow-500/30 rounded-xl">
      <div class="flex items-start gap-3">
        <svg class="w-5 h-5 text-yellow-400 mt-0.5 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-2.5L13.732 4c-.77-.833-1.964-.833-2.732 0L4.082 16.5c-.77.833.192 2.5 1.732 2.5z" />
        </svg>
        <div class="text-sm text-yellow-200">
          <p class="font-medium mb-1">API Configuration Required</p>
          <p>To use this feature, you need to set up environment variables:</p>
          <ul class="mt-2 space-y-1 text-xs">
            <li>• <code class="bg-yellow-900/30 px-1 rounded">VITE_OPENAI_API_KEY</code> - Your OpenAI API key</li>
            <li>• <code class="bg-yellow-900/30 px-1 rounded">VITE_ELEVENLABS_API_KEY</code> - Your ElevenLabs API key</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.delay-100 {
  animation-delay: 150ms;
}

.delay-200 {
  animation-delay: 300ms;
}

/* Custom scrollbar */
.overflow-y-auto {
  scrollbar-width: thin;
  scrollbar-color: rgba(148, 163, 184, 0.3) transparent;
}

.overflow-y-auto::-webkit-scrollbar {
  width: 6px;
}

.overflow-y-auto::-webkit-scrollbar-track {
  background: transparent;
}

.overflow-y-auto::-webkit-scrollbar-thumb {
  background-color: rgba(148, 163, 184, 0.3);
  border-radius: 3px;
}

.overflow-y-auto::-webkit-scrollbar-thumb:hover {
  background-color: rgba(148, 163, 184, 0.5);
}
</style>