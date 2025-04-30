import os

class Config(object):
    BOT_TOKEN = os.environ.get("7717267110:AAGXDF-4RugBLwiB_lzyfD1L5e0LeuLodZQ")
    API_ID = int(os.environ.get("25431437"))
    API_HASH = os.environ.get("3b6235f4375b77e9ce448ebc3111aa50")
    AUTH_USER = os.environ.get('6434880730', '').split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
    HOST = "https://drm-api-six.vercel.app"
    CREDIT = "[꧁ DARK ꧂]"
