#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week-1 Assignment1, Part 2 - Simple Class"""

class Book:
    def __init__( exm, author = '', title = '' ):
        exm.a = author
        exm.t = title
        return

    def display(exm):
        """This fuction simply rints out a string representing the book"""
        print "%s, written by %s" % (exm.a, exm.t)
        return

book1 = Book('Of Mice and Men', 'John Steinbeck')
book2 = Book('To Kill a Mockingbird', 'Harper Lee')

book1.display()
book2.display()
