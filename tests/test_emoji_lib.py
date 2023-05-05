from comrade.lib.standalone.emoji_converter import string_to_regional_indicator, regional_indicator_string_to_string


def test_emoji_fwd_conversion():
    test_s = "apple"
    expected_s = "🇦🇵🇵🇱🇪"

    assert string_to_regional_indicator(test_s) == expected_s


def test_emoji_rev_conversion():
    test_s = "🇦🇵🇵🇱🇪"
    expected_s = "apple"

    assert regional_indicator_string_to_string(test_s) == expected_s
