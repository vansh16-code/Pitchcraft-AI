from ninja import NinjaAPI
from core.api.pitch import router as pitch_router

api = NinjaAPI()
api.add_router("/pitch/", pitch_router)
