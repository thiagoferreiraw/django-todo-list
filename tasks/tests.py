from django.test import TestCase
from rest_framework import status

from .models import Task


class TasksTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        Task.objects.bulk_create(
            [
                Task(title="Walk the dogs"),
                Task(title="Build spaceship"),
                Task(title="Take out the trash", status=True),
            ]
        )

    def test_task_list(self):
        response = self.client.get("/tasks/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(
            data,
            {
                "next": None,
                "previous": None,
                "results": [
                    {"id": 3, "title": "Take out the trash", "status": True},
                    {"id": 2, "title": "Build spaceship", "status": False},
                    {"id": 1, "title": "Walk the dogs", "status": False},
                ],
            },
            data,
        )

    def test_task_retrieve(self):
        response = self.client.get("/tasks/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(), {"id": 1, "status": False, "title": "Walk the dogs"}
        )

    def test_task_create(self):
        response = self.client.post(
            "/tasks/", data={"status": False, "title": "Seize the means of production"}
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            response.json(),
            {"id": 4, "status": False, "title": "Seize the means of production"},
        )

    def test_task_update(self):
        response = self.client.put(
            "/tasks/1/",
            data={"status": False, "title": "Walk the dogs at night"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {"id": 1, "status": False, "title": "Walk the dogs at night"},
        )

    def test_task_partial_update(self):
        response = self.client.patch(
            "/tasks/1/", data={"status": True}, content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(), {"id": 1, "status": True, "title": "Walk the dogs"}
        )
