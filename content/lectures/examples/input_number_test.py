from .input_number import input_number

def fake_input(msg):
    return 5

def test_input_int(monkeypatch):
    monkeypatch.setattr('builtins.input', fake_input)

    assert input_number('Enter num') == 5


    

def test_input_str(monkeypatch, capsys):
    answers = iter(['none', '50'])
    monkeypatch.setattr('builtins.input', lambda msg: next(answers))

    assert input_number('Enter num') == 50
    captured = capsys.readouterr()
    assert captured.out == 'Your answer must be a number. Try again.\n'