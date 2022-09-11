import pytest


class TestSet:
    def test_clear(self):
        set_test = {1, 2, 3, 4, 5}
        assert set_test == {1, 2, 3, 4, 5}
        set_test.clear()
        assert len(set_test) == 0

    def test_negative_pop(self):
        with pytest.raises(KeyError) as exc:
            set().pop()
        assert str(exc.value) == "'pop from an empty set'"

    @pytest.mark.parametrize(
        ("set_param", "set_equal", "final"),
        [
            ({1, 2, 3, 4, 5}, {1, 2, 3, 4, 5, 6}, False),
            ({}, {}, True),
            ({1, 2}, {2, 1}, True),
            ({1, 2, 2, 3}, {1, 2, 3}, True),
        ],
    )
    def test_equality(self, set_param, set_equal, final):
        res = set_param == set_equal
        assert res == final
