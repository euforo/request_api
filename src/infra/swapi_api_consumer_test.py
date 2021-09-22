from .swapi_api_consumer import SwapiApiConsumer


def test_get_starships(requests_mock):
    '''testando get_starships.'''
    requests_mock.get('https://swapi.dev/api/starships/', status_code = 200, json = {'alguma': 'coisa'})
    swapi_api_consumer = SwapiApiConsumer()
    response = swapi_api_consumer.get_starships(page=1)

    print(response)