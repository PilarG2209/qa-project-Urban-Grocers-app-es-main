import data
import sender_stand_request



def positive_assert(name):
        user_response =sender_stand_request.post_new_kit_in_new_user(name)
        assert user_response.status_code ==201
        assert user_response.json() ["name"] ==name["name"]

def negative_assert(name):
        response = sender_stand_request.post_new_kit_in_new_user(name)
        assert response.status_code == 400


def test_create_kit_body_1_character_in_name_get_error_response(): #test1
        positive_assert(data.kit_body_1)
def test_create_kit_body_511_character_in_name_get_error_response(): #test2
        positive_assert(data.kit_body_2)
def test_create_kit_body_0_character_in_name_get_error_response(): #test3
        negative_assert(data.kit_body_3)
def test_create_kit_body_512_character_in_name_get_error_response():  # test4
        negative_assert(data.kit_body_4)
def test_create_kit_body_special_character_in_name_get_error_response():  # test5
        positive_assert(data.kit_body_5)
def test_create_kit_body_space_in_name_get_error_response():  # test6
        positive_assert(data.kit_body_6)
def test_create_kit_body_numbers_in_name_get_error_response():  # test7
        positive_assert(data.kit_body_7)
def test_create_kit_body_not_required_in_name_get_error_response():  # test8
        negative_assert(data.kit_body_8)
def test_create_kit_body_different_parament_in_name_get_error_response():  # test9
        negative_assert(data.kit_body_9)









