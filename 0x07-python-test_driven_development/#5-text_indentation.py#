#!/usr/bin/python3
def text_indentation(text):
    """ Function that indent string

        Args:
           text: Text to indent

        Returns:
           Nothing - Just print a indent text
    """
    if type(text) is not str:
        raise TypeError ("text must be a string")
    text1 = text.replace('. ', ".\n\n")
    text1 = text1.replace('? ', "?\n\n")
    text1 = text1.replace(': ', ":\n\n")
    text1 = text1.strip()
    print("{:s}".format(text1), end="")
