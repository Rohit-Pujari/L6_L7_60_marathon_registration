"""Expanded tests targeting complete executable line coverage."""
import pytest
from marathon_registration import entry_fee, start_wave, finisher_status


@pytest.mark.parametrize(
    ("race", "age", "early", "shirt", "expected"),
    [
        ("5k", 12, False, False, 500),
        ("10k", 30, False, False, 800),
        ("half", 18, True, False, 900),
        ("full", 64, False, True, 2100),
        ("5k", 65, False, False, 250),
        ("10k", 65, True, True, 600),
    ],
)
def test_entry_fee_valid_combinations(race, age, early, shirt, expected):
    assert entry_fee(race, age, early, shirt) == expected


@pytest.mark.parametrize(
    ("race", "age", "message"),
    [
        ("ultra", 30, "unknown race"),
        ("5k", 11, "too young"),
        ("half", 17, "too young for this distance"),
        ("full", 17, "too young for this distance"),
    ],
)
def test_entry_fee_rejections(race, age, message):
    with pytest.raises(ValueError, match=message):
        entry_fee(race, age, False, False)


@pytest.mark.parametrize(
    ("best_time", "race", "expected"),
    [
        (None, "full", "D"),
        (180, "full", "A"),
        (240, "full", "B"),
        (241, "full", "C"),
        (90, "10k", "A"),
        (120, "10k", "B"),
        (121, "10k", "C"),
    ],
)
def test_start_wave_categories(best_time, race, expected):
    assert start_wave(best_time, race) == expected


@pytest.mark.parametrize(
    ("elapsed", "race", "missed", "expected"),
    [
        (360, "full", 0, "finisher"),
        (361, "full", 0, "DNF"),
        (180, "half", 0, "finisher"),
        (181, "half", 0, "DNF"),
        (90, "5k", 0, "finisher"),
        (91, "10k", 0, "DNF"),
        (1, "full", 1, "DSQ"),
    ],
)
def test_finisher_status_boundaries(elapsed, race, missed, expected):
    assert finisher_status(elapsed, race, missed) == expected
