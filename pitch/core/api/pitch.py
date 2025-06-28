from ninja import Router
from core.models import Pitch
from core.api.schemas import PitchIn
from django.http import HttpRequest
from typing import cast
import httpx
import json
from asgiref.sync import sync_to_async

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
