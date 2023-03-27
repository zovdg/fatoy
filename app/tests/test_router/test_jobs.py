import json
from fastapi import status


def test_create_job(client):
    data = {
        "title": "SDE super",
        "company": "doogle",
        "company_url": "www.doogle.com",
        "location": "USA,NY",
        "description": "python",
        "date_posted": "2022-03-20",
    }
    response = client.post(url="/jobs/create-job/", data=json.dumps(data))
    assert response.status_code == 200
    assert response.json()["company"] == "doogle"
    assert response.json()["description"] == "python"


def test_read_job(client):  # new test
    data = {
        "title": "SDE super",
        "company": "doogle",
        "company_url": "www.doogle.com",
        "location": "USA,NY",
        "description": "python",
        "date_posted": "2022-03-20",
    }
    _response = client.post(url="/jobs/create-job/", data=json.dumps(data))
    response = client.get(url="/jobs/get/1/")
    assert response.status_code == 200
    assert response.json()["title"] == "SDE super"


def test_read_all_jobs(client):
    data = {
        "title": "SDE super",
        "company": "doogle",
        "company_url": "www.doogle.com",
        "location": "USA,NY",
        "description": "python",
        "date_posted": "2022-03-20",
    }
    client.post(url="/jobs/create-job/", data=json.dumps(data))
    client.post(url="/jobs/create-job/", data=json.dumps(data))

    response = client.get(url="/jobs/all/")
    assert response.status_code == 200
    assert response.json()[0]
    assert response.json()[1]


def test_update_a_job(client):
    data = {
        "title": "New Job super",
        "company": "doogle",
        "company_url": "www.doogle.com",
        "location": "USA,NY",
        "description": "fastapi",
        "date_posted": "2022-03-20",
    }
    client.post(url="/jobs/create-job/", data=json.dumps(data))
    data["title"] = "test new title"
    response = client.put(url="/jobs/update/1", data=json.dumps(data))
    assert response.json()["msg"] == "Successfully updated data."


def test_delete_a_job(client):
    data = {
        "title": "New Job super",
        "company": "doogle",
        "company_url": "www.doogle.com",
        "location": "USA,NY",
        "description": "fastapi",
        "date_posted": "2022-03-20",
    }
    client.post(url="/jobs/create-job/", data=json.dumps(data))
    msg = client.delete(url="/jobs/delete/1")
    response = client.get(url="/jobs/get/1/")
    assert response.status_code == status.HTTP_404_NOT_FOUND
