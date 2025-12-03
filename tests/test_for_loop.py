import pytest
from unittest.mock import patch
from for_loop import main


def test_main_vaild(capsys):
    with patch("builtins.input", side_effect=["23.0", "q"]):
        main()
    captured = capsys.readouterr()
    assert "你输入的数字是 23.0" in captured.out
    with patch("builtins.input", side_effect=["2", "q"]):
        main()
    captured = capsys.readouterr()
    assert "你输入的数字是 2" in captured.out


def test_main_invalid(capsys):
    with patch("builtins.input", side_effect=["not num", "q"]):
        main()
    captured = capsys.readouterr()
    assert "请输入数字或 q! " in captured.out


def test_main_exit(capsys):
    with patch("builtins.input", side_effect=["q", "Q"]):
        main()
    captured = capsys.readouterr()
    assert "已退出" in captured.out
