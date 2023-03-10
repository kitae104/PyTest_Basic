import pytest

@pytest.fixture
def square_10():
    return 10 * 10

def test_square(square_10):
    # fixture로 명명한 square_10은 변수처럼 사용
    assert square_10 == 100
    assert square_10 == 121