import sqlite3

from os.path import exists
from typing import Tuple

class DBController:
    def __init__(self, db_file_path) -> None:

        db_file_exist = exists(db_file_path)
        
        self._con = sqlite3.connect(db_file_path)

        # to do: check db integrity

        if not db_file_exist:

            # create db tables

            pass

        pass

    def add_key(self) -> None:
        pass

    
    def check_key(self) -> Tuple[bool, int]:
        pass

    # (allow bot to process messages from chat linked to key)
    def grant_access_by_key(self) -> bool:
        pass

    def grant_access_by_chat_id()