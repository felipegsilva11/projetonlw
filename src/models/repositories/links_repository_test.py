import pytest #type: ignore
import uuid
from links_repository import LinksRepository
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()

link_id = str(uuid.uuid4())
trip_id = str(uuid.uuid4())

def test_registry_link():
    conn = db_connection_handler.get_connection()
    link_repository = LinksRepository(conn)

link_infos = {
    "id": "1234-4321",
    "trip_id": trip_id,
    "link": "somelink.com",
    "title": "Hotel"
}

link_repository.registry_link(link_infos)

def test_find_from_trips():
    conn = db_connection_handler.get_connection()
    link_repository = LinksRepository(conn)
    
    response = link_repository.find_links_from_trip(trip_id)
    print()
    print(response)

