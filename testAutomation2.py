import pytest
import requests

BASE_URL = "http://127.0.0.1:8000"

# Define test cases for parameterized testing
testcases = [
    ("/add", 10, 5, 15, "Addition of 10 and 5"),
    ("/subtract", 10, 5, 5, "Subtraction of 10 and 5"),
    ("/multiply", 10, 5, 50, "Multiplication of 10 and 5"),
    ("/add", -3, 3, 0, "Addition of -3 and 3"),
    ("/multiply", 0, 5, 0, "Multiplication by zero"),
]

@pytest.mark.parametrize("endpoint, num1, num2, expected, description", testcases)
def test_api(endpoint, num1, num2, expected, description):
    """
    Parameterized test for API endpoints.
    """
    url = f"{BASE_URL}{endpoint}/{num1}/{num2}"
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json()["result"] == expected, f"{description} FAILED! Expected {expected}, got {response.json()['result']}"
    print(f"{description} PASSED ✅")

if __name__ == "__main__":
    pytest.main()
