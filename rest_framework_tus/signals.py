# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.dispatch import Signal

receiving = Signal()
received = Signal()
saving = Signal()
saved = Signal()
finished = Signal()
