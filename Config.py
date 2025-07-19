from livekit import api
from dotenv import load_dotenv
import asyncio
import os
load_dotenv()



async def Recording(room_name):
    lkapi = api.LiveKitAPI()
    req = api.RoomCompositeEgressRequest(
            room_name=room_name,
            audio_only=True,
            file_outputs= [
                api.EncodedFileOutput(
                    filepath=f"{room_name}.mp4",
                    s3 =  api.S3Upload(
                        access_key=os.environ.get("AWS_S3_ACCESS_KEY"),
                        secret=os.environ.get("AWS_S3_SECRET_KEY"),
                        region="ap-southeast-2",
                        bucket="hello-hawk"
                    )
                    
                )
            ]
        )
    print("Starting room egress...")
    egress_info = await lkapi.egress.start_room_composite_egress(req)
    await lkapi.aclose()
    egress_id = getattr(egress_info, "egress_id", None) or getattr(egress_info, "egressId", None)
    print(f"Egress started successfully. Egress ID: {egress_id}")