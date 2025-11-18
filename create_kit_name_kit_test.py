import sender_stand_request
import data

def get_new_user_token():
    user_body = data.user_body
    resp_user = sender_stand_request.post_new_user(user_body)
    return resp_user.json()["authToken"]

def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

def positive_assert(kit_body):
    resp_kit = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert resp_kit.status_code == 201
    assert resp_kit.json()["name"] == kit_body["name"]

def negative_assert_code_400(kit_body):
    resp = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert resp.status_code == 400

def test_create_kit_1_letter_in_name_get_success_response():
    kit_body = get_kit_body("a")
    positive_assert(kit_body)

def test_create_kit_511_letter_in_name_get_success_response():
    kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
    positive_assert(kit_body)

def test_create_kit_0_letter_in_name_get_error_response():
    kit_body = get_kit_body("")
    negative_assert_code_400(kit_body)

def test_create_kit_512_letter_in_name_get_error_response():
    kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    negative_assert_code_400(kit_body)

def test_create_kit_english_letter_in_name_get_success_response():
    kit_body = get_kit_body("QWErty")
    positive_assert(kit_body)

def test_create_kit_russian_letter_in_name_get_success_response():
    kit_body = get_kit_body("Мария")
    positive_assert(kit_body)

def test_create_kit_symbols_letter_in_name_get_success_response():
    kit_body = get_kit_body('"№%@,"')
    positive_assert(kit_body)

def test_create_kit_space_letter_in_name_get_success_response():
    kit_body = get_kit_body(" Человек и КО ")
    positive_assert(kit_body)

def test_create_kit_number_letter_in_name_get_success_response():
    kit_body = get_kit_body("123")
    positive_assert(kit_body)

def test_create_kit_blank_letter_in_name_get_error_response():
    kit_body={}
    negative_assert_code_400(kit_body)

def test_create_kit_integer_letter_in_name_get_error_response():
    kit_body = get_kit_body(123)
    negative_assert_code_400(kit_body)