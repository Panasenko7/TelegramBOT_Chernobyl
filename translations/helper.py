from translations.translations import TRANSLATIONS, BUTTON_TRANSLATIONS, RADLEVEL_TRANSLATIONS


def get_messagetext_by_language(language, key_word):
    return TRANSLATIONS[key_word][language]


def get_button_text_by_language(language, key_word, button_name):
    return BUTTON_TRANSLATIONS[key_word][button_name][language]


def get_subbutton_text_by_language(language, key_word, button_name):
    return RADLEVEL_TRANSLATIONS[key_word][button_name][language]


def get_menu_values_by_key_word(key_word, button_name):
    return list(BUTTON_TRANSLATIONS[key_word][button_name].values())


def get_rad_lvl_values_by_key_word(key_word, button_name):
    return list(RADLEVEL_TRANSLATIONS[key_word][button_name].values())


def get_rad_lvl_keys():
    from asorc import RAD_LEVELS
    new_list = []
    for keys in RAD_LEVELS.keys():
        for key in keys:
            new_list.append(key)
    return new_list