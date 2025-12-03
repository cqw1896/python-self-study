# pytest测试 tests/test_check_age.py
import pytest
from unittest.mock import patch
from check_age import is_adult, main

# 测试纯函数
def test_is_adult_gt_et_18():
    assert is_adult(18) == "成年人"
    assert is_adult(29) == "成年人"
    assert is_adult(1000) == "成年人"


def test_is_adult_lt_18():
    assert is_adult(12) == "未成年"
    assert is_adult(0) == "未成年"
    assert is_adult(-6) == "未成年"


# 测试 main
# main() 函数是一个 while True, 无限循环。处理完一个输入后，程序会继续等待下一个输入，导致测试卡住。
# 所以应该在输入序列末尾添加 "q" 来退出循环
def test_main_valid_input(capsys):
    with patch("builtins.input", side_effect=["25", "q"]):
        main()
    captured = capsys.readouterr()
    assert "成年人" in captured.out
    with patch("builtins.input", side_effect=["12", "q"]):
        main()
    captured = capsys.readouterr()
    assert "未成年" in captured.out


def test_main_invalid_input(capsys):
    with patch("builtins.input", side_effect=["not a number", "q"]):
        main()
    captured = capsys.readouterr()
    assert "请输入有效数字！" in captured.out


def test_main_exit(capsys):
    with patch("builtins.input", side_effect=["q", "Q"]):
        main()
    captured = capsys.readouterr()
    assert "已退出" in captured.out
