#!/usr/bin/env python3

from app import app


class TestContract:
    '''Contract route.'''

    def test_found_returns_200_and_data(self):
        '''returns 200 and the contract info when the id exists.'''
        client = app.test_client()
        response = client.get("/contract/1")
        assert response.status_code == 200
        assert "shed" in response.get_json()["contract_information"]

    def test_not_found_returns_404(self):
        '''returns 404 when no contract has that id.'''
        client = app.test_client()
        response = client.get("/contract/999")
        assert response.status_code == 404


class TestCustomer:
    '''Customer route.'''

    def test_found_returns_204_and_no_body(self):
        '''returns 204 with an empty body when the customer exists.'''
        client = app.test_client()
        response = client.get("/customer/bob")
        assert response.status_code == 204
        assert response.data == b""

    def test_found_is_case_insensitive(self):
        '''matches a customer name regardless of case.'''
        client = app.test_client()
        response = client.get("/customer/Bob")
        assert response.status_code == 204

    def test_not_found_returns_404(self):
        '''returns 404 when no customer has that name.'''
        client = app.test_client()
        response = client.get("/customer/nobody")
        assert response.status_code == 404