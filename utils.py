import os

def getOpenFileName(default = None):
    """
    Prompts the user to pick a file name.  If the user doesn't enter a filename,
    returns the default.
    """

    promot = "Enter a file name to load from : "
    if default is not None:
        promot += (" (default: %s" % default)
    promot += " :"

    filename = raw_input(promot)
    if filename == "" and not (default is None) :
        filename = default

    return filename