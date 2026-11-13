import json
import tempfile
from pathlib import Path
from unittest.mock import patch

from django.test import TestCase

from hello_api.entities.result_dto import ResultDto


class ResultDtoTests(TestCase):
    def test_stores_result_properties(self):
        result = ResultDto(id=1, success=True, message="Completed")

        self.assertEqual(result.id, 1)
        self.assertIs(result.success, True)
        self.assertEqual(result.message, "Completed")


class HelloWorldTests(TestCase):
    def test_homepage_returns_hello_world(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Hello world"})


class JsonPersistenceTests(TestCase):
    def setUp(self):
        self.temp_directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_directory.cleanup)
        self.storage_patch = patch(
            "hello_api.storage.DATA_DIRECTORY",
            Path(self.temp_directory.name)
        )
        self.storage_patch.start()
        self.addCleanup(self.storage_patch.stop)

    def test_user_post_saves_record_to_json(self):
        response = self.client.post(
            "/user",
            data=json.dumps({"id": 1, "name": "Cheems", "account": "cheems01"}),
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 201)
        saved_users = json.loads(
            (Path(self.temp_directory.name) / "users.json").read_text(encoding="utf-8")
        )
        self.assertEqual(
            saved_users,
            [{"id": 1, "name": "Cheems", "account": "cheems01"}]
        )

    def test_animal_post_saves_record_to_json(self):
        response = self.client.post(
            "/animals",
            data=json.dumps({"id": 1, "name": "Cheems", "species": "dog"}),
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 201)
        saved_animals = json.loads(
            (Path(self.temp_directory.name) / "animals.json").read_text(encoding="utf-8")
        )
        self.assertEqual(
            saved_animals,
            [{"id": 1, "name": "Cheems", "species": "dog"}]
        )
