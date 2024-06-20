import fputs
import os
import tempfile


def test_copy_data():
    output_fp = os.path.join(tempfile.gettempdir(), "test.txt")
    content = "Good is good!"
    bytes = fputs.fputs(content, output_fp)
    assert bytes > 0

    with open(output_fp, 'r') as f:
        retrieved = f.read()
    assert content == retrieved

