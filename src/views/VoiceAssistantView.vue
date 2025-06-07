<template>
  <div class="min-h-screen">
    <div class="pt-24 pb-4 px-4 text-white relative mb-3">
      <div class="max-w-4xl mx-auto">
        <div class="text-center mb-8">
          <h1 class="font-display text-6xl font-bold mb-6 relative">
            <span class="bg-gradient-to-r from-cyan-300 via-blue-500 to-cyan-300 bg-clip-text text-transparent bg-[length:200%_200%] animate-gradient">
              Voice Assistant
            </span>
          </h1>
          <p class="text-lg text-blue-200/80 font-display tracking-wide">
            Talk to Alex, your AI-powered voice assistant for news analysis and fact-checking
          </p>
        </div>

        <!-- Voice Assistant Features Info -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-12">
          <div class="bg-slate-800/50 rounded-xl p-6 border border-white/10">
            <div class="flex items-center gap-3 mb-4">
              <div class="w-12 h-12 bg-gradient-to-r from-cyan-400 to-blue-500 rounded-lg flex items-center justify-center">
                <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"/>
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 10v2a7 7 0 0 1-14 0v-2"/>
                  <line stroke-linecap="round" stroke-linejoin="round" stroke-width="2" x1="12" y1="19" x2="12" y2="23"/>
                  <line stroke-linecap="round" stroke-linejoin="round" stroke-width="2" x1="8" y1="23" x2="16" y2="23"/>
                </svg>
              </div>
              <h3 class="text-xl font-semibold text-blue-200">Real-time Voice</h3>
            </div>
            <p class="text-slate-300">
              Speak naturally and get instant voice responses powered by advanced AI technology.
            </p>
          </div>

          <div class="bg-slate-800/50 rounded-xl p-6 border border-white/10">
            <div class="flex items-center gap-3 mb-4">
              <div class="w-12 h-12 bg-gradient-to-r from-cyan-400 to-blue-500 rounded-lg flex items-center justify-center">
                <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5h12M9 3v2m1.048 9.5A18.022 18.022 0 016.412 9m6.088 9h7M11 21l5-10 5 10M12.751 5C11.783 10.77 8.07 15.61 3 18.129"/>
                </svg>
              </div>
              <h3 class="text-xl font-semibold text-blue-200">Multilingual</h3>
            </div>
            <p class="text-slate-300">
              Communicate in English or Spanish - Alex automatically detects and responds in your language.
            </p>
          </div>

          <div class="bg-slate-800/50 rounded-xl p-6 border border-white/10">
            <div class="flex items-center gap-3 mb-4">
              <div class="w-12 h-12 bg-gradient-to-r from-cyan-400 to-blue-500 rounded-lg flex items-center justify-center">
                <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
                </svg>
              </div>
              <h3 class="text-xl font-semibold text-blue-200">News Expert</h3>
            </div>
            <p class="text-slate-300">
              Get expert insights on news analysis, bias detection, and fact-checking from your voice assistant.
            </p>
          </div>
        </div>

        <!-- Instructions -->
        <div class="bg-slate-900/50 rounded-xl p-6 border border-white/10 mb-8">
          <h3 class="text-xl font-semibold text-blue-200 mb-4">How to Use</h3>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div class="space-y-3">
              <div class="flex items-start gap-3">
                <div class="w-6 h-6 bg-cyan-400 rounded-full flex items-center justify-center text-slate-900 font-bold text-sm mt-0.5">1</div>
                <p class="text-slate-300">Click the voice button below to start a conversation</p>
              </div>
              <div class="flex items-start gap-3">
                <div class="w-6 h-6 bg-cyan-400 rounded-full flex items-center justify-center text-slate-900 font-bold text-sm mt-0.5">2</div>
                <p class="text-slate-300">Allow microphone access when prompted</p>
              </div>
            </div>
            <div class="space-y-3">
              <div class="flex items-start gap-3">
                <div class="w-6 h-6 bg-cyan-400 rounded-full flex items-center justify-center text-slate-900 font-bold text-sm mt-0.5">3</div>
                <p class="text-slate-300">Speak naturally about news, bias, or fact-checking</p>
              </div>
              <div class="flex items-start gap-3">
                <div class="w-6 h-6 bg-cyan-400 rounded-full flex items-center justify-center text-slate-900 font-bold text-sm mt-0.5">4</div>
                <p class="text-slate-300">Listen to Alex's voice response and continue the conversation</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Sample Questions -->
        <div class="bg-slate-900/50 rounded-xl p-6 border border-white/10 mb-8">
          <h3 class="text-xl font-semibold text-blue-200 mb-4">Try Asking Alex</h3>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="space-y-2">
              <p class="text-slate-300 italic">"How can I detect bias in news articles?"</p>
              <p class="text-slate-300 italic">"What makes a news source reliable?"</p>
              <p class="text-slate-300 italic">"Explain the TruthLens analysis results"</p>
            </div>
            <div class="space-y-2">
              <p class="text-slate-300 italic">"¿Cómo puedo verificar noticias falsas?"</p>
              <p class="text-slate-300 italic">"What are emotional manipulation techniques?"</p>
              <p class="text-slate-300 italic">"Help me understand media literacy"</p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Voice Assistant Component -->
    <VoiceAssistant />
  </div>
</template>

<script setup lang="ts">
import VoiceAssistant from '../components/VoiceAssistant.vue';
</script>

<style scoped>
.animate-gradient {
  animation: gradient 8s linear infinite;
}

@keyframes gradient {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}
</style>