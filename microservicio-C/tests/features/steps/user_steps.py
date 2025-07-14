from behave import given, when, then
import requests


@given('el servicio esta en linea')
def step_service_online(context):
    response = requests.get('http://localhost:8000/ping')
    assert response.status_code == 200


@when('hago un GET a /action/{item_id}')
def step_get_action(context, item_id):
    context.response = requests.get(f'http://localhost:8000/welcome/{item_id}')


@then('el resultado debe incluir "{expected_text}"')
def step_result_contains(context, expected_text):
    assert expected_text in context.response.text
