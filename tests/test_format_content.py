from utils.format_content import format_content

def test_format_content_no_content():
  content = []
  assert format_content(content) == []

def test_format_content_no_argument():
  assert format_content() == []

def test_format_content_with_content():
  content = ["Hello\n", "\n", "World"]
  assert format_content(content) == ["Hello", "\n", "World"]