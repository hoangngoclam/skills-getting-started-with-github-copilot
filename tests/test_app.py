import copy

import pytest
from fastapi.testclient import TestClient

from src import app as app_module


client = TestClient(app_module.app)


@pytest.fixture(autouse=True)
def reset_activities():
    """Backup and restore the in-memory activities to keep tests isolated."""
    original = copy.deepcopy(app_module.activities)
    yield
    app_module.activities.clear()
    app_module.activities.update(original)


def test_get_activities():
    resp = client.get("/activities")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, dict)
    # Basic expected activity
    assert "Chess Club" in data


def test_signup_and_unregister():
    activity_name = "Basketball Team"
    email = "tester@example.com"

    # Ensure clean start
    assert email not in app_module.activities[activity_name]["participants"]

    # Sign up
    resp = client.post(f"/activities/{activity_name}/signup?email={email}")
    assert resp.status_code == 200
    assert email in app_module.activities[activity_name]["participants"]

    # Unregister
    resp = client.delete(f"/activities/{activity_name}/participants?email={email}")
    assert resp.status_code == 200
    assert email not in app_module.activities[activity_name]["participants"]


def test_unregister_nonexistent_returns_error():
    activity_name = "Soccer Club"
    email = "nonexistent@example.com"
    # make sure it's not signed up
    if email in app_module.activities[activity_name]["participants"]:
        app_module.activities[activity_name]["participants"].remove(email)

    resp = client.delete(f"/activities/{activity_name}/participants?email={email}")
    assert resp.status_code == 400
    data = resp.json()
    assert "Student not signed up" in data.get("detail", "")
