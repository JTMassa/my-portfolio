import pytest
from app import app

def test_app_exists():
    """Test that the app exist"""
    assert app is not None

    def test_home_page():
        """Test that the home page enpoint"""
        with app.test_client() as client:
             response = client.get('/')
             assert response.status_code == 200
       