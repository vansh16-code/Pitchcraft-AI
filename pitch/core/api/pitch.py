from ninja import Router
from core.models import Pitch
from core.api.schemas import PitchIn
from django.http import HttpRequest
from typing import cast
import requests
import json

router = Router()

def generate_ai_feedback(pitch_text: str) -> str:
    prompt = (
        "Give constructive, helpful feedback on the following product pitch. "
        "Don't hold back—pinpoint effective areas and areas of improvement. "
        "Make suggestions as if you are an investor yourself, but be respectful.\n\n"
        f"Pitch:\n{pitch_text}"
    )

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "llama2", "prompt": prompt},
            timeout=60,
            stream=True
        )

        feedback = ""
        for line in response.iter_lines():
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
def submit_pitch(request: HttpRequest, data: PitchIn):
    # ✅ Generate feedback first
    feedback = generate_ai_feedback(data.pitch_text)

    # ✅ Then create the Pitch using the feedback
    pitch = cast(Pitch, Pitch.objects.create(
        seller_name=data.seller_name,
        product_name=data.product_name,
        pitch_text=data.pitch_text,
        ai_feedback=feedback
    ))

    return {
        "message": "Pitch submitted successfully",
        "id": pitch.id, #type:ignore
        "ai_feedback": feedback
    }
