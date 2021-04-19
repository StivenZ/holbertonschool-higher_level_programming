#!/usr/bin/python3
"""Use of magic functions in python: eq and ne
"""

class MyInt(int):
    """Uses magic functions to invert equality valence
    """
    def __init__(self, integer):
        self.integer = integer
    
    def __eq__(self, other):
        """Called when equality used"""
        if self.integer == other:
            return False
        else:
            return True
    
    def __ne__(self, other):
        """Called when inequality used"""
        if self.integer == other:
            return True
        else:
            return False
