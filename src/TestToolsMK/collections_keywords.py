#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2015 Cutting Edge QA


class CollectionsKeywordsExtension(object):
    def __int__(self, **kwargs):
        super(CollectionsKeywordsExtension, self).__int__(**kwargs)

    @staticmethod
    def create_dictionary_from_list(table):
        """

        :rtype : dict
        """
        return dict((x, 0) for x in table)

    @staticmethod
    def create_dictionary_from_two_lists(keys, values):
        """

        :rtype : dict
        """
        return dict(zip(keys, values))
