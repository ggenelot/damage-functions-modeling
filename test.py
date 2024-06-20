def random_function(kinds=None):
    """
    Return a list of random ingredients as strings.

    :param kinds: Optional "kind" of ingredients.
    :type kinds: list[str] or None
    :raise lumache.InvalidKindError: If the kind is invalid.
    :return: The ingredients list.
    :rtype: list[str]
    """
    return ["shells", "gorgonzola", "parsley"]