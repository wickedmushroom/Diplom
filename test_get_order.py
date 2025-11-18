# Егор Казаков, 37-я когорта — Финальный проект. Инженер по тестированию плюс

import data
import configuration
import sender_stand_request

def test_create_and_get_order():
    create_response = sender_stand_request.create_order()
    track_number = create_response.json()["track"]
    get_response = sender_stand_request.get_order(track_number)
    assert get_response.status_code == 200

