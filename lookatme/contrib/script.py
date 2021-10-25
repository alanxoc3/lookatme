"""
Allows scripts to be run but not displayed.
"""

import subprocess
import shlex
import urwid
import yaml

import lookatme.render
from lookatme.exceptions import IgnoredByContrib
import lookatme.config

SCRIPTS = {}
def transition_slide(next_slide, prev_slide):
    if next_slide > prev_slide and next_slide in SCRIPTS:
        subprocess.run(SCRIPTS[next_slide])

def render_code(token, body, stack, loop):
    lang = token["lang"] or ""
    slide = token["slide"] or 0
    if lang == 'script': SCRIPTS[slide] = shlex.split(token["text"])
    else: raise IgnoredByContrib

    return []
