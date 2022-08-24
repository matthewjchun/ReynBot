import os

from discord.ext import commands
from dotenv import load_dotenv
from pymongo import MongoClient
from pathlib import Path

# -------------------- DATABASE SETUP --------------------

load_dotenv()
CONNECTION_URL = os.getenv('CONNECTION_URL')

cluster = MongoClient(CONNECTION_URL)

db = cluster["UserData"]

collection = db["UserData"]

# --------------------------------------------------------


class Reyn(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # ----- CUSTOM PARAMETERS -----
        self.cluster = MongoClient(CONNECTION_URL)
        self.clips = Path("../clips/")

    def get_cluster(self):
        return self.cluster

    def get_clips(self):
        return self.clips
