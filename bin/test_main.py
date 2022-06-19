import pytest
import main

def test_simpleSieve(capsys):
    main.simpleSieve(5)
    captured = capsys.readouterr()
    assert captured.out == "2 3 "

def test_segmentedSieve(capsys):
    main.segmentedSieve(5)
    captured = capsys.readouterr()
    assert captured.out == "2 "
