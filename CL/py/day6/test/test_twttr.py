from twttr import shorten

def test_shorten():
    assert shorten("hello") == "hll"
    assert shorten("world") == "wrld"
    assert shorten("aeiou") == ""
    assert shorten("AEIOU") == ""
    assert shorten("hElLo") == "hlL"
