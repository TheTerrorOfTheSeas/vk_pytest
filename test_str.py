import pytest


class TestStr:
    @pytest.mark.parametrize(
        ("proc", "final"),
        [("", []), ("a", ["a"]), ("a b", ["a", "b"]), ("ab c", ["ab", "c"])],
    )
    def test_split(self, proc, final):
        assert proc.split() == final

    def test_lower(self):
        assert "AaBbCcDd12".lower() == "aabbccdd12"

    def test_negative_str_plus_int(self):
        with pytest.raises(TypeError) as exc:
            "123" + 1
        assert str(exc.value) == 'can only concatenate str (not "int") to str'
