"""Tests for both outcomes of each decision (branch coverage)."""
import pytest
from marathon_registration import entry_fee, start_wave, finisher_status


# entry_fee: known/unknown race, age below/above minimum, youth distance
# restriction, early-bird toggle, senior toggle and shirt toggle.
def test_unknown_race_branch():
    with pytest.raises(ValueError, match="unknown race"):
        entry_fee("ultra", 30, False, False)


def test_under_minimum_age_branch():
    with pytest.raises(ValueError, match="too young"):
        entry_fee("5k", 11, False, False)


@pytest.mark.parametrize("race", ["half", "full"])
def test_under_18_distance_restriction(race):
    with pytest.raises(ValueError, match="too young for this distance"):
        entry_fee(race, 17, False, False)


def test_early_bird_yes_and_no():
    assert entry_fee("10k", 30, True, False) == 600
    assert entry_fee("10k", 30, False, False) == 800


def test_senior_yes_and_no():
    assert entry_fee("5k", 65, False, False) == 250
    assert entry_fee("5k", 64, False, False) == 500


def test_tshirt_yes_and_no():
    assert entry_fee("5k", 30, False, True) == 800
    assert entry_fee("5k", 30, False, False) == 500


# start_wave: no time/time, full/other race, A/B/C outcomes.
def test_start_wave_missing_time():
    assert start_wave(None, "10k") == "D"


def test_start_wave_full_and_non_full_cutoffs():
    assert start_wave(180, "full") == "A"
    assert start_wave(90, "10k") == "A"
    assert start_wave(240, "full") == "B"
    assert start_wave(120, "10k") == "B"
    assert start_wave(241, "full") == "C"
    assert start_wave(121, "10k") == "C"


# finisher_status: disqualification and non-disqualification;
# each distance-specific time-limit branch and both outcomes.
def test_checkpoint_disqualification_precedes_time_check():
    assert finisher_status(1, "full", 1) == "DSQ"


def test_full_race_finisher_and_dnf():
    assert finisher_status(360, "full", 0) == "finisher"
    assert finisher_status(361, "full", 0) == "DNF"


def test_half_race_finisher_and_dnf():
    assert finisher_status(180, "half", 0) == "finisher"
    assert finisher_status(181, "half", 0) == "DNF"


def test_other_race_finisher_and_dnf():
    assert finisher_status(90, "5k", 0) == "finisher"
    assert finisher_status(91, "10k", 0) == "DNF"
