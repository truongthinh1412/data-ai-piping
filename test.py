import unittest
import requests

class TestAPI(unittest.TestCase):

    def setUp(self):
        self.base_url = ""

    def test_get_posts(self):
        url = f"http://localhost:8001/lead/"
        response = requests.post(url, json={})
        self.assertEqual(response.status_code, 200)
        id = response.json()["id"]

        get_url = 'http://localhost:8001/lead/?lead_id=' + id
        get_response = requests.get(get_url)
        self.assertEqual(get_response.status_code, 200)
        # print(get_response.content.decode('utf-8'))
        self.assertEqual(get_response.json()["company_type"], "Startup")
        self.assertEqual(get_response.json()["firstname"], "Julien")

if __name__ == "__main__":
    unittest.main()