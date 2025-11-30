import pytest
from unittest.mock import patch
from variables_1 import variables, main


# 1. 测试纯函数 variables_1
def test_variables_default():
    assert variables("张三", 25) == "Hello, 张三, you are 25 years old."


def test_variables_negative_age():
    assert variables("李四", -5) == "Hello, 李四, you are -5 years old."


def test_variables_zero_age():
    assert variables("王五", 0) == "Hello, 王五, you are 0 years old."


# 2. 测试 main() 需要模拟 I/O ,但逻辑已最小化
def test_main_valid_input(capsys):
    with patch("builtins.input", side_effect=["王五", "30"]):
        main()
    captured = capsys.readouterr()
    assert "Hello, 王五, you are 30 years old." in captured.out


def test_main_invalid_age(capsys):
    with patch("builtins.input", side_effect=["赵六", "not_a_number"]):
        main()
    captured = capsys.readouterr()
    assert "年龄必须是数字!" in captured.out
