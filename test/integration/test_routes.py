import unittest

from src import app


class TestRoutes(unittest.TestCase):
    def setUp(self) -> None:
        self.app = app.test_client()

    def test_should_get_all_planets(self):
        response = self.app.get('/planet')

        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response)

    def test_should_get_planet_by_name(self):
        response = self.app.get(f'/planet/name/{"teste"}')

        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response)

    def test_should_get_planet_by_id(self):
        response = self.app.get(f'/planet/name/{"654986613489"}')

        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response)

    def test_should_create_planet(self):
        body = {
            'name': 'Alderaan',
            'climate': 'teste',
            'terrain': 'teste'
        }

        response = self.app.post('/planet', json=body)

        self.assertEqual(response.status_code, 201)
        self.assertIsNotNone(response)

    def test_should_update_planet(self):
        body = {
            'climate': 'temperate'
        }

        response = self.app.patch(f'/planet?name={"Alderaan"}', json=body)

        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response)

    def test_should_delete_planet(self):
        response = self.app.delete(f'/planet?name={"Alderaan"}')

        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response)


if __name__ == '__main__':
    unittest.main()
