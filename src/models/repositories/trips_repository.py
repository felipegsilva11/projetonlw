from typing import Dict
from sqlite3 import Connection

class TripsRepository:
    def __init__(self, conn: Connection)-> None:
        self.__conn = conn
        
    def create_trip(self, trips_infos: Dict) ->
        cursor = self.__conn.cursor()
        cursor.execute(
            ' ' '
                INSET INTO trips
                    (id, destinatio, start_date, end_date, owner_name, owner_email)
                VALUES
                    (?,?,?,?,?,?)     
            ' ' ' , (
                trips_infos["id"],
                trips_infos["destinatio"],
                trips_infos["start_date"],
                trips_infos["end_date"],
                trips_infos["owner_name"],
                trips_infos["owner_email"],
            )
        )
        self.__conn.commit()