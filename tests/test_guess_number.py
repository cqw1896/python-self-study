import pytest
from unittest.mock import patch, MagicMock
import random
from guess_number import guess_number_game


@pytest.fixture
def mock_random():
    with patch("random.randint") as mock_rand:
        mock_rand.return_value = 42  # 固定随机数以便测试
        yield mock_rand


def test_guess_correct_number(mock_random, capsys):
    # 模拟用户输入正确数字
    with patch("builtins.input", return_value="42"):
        guess_number_game()
    captured = capsys.readouterr()
    assert "恭喜！你用了 1 次猜中数字 42！" in captured.out


def test_guess_lower_number(mock_random, capsys):
    # 模拟用户先输入较小数字，再输入正确数字
    with patch("builtins.input", side_effect=["30", "42"]):
        guess_number_game()
    captured = capsys.readouterr()
    assert "太小了，再试试！" in captured.out
    assert "恭喜！你用了 2 次猜中数字 42！" in captured.out


def test_guess_higher_number(mock_random, capsys):
    # 模拟用户先输入较大数字，再输入正确数字
    with patch("builtins.input", side_effect=["50", "42"]):
        guess_number_game()
    captured = capsys.readouterr()
    assert "太大了，再试试！" in captured.out
    assert "恭喜！你用了 2 次猜中数字 42！" in captured.out


def test_quit_game(mock_random, capsys):
    # 测试退出游戏功能
    with patch("builtins.input", return_value="q"):
        guess_number_game()
    captured = capsys.readouterr()
    assert "已退出，游戏结束。" in captured.out


def test_invalid_input(mock_random, capsys):
    # 测试无效输入处理
    with patch("builtins.input", side_effect=["abc", "42"]):
        guess_number_game()
    captured = capsys.readouterr()
    assert "输入无效，请输入整数或 q。" in captured.out
    assert "恭喜！你用了 1 次猜中数字 42！" in captured.out
