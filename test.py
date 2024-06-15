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

    def test_upload_download(self):
        upload_url = f"http://localhost:8003/upload/"
        file_content = b"This is a test file."
        files = {"file": ("testfile.txt", file_content, "text/plain")}
        response = requests.post(upload_url, files=files)
        assert response.status_code == 200
        data = response.json()
        assert "file_id" in data
        response = requests.get("http://localhost:8003/download/" + data["file_id"])
        assert response.status_code == 200

if __name__ == "__main__":
    unittest.main()