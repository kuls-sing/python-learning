import pytest

@pytest.fixture
def student():
    return {"name": "Kulwant", "grade": 85, "subject": "Python"}

@pytest.fixture
def rectangle():
    return {"width": 10, "height": 5}

def test_student_name(student):
    assert student["name"] == "Kulwant"

def test_student_grade(student):
    assert student["grade"] == 85

def test_student_pass(student):
    assert student["grade"] >= 50
    
def test_width(rectangle):
    assert rectangle["width"] == 10
    
def test_height(rectangle):
    assert rectangle["height"] == 5
    
def test_area(rectangle):
    assert rectangle["width"] * rectangle["height"] == 50