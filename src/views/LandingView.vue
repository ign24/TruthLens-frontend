<template>
  <div class="min-h-screen bg-gradient-to-b from-slate-900 to-slate-950 text-white overflow-hidden">
    <!-- Hero Section -->
    <section class="relative min-h-screen flex items-center justify-center px-4">
      <!-- Background Effects -->
      <div class="absolute inset-0 overflow-hidden">
        <div class="absolute top-1/4 left-1/4 w-96 h-96 bg-blue-500/10 rounded-full blur-3xl animate-pulse"></div>
        <div class="absolute bottom-1/4 right-1/4 w-96 h-96 bg-cyan-500/10 rounded-full blur-3xl animate-pulse delay-1000"></div>
        <div class="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 w-[800px] h-[800px] bg-gradient-to-r from-blue-500/5 to-cyan-500/5 rounded-full blur-3xl"></div>
      </div>

      <div class="relative z-10 text-center max-w-6xl mx-auto">
        <!-- Logo and Title -->
        <div class="mb-8">
          <img
            src="../assets/logo.png"
            alt="TruthLens Logo"
            class="h-20 w-auto mx-auto mb-6 animate-fade-in"
          />
          <h1 class="text-7xl md:text-8xl font-bold mb-6 bg-gradient-to-r from-cyan-300 via-blue-500 to-cyan-300 bg-clip-text text-transparent bg-[length:200%_200%] animate-gradient">
            TruthLens
          </h1>
          <p class="text-2xl md:text-3xl text-blue-200/80 font-light mb-8 animate-fade-in-up">
            AI-Powered News Analysis & Voice Assistant
          </p>
          <p class="text-lg md:text-xl text-slate-300 max-w-3xl mx-auto leading-relaxed animate-fade-in-up delay-200">
            Detect bias, analyze credibility, and get instant insights with our advanced AI technology. 
            Now featuring real-time voice conversations with Alex, your intelligent news analysis companion.
          </p>
        </div>

        <!-- CTA Buttons -->
        <div class="flex flex-col sm:flex-row gap-6 justify-center items-center mb-12 animate-fade-in-up delay-400">
          <RouterLink
            to="/analyze"
            class="group relative px-8 py-4 bg-gradient-to-r from-cyan-400 to-blue-500 text-white rounded-xl font-semibold text-lg transition-all duration-300 hover:scale-105 hover:shadow-2xl hover:shadow-cyan-500/25 min-w-[200px]"
          >
            <span class="relative z-10">Start Analyzing</span>
            <div class="absolute inset-0 bg-gradient-to-r from-cyan-300 to-blue-400 rounded-xl opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
          </RouterLink>
          
          <button
            @click="scrollToDemo"
            class="group px-8 py-4 border-2 border-cyan-400/50 text-cyan-300 rounded-xl font-semibold text-lg transition-all duration-300 hover:border-cyan-400 hover:bg-cyan-400/10 hover:scale-105 min-w-[200px]"
          >
            <span class="flex items-center justify-center gap-2">
              <svg class="w-5 h-5 group-hover:animate-bounce" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.536 8.464a5 5 0 010 7.072m2.828-9.9a9 9 0 010 14.142M8 21l4-4H5a2 2 0 01-2-2V9a2 2 0 012-2h7l4-4v18z" />
              </svg>
              Try Voice AI
            </span>
          </button>
        </div>

        <!-- Stats -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-4xl mx-auto animate-fade-in-up delay-600">
          <div class="text-center">
            <div class="text-4xl font-bold text-cyan-400 mb-2">99.2%</div>
            <div class="text-slate-300">Accuracy Rate</div>
          </div>
          <div class="text-center">
            <div class="text-4xl font-bold text-blue-400 mb-2">35+</div>
            <div class="text-slate-300">Languages Supported</div>
          </div>
          <div class="text-center">
            <div class="text-4xl font-bold text-cyan-400 mb-2">Real-time</div>
            <div class="text-slate-300">Voice Analysis</div>
          </div>
        </div>
      </div>

      <!-- Scroll Indicator -->
      <div class="absolute bottom-8 left-1/2 transform -translate-x-1/2 animate-bounce">
        <svg class="w-6 h-6 text-cyan-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 14l-7 7m0 0l-7-7m7 7V3" />
        </svg>
      </div>
    </section>

    <!-- Features Section -->
    <section class="py-20 px-4 relative">
      <div class="max-w-7xl mx-auto">
        <div class="text-center mb-16">
          <h2 class="text-5xl font-bold mb-6 bg-gradient-to-r from-cyan-300 to-blue-400 bg-clip-text text-transparent">
            Powerful Features
          </h2>
          <p class="text-xl text-slate-300 max-w-3xl mx-auto">
            Advanced AI technology to help you navigate the complex world of news and information
          </p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          <!-- Feature 1: News Analysis -->
          <div class="group p-8 bg-slate-800/50 rounded-2xl border border-white/10 hover:border-cyan-400/50 transition-all duration-300 hover:transform hover:scale-105">
            <div class="w-16 h-16 bg-gradient-to-r from-cyan-400 to-blue-500 rounded-xl flex items-center justify-center mb-6 group-hover:scale-110 transition-transform duration-300">
              <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
              </svg>
            </div>
            <h3 class="text-2xl font-bold mb-4 text-white group-hover:text-cyan-300 transition-colors">News Analysis</h3>
            <p class="text-slate-300 leading-relaxed">
              Analyze articles for bias, credibility, and emotional tone. Get detailed breakdowns of factual accuracy and political leanings.
            </p>
          </div>

          <!-- Feature 2: Voice AI Assistant -->
          <div class="group p-8 bg-slate-800/50 rounded-2xl border border-white/10 hover:border-cyan-400/50 transition-all duration-300 hover:transform hover:scale-105">
            <div class="w-16 h-16 bg-gradient-to-r from-cyan-400 to-blue-500 rounded-xl flex items-center justify-center mb-6 group-hover:scale-110 transition-transform duration-300">
              <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.536 8.464a5 5 0 010 7.072m2.828-9.9a9 9 0 010 14.142M8 21l4-4H5a2 2 0 01-2-2V9a2 2 0 012-2h7l4-4v18z" />
              </svg>
            </div>
            <h3 class="text-2xl font-bold mb-4 text-white group-hover:text-cyan-300 transition-colors">Voice AI Assistant</h3>
            <p class="text-slate-300 leading-relaxed">
              Talk to Alex, our intelligent voice assistant. Get instant explanations and insights through natural conversation.
            </p>
          </div>

          <!-- Feature 3: Multilingual Support -->
          <div class="group p-8 bg-slate-800/50 rounded-2xl border border-white/10 hover:border-cyan-400/50 transition-all duration-300 hover:transform hover:scale-105">
            <div class="w-16 h-16 bg-gradient-to-r from-cyan-400 to-blue-500 rounded-xl flex items-center justify-center mb-6 group-hover:scale-110 transition-transform duration-300">
              <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5h12M9 3v2m1.048 9.5A18.022 18.022 0 016.412 9m6.088 9h7M11 21l5-10 5 10M12.751 5C11.783 10.77 8.07 15.61 3 18.129" />
              </svg>
            </div>
            <h3 class="text-2xl font-bold mb-4 text-white group-hover:text-cyan-300 transition-colors">Multilingual Support</h3>
            <p class="text-slate-300 leading-relaxed">
              Analyze content in 35+ languages. Professional translation with context awareness and cultural adaptation.
            </p>
          </div>

          <!-- Feature 4: Real-time Processing -->
          <div class="group p-8 bg-slate-800/50 rounded-2xl border border-white/10 hover:border-cyan-400/50 transition-all duration-300 hover:transform hover:scale-105">
            <div class="w-16 h-16 bg-gradient-to-r from-cyan-400 to-blue-500 rounded-xl flex items-center justify-center mb-6 group-hover:scale-110 transition-transform duration-300">
              <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
              </svg>
            </div>
            <h3 class="text-2xl font-bold mb-4 text-white group-hover:text-cyan-300 transition-colors">Real-time Processing</h3>
            <p class="text-slate-300 leading-relaxed">
              Get instant results with our optimized AI models. Low-latency voice responses and rapid text analysis.
            </p>
          </div>

          <!-- Feature 5: Bias Detection -->
          <div class="group p-8 bg-slate-800/50 rounded-2xl border border-white/10 hover:border-cyan-400/50 transition-all duration-300 hover:transform hover:scale-105">
            <div class="w-16 h-16 bg-gradient-to-r from-cyan-400 to-blue-500 rounded-xl flex items-center justify-center mb-6 group-hover:scale-110 transition-transform duration-300">
              <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
              </svg>
            </div>
            <h3 class="text-2xl font-bold mb-4 text-white group-hover:text-cyan-300 transition-colors">Bias Detection</h3>
            <p class="text-slate-300 leading-relaxed">
              Identify political bias, emotional manipulation, and propaganda techniques with advanced NLP algorithms.
            </p>
          </div>

          <!-- Feature 6: Interactive Chat -->
          <div class="group p-8 bg-slate-800/50 rounded-2xl border border-white/10 hover:border-cyan-400/50 transition-all duration-300 hover:transform hover:scale-105">
            <div class="w-16 h-16 bg-gradient-to-r from-cyan-400 to-blue-500 rounded-xl flex items-center justify-center mb-6 group-hover:scale-110 transition-transform duration-300">
              <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z" />
              </svg>
            </div>
            <h3 class="text-2xl font-bold mb-4 text-white group-hover:text-cyan-300 transition-colors">Interactive Chat</h3>
            <p class="text-slate-300 leading-relaxed">
              Ask questions about your analysis results. Get detailed explanations and recommendations from our AI assistant.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Voice AI Demo Section -->
    <section ref="demoSection" class="py-20 px-4 bg-gradient-to-r from-slate-900/50 to-slate-800/50">
      <div class="max-w-6xl mx-auto text-center">
        <h2 class="text-5xl font-bold mb-6 bg-gradient-to-r from-cyan-300 to-blue-400 bg-clip-text text-transparent">
          Meet Alex, Your Voice AI Assistant
        </h2>
        <p class="text-xl text-slate-300 mb-12 max-w-3xl mx-auto">
          Experience the future of news analysis with real-time voice conversations. 
          Alex understands context, speaks multiple languages, and provides instant insights.
        </p>

        <!-- Voice Assistant Demo -->
        <div class="relative max-w-2xl mx-auto">
          <!-- Demo Voice Button -->
          <div class="voice-demo-container mb-8">
            <div class="voice-demo-disc">
              <div class="demo-gradient"></div>
              <div class="demo-shine"></div>
            </div>
            <button class="voice-demo-button" @click="playDemoAudio">
              <div class="demo-icon">
                <svg class="w-8 h-8" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.536 8.464a5 5 0 010 7.072m2.828-9.9a9 9 0 010 14.142M8 21l4-4H5a2 2 0 01-2-2V9a2 2 0 012-2h7l4-4v18z" />
                </svg>
              </div>
              <span class="demo-text">Try Voice Demo</span>
            </button>
          </div>

          <!-- Demo Features -->
          <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mt-12">
            <div class="p-6 bg-slate-800/30 rounded-xl border border-cyan-400/20">
              <div class="w-12 h-12 bg-cyan-400/20 rounded-lg flex items-center justify-center mb-4 mx-auto">
                <svg class="w-6 h-6 text-cyan-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 18h.01M8 21h8a2 2 0 002-2V5a2 2 0 00-2-2H8a2 2 0 00-2 2v14a2 2 0 002 2z" />
                </svg>
              </div>
              <h3 class="text-lg font-semibold text-white mb-2">Natural Speech</h3>
              <p class="text-slate-300 text-sm">Speak naturally and get human-like responses</p>
            </div>

            <div class="p-6 bg-slate-800/30 rounded-xl border border-cyan-400/20">
              <div class="w-12 h-12 bg-cyan-400/20 rounded-lg flex items-center justify-center mb-4 mx-auto">
                <svg class="w-6 h-6 text-cyan-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
                </svg>
              </div>
              <h3 class="text-lg font-semibold text-white mb-2">Instant Response</h3>
              <p class="text-slate-300 text-sm">Low-latency processing for real-time conversations</p>
            </div>

            <div class="p-6 bg-slate-800/30 rounded-xl border border-cyan-400/20">
              <div class="w-12 h-12 bg-cyan-400/20 rounded-lg flex items-center justify-center mb-4 mx-auto">
                <svg class="w-6 h-6 text-cyan-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5h12M9 3v2m1.048 9.5A18.022 18.022 0 016.412 9m6.088 9h7M11 21l5-10 5 10M12.751 5C11.783 10.77 8.07 15.61 3 18.129" />
                </svg>
              </div>
              <h3 class="text-lg font-semibold text-white mb-2">Multilingual</h3>
              <p class="text-slate-300 text-sm">Responds in your preferred language automatically</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- How It Works Section -->
    <section class="py-20 px-4">
      <div class="max-w-6xl mx-auto">
        <div class="text-center mb-16">
          <h2 class="text-5xl font-bold mb-6 bg-gradient-to-r from-cyan-300 to-blue-400 bg-clip-text text-transparent">
            How It Works
          </h2>
          <p class="text-xl text-slate-300 max-w-3xl mx-auto">
            Simple, powerful, and intelligent. Get insights in three easy steps.
          </p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <!-- Step 1 -->
          <div class="text-center group">
            <div class="relative mb-8">
              <div class="w-24 h-24 bg-gradient-to-r from-cyan-400 to-blue-500 rounded-full flex items-center justify-center mx-auto group-hover:scale-110 transition-transform duration-300">
                <span class="text-2xl font-bold text-white">1</span>
              </div>
              <div class="absolute top-1/2 left-full w-full h-0.5 bg-gradient-to-r from-cyan-400/50 to-transparent hidden md:block"></div>
            </div>
            <h3 class="text-2xl font-bold mb-4 text-white">Input Content</h3>
            <p class="text-slate-300 leading-relaxed">
              Paste your news article or speak directly to Alex. Our AI processes text and voice input seamlessly.
            </p>
          </div>

          <!-- Step 2 -->
          <div class="text-center group">
            <div class="relative mb-8">
              <div class="w-24 h-24 bg-gradient-to-r from-cyan-400 to-blue-500 rounded-full flex items-center justify-center mx-auto group-hover:scale-110 transition-transform duration-300">
                <span class="text-2xl font-bold text-white">2</span>
              </div>
              <div class="absolute top-1/2 left-full w-full h-0.5 bg-gradient-to-r from-cyan-400/50 to-transparent hidden md:block"></div>
            </div>
            <h3 class="text-2xl font-bold mb-4 text-white">AI Analysis</h3>
            <p class="text-slate-300 leading-relaxed">
              Advanced algorithms analyze bias, credibility, emotional tone, and factual accuracy in real-time.
            </p>
          </div>

          <!-- Step 3 -->
          <div class="text-center group">
            <div class="relative mb-8">
              <div class="w-24 h-24 bg-gradient-to-r from-cyan-400 to-blue-500 rounded-full flex items-center justify-center mx-auto group-hover:scale-110 transition-transform duration-300">
                <span class="text-2xl font-bold text-white">3</span>
              </div>
            </div>
            <h3 class="text-2xl font-bold mb-4 text-white">Get Insights</h3>
            <p class="text-slate-300 leading-relaxed">
              Receive detailed reports and recommendations. Ask follow-up questions through voice or text chat.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA Section -->
    <section class="py-20 px-4 bg-gradient-to-r from-cyan-900/20 to-blue-900/20">
      <div class="max-w-4xl mx-auto text-center">
        <h2 class="text-5xl font-bold mb-6 bg-gradient-to-r from-cyan-300 to-blue-400 bg-clip-text text-transparent">
          Ready to Analyze?
        </h2>
        <p class="text-xl text-slate-300 mb-8 max-w-2xl mx-auto">
          Join thousands of users who trust TruthLens for accurate news analysis and bias detection.
        </p>
        
        <div class="flex flex-col sm:flex-row gap-6 justify-center items-center">
          <RouterLink
            to="/analyze"
            class="group relative px-10 py-5 bg-gradient-to-r from-cyan-400 to-blue-500 text-white rounded-xl font-semibold text-xl transition-all duration-300 hover:scale-105 hover:shadow-2xl hover:shadow-cyan-500/25 min-w-[250px]"
          >
            <span class="relative z-10 flex items-center justify-center gap-2">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
              </svg>
              Start Analyzing Now
            </span>
            <div class="absolute inset-0 bg-gradient-to-r from-cyan-300 to-blue-400 rounded-xl opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
          </RouterLink>
          
          <RouterLink
            to="/translator"
            class="group px-10 py-5 border-2 border-cyan-400/50 text-cyan-300 rounded-xl font-semibold text-xl transition-all duration-300 hover:border-cyan-400 hover:bg-cyan-400/10 hover:scale-105 min-w-[250px]"
          >
            <span class="flex items-center justify-center gap-2">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5h12M9 3v2m1.048 9.5A18.022 18.022 0 016.412 9m6.088 9h7M11 21l5-10 5 10M12.751 5C11.783 10.77 8.07 15.61 3 18.129" />
              </svg>
              Try Translator Pro
            </span>
          </RouterLink>
        </div>
      </div>
    </section>

    <!-- Footer -->
    <footer class="py-12 px-4 border-t border-white/10">
      <div class="max-w-6xl mx-auto">
        <div class="flex flex-col md:flex-row justify-between items-center">
          <div class="flex items-center space-x-3 mb-4 md:mb-0">
            <img
              src="../assets/logo.png"
              alt="TruthLens Logo"
              class="h-8 w-auto"
            />
            <span class="text-xl font-bold text-white">TruthLens</span>
          </div>
          
          <div class="flex items-center space-x-6">
            <RouterLink to="/analyze" class="text-slate-300 hover:text-white transition-colors">
              Analyze
            </RouterLink>
            <RouterLink to="/translator" class="text-slate-300 hover:text-white transition-colors">
              Translator
            </RouterLink>
            <a href="https://truthlens-backend-production.up.railway.app/docs" target="_blank" class="text-slate-300 hover:text-white transition-colors">
              API Docs
            </a>
          </div>
          
          <div class="flex items-center space-x-4 mt-4 md:mt-0">
            <a href="https://bolt.new" target="_blank" rel="noopener noreferrer"
              class="flex items-center space-x-2 px-4 py-2 rounded-full bg-gradient-to-r from-cyan-400 to-blue-500 text-white text-sm font-medium hover:opacity-90 transition-opacity">
              <span>Made with Bolt</span>
            </a>
          </div>
        </div>
        
        <div class="mt-8 pt-8 border-t border-white/10 text-center text-slate-400">
          <p>&copy; 2024 TruthLens. Powered by advanced AI technology.</p>
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { RouterLink } from 'vue-router';

