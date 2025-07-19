# Project Title: Outbound AI Voice Agent for Real-Time Telephonic Conversations

# 📝 Project Summary
Build a real-time AI voice agent that makes outbound calls, engages customers using natural conversations, and moves step-by-step in a selling flow (like insurance, service plans, etc.). The system uses LiveKit, Gemini Model, and connects via a telephonic integration to handle audio, transcription, and conversational flow.


# 🧱 Tech Stack
- AI Model: Gemini Live Transcription
- Voice Infra: LiveKit
- Python (Backend)

**I have already Build most of the functionality of the Bot** 

## Thing's I want you to Build 
# Feature 1
    1. Conversation Starter and Auto-Hangup Logic
            Bot should start every call with:
            "Hello, how you doing?"
            If no response, repeat this up to 3 times.
            After 3 attempts with no reply (timeout or silence), terminate the call gracefully.

    2. Check if you can Find anything relevant to it in the Docs if you find nothing than we will do it Manually by Using Func:
    def greeting_attempt_tracker():
        """count and check greeting attempts before hanging up"""


# Feature: 2:
    LiveKit provides transcriptions I can see when I run mine project & connect it to the livekit agent playground 
    obviously Gemini processes those transcription 
    I want to display those transcription of mine terminal as well 
    Subscribe to transcription events from LiveKit

# Feature 3:
    1.Disable Interruptions While Bot Speaks
            Set allow_interruption = False in the AI agent configuration.
            Bot should always complete its message before listening for user input.
            for it Check the Latest Docs


# Feature 4:
        VAD should account for user age or speaking pace:
        Elderly users speak slower — set higher post-silence delay before bot responds.
        Identify and modify the VAD timeout config








