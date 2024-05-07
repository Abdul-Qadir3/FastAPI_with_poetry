from project_1 import main

def test_function():
    r  = main.my_function()
    assert r == "hello world"

def test_function_1():
    r  = main.my_function()
    assert r != "Pakistan"