import pytest
from unittest.mock import patch
from io import StringIO
import sys
from variables import main


def test_valid_input(capsys):
    """测试正常输入：姓名和有效年龄"""
    # 模拟 input 的返回值
    with patch("builtins.input", side_effect=["张三", "25"]):
        main()
    # 捕获 print 输出
    captured = capsys.readouterr()
    assert "Hello, 张三, you are 25 years old."


def test_invalid_age(capsys):
    """测试年龄输入非数字的情况"""
    with patch("builtins.input", side_effect=["李四", "abc"]):
        main()
    captured = capsys.readouterr()
    assert "年龄必须是数字!" in captured.out


def test_negative_age(capsys):
    """测试负数年龄（合法整数，程序应接受）"""
    with patch("builtins.input", side_effect=["王五", "-5"]):
        main()
    captured = capsys.readouterr()
    assert "Hello, 王五, you are -5 years old." in captured.out
