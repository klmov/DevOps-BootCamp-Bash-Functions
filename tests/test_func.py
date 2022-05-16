from email import message
import pytest
from subprocess import check_output
from datetime import datetime

def run_shell_test(script, *args):

    out = check_output([script] + list(args), universal_newlines=True)
    return out.split("\n")[0]

def run_shell_test_multiline(script, *args):

    out = check_output([script] + list(args), universal_newlines=True)
    return out

def test_pow_1():
    result = run_shell_test('./tests/test_pow.sh', '2', '3')
    assert int(result) == 8

def test_pow_2():
    result = run_shell_test('./tests/test_pow.sh', '2', '5')
    assert int(result) == 32

def test_pow_3():
    result = run_shell_test('./tests/test_pow.sh', '0', '3')
    assert int(result) == 0

def test_pow_4():
    result = run_shell_test('./tests/test_pow.sh', '1', '1')
    assert int(result) == 1

def test_pow_5():
    result = run_shell_test('./tests/test_pow.sh', '10', '5')
    assert int(result) == 100000

def test_shortest_1():
    result = run_shell_test_multiline('./tests/test_shortest.sh', "This", "is", "Bash", "Functions", "Task")
    assert result == "is\n"

def test_shortest_2():
    result = run_shell_test_multiline('./tests/test_shortest.sh', "Test", "is", "short", "do")
    assert result == "is\ndo\n"

def test_shortest_3():
    result = run_shell_test_multiline('./tests/test_shortest.sh', "Java", "Bash", "Python")
    assert result == "Java\nBash\n"

def test_shortest_4():
    result = run_shell_test_multiline('./tests/test_shortest.sh', "1", "2", "42")
    assert result == "1\n2\n"

def test_shortest_5():
    result = run_shell_test_multiline('./tests/test_shortest.sh', "Oh", "this", "is", "a", "test", "!")
    assert result == "a\n!\n"

def test_log_1():

    message = "1"
    now = datetime.now()

    result = run_shell_test('./tests/test_log.sh', message)
    assert result == f"[{now.strftime('%Y-%m-%d %H:%M')}] {message}"

def test_log_2():
    message = "This is a test message"
    now = datetime.now()

    result = run_shell_test('./tests/test_log.sh', f"{message}")
    assert result == f"[{now.strftime('%Y-%m-%d %H:%M')}] {message}"