const demoSection = ref<HTMLElement | null>(null);

const scrollToDemo = () => {
  if (demoSection.value) {
    demoSection.value.scrollIntoView({ behavior: 'smooth' });
  }
};

const playDemoAudio = () => {
  // Demo functionality - could play a sample audio or show a modal
  alert('Voice demo would play here! Click "Start Analyzing" to try the real voice assistant.');
};
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

.animate-fade-in {
  animation: fadeIn 1s ease-out;
}

.animate-fade-in-up {
  animation: fadeInUp 1s ease-out;
}

.delay-200 {
  animation-delay: 200ms;
}

.delay-400 {
  animation-delay: 400ms;
}

.delay-600 {
  animation-delay: 600ms;
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Voice Demo Styles */
.voice-demo-container {
  position: relative;
  width: 200px;
  height: 200px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: center;
}

.voice-demo-disc {
  position: absolute;
  inset: 0;
  border-radius: 50%;
  overflow: hidden;
}

.demo-gradient {
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

.demo-shine {
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

.voice-demo-button {
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

.voice-demo-button:hover {
  transform: scale(1.05);
  border-color: rgba(59, 130, 246, 0.5);
  box-shadow: 
    0 0 40px rgba(59, 130, 246, 0.3),
    inset 0 2px 4px rgba(255, 255, 255, 0.15);
}

.demo-icon {
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.demo-text {
  font-size: 0.875rem;
  font-weight: 500;
  text-align: center;
  line-height: 1.2;
}

@keyframes rotate {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

/* Responsive adjustments */
@media (max-width: 768px) {
  .voice-demo-container {
    width: 160px;
    height: 160px;
  }
  
  .voice-demo-button {
    width: 120px;
    height: 120px;
  }
  
  .demo-icon {
    width: 28px;
    height: 28px;
  }
  
  .demo-text {
    font-size: 0.75rem;
  }
}
</style>