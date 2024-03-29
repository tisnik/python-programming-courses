#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import requests


def expect_ok_response(response):
    assert response is not None
    assert response.ok
    assert response.status_code == 200


def expect_content_type(response, content_type):
    # precteni hlavicek
    headers = response.headers

    # test existence hlavicky
    assert "content-type" in headers

    # kontrola obsahu hlavicky
    assert headers["content-type"] == content_type


def test_post_method_for_existing_endpoint():
    # adresa s testovaci REST API sluzbou
    URL = "http://httpbin.org/post"

    # data posilana serveru
    payload = {"klic": "hodnota", "answer": 42, "question": None, "correct": True}

    # poslani HTTP dotazu typu POST s telem
    response = requests.post(URL, data=payload)

    # zakladni test odpovedi
    expect_ok_response(response)
    expect_content_type(response, "application/json")
