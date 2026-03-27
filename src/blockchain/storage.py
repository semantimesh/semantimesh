import json
import hashlib
from datetime import datetime
from typing import Dict, List, Any

class BlockchainStorage:
    def __init__(self, storage_path: str = "blockchain_data"):
        self.storage_path = storage_path
        self.chain = []
        self.
