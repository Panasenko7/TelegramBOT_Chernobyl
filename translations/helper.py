from translations.translations import TRANSLATIONS, BUTTON_TRANSLATIONS


def get_text_by_language(language, key_word):
    return TRANSLATIONS[key_word][language]


def get_button_text_by_language(language, key_word, button_name):
    return BUTTON_TRANSLATIONS[key_word][button_name][language]


def get_all_values_by_key_word(key_word, button_name):
    return list(BUTTON_TRANSLATIONS[key_word][button_name].values())

