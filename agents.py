from livekit.agents import (
    JobContext,
    AutoSubscribe,
    Agent,
    AgentSession,
    cli,
    WorkerOptions,
    RoomInputOptions
)
from dotenv import load_dotenv
from livekit.plugins import google,noise_cancellation
from Prompts import SystemInstructions
from livekit import api
from Config import Recording
import os
import asyncio

load_dotenv()



class Assistant(Agent):
    def __init__(self):
        super().__init__(instructions=SystemInstructions)

async def entrypoint(ctx:JobContext):
    await ctx.connect(auto_subscribe=AutoSubscribe.SUBSCRIBE_ALL)
    await ctx.wait_for_participant()

    try:
        asyncio.run(Recording(ctx.room.name))
    except Exception as e:
        print(f"❌ Sorry an Error Accoured While Setting up the Engress For recording Calls {e}")



    model = google.beta.realtime.RealtimeModel(
        model="gemini-2.5-flash-preview-native-audio-dialog",
        instructions=SystemInstructions,
        voice="Leda",
        temperature=0.8,
        modalities=["Audio"],
        language=""

    )
    session = AgentSession(
        llm=model
    )

    await session.start(
        room=ctx.room,
        agent=Assistant(),
         room_input_options=RoomInputOptions(
            # LiveKit Cloud enhanced noise cancellation
            # - If self-hosting, omit this parameter
            # - For telephony applications, use `BVCTelephony` for best results
            audio_enabled=True,
            video_enabled=False,
            noise_cancellation=noise_cancellation.BVC(),
        ),
    )
    await session.generate_reply(
        instructions="Simply Say 'Hello How are you Doing?' Nothing else",allow_interruptions=False
    )
    
    
    
if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))
    
