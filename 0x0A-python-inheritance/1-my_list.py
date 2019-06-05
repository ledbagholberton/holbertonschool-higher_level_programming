#!/usr/bin/python3
""" My_list               """


class MyList(list):
    """ MyList Class """
    def print_sorted(self):
        """ Return print  sortedd list
        Parameters:
        self
        Return:
        No return
        """
        print(sorted(self))
