from ninja import Router
from core.models import Pitch
from core.api.schemas import PitchIn
from django.http import HttpRequest, StreamingHttpResponse
from typing import cast
import httpx
import json
from asgiref.sync import sync_to_async
import asyncio

router = Router()

async def generate_ai_feedback(pitch_text: str) -> str:
    prompt = (
        "Give constructive, helpful feedback on the following product pitch. "
        "Don't hold back—pinpoint effective areas and areas of improvement. "
        "Make suggestions as if you are an investor yourself, but be respectful.\n\n"
        f"Pitch:\n{pitch_text}"
    )

    try:
        async with httpx.AsyncClient(timeout=60) as client:
            async with client.stream(
                "POST",
                "http://localhost:11434/api/generate",
                json={"model": "llama2", "prompt": prompt},
            ) as response:
                feedback = ""
                async for line in response.aiter_lines():
                    if line:
                        try:
                            chunk = json.loads(line)
                            feedback += chunk.get("response", "")
                        except json.JSONDecodeError:
                            continue
                return feedback.strip() or "No meaningful feedback was generated."
    except Exception as e:
        return f"Error calling Ollama: {str(e)}"

async def stream_ai_feedback(pitch_text: str):
    prompt = (
        "Give constructive, helpful feedback on the following product pitch. "
        "Don't hold back—pinpoint effective areas and areas of improvement. "
        "Make suggestions as if you are an investor yourself, but be respectful.\n\n"
        f"Pitch:\n{pitch_text}"
    )
    try:
        async with httpx.AsyncClient(timeout=60) as client:
            async with client.stream(
                "POST",
                "http://localhost:11434/api/generate",
                json={"model": "llama2", "prompt": prompt},
            ) as response:
                async for line in response.aiter_lines():
                    if line:
                        try:
                            chunk = json.loads(line)
                            text = chunk.get("response", "")
                            if text:
                                yield text
                                await asyncio.sleep(0)  # Yield control to event loop
                        except json.JSONDecodeError:
                            continue
    except Exception as e:
        yield f"Error calling Ollama: {str(e)}"

@router.post("/submit/")
async def submit_pitch(request: HttpRequest, data: PitchIn):
    feedback = await generate_ai_feedback(data.pitch_text)
    pitch = await sync_to_async(Pitch.objects.create)(
        seller_name=data.seller_name,
        product_name=data.product_name,
        pitch_text=data.pitch_text,
        ai_feedback=feedback
    )
    return {
        "message": "Pitch submitted successfully",
        "id": pitch.id, #type:ignore
        "ai_feedback": feedback
    }

@router.post("/submit/stream/")
def submit_pitch_stream(request: HttpRequest, data: PitchIn):
    # This is a sync wrapper for the async generator, needed for StreamingHttpResponse
    import threading
    import queue

    q = queue.Queue()
    stop_token = object()

    def run_async():
        async def inner():
            async for chunk in stream_ai_feedback(data.pitch_text):
                q.put(chunk)
            q.put(stop_token)
        asyncio.run(inner())
    threading.Thread(target=run_async, daemon=True).start()

    def generator():
        while True:
            chunk = q.get()
            if chunk is stop_token:
                break
            yield chunk

    return StreamingHttpResponse(generator(), content_type="text/plain")
