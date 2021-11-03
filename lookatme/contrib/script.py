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

BEG_SCRIPTS = {}
END_SCRIPTS = {}
def transition_slide(next_slide, prev_slide):
    if next_slide > prev_slide:
        if prev_slide in END_SCRIPTS:
            subprocess.run(END_SCRIPTS[prev_slide])
            del END_SCRIPTS[prev_slide]
        if next_slide in BEG_SCRIPTS:
            subprocess.run(BEG_SCRIPTS[next_slide])
            del BEG_SCRIPTS[next_slide]

def render_code(token, body, stack, loop):
    lang = token["lang"] or ""
    slide = token["slide"] or 0
    if   lang == 'beg-script': BEG_SCRIPTS[slide] = shlex.split(token["text"])
    elif lang == 'end-script': END_SCRIPTS[slide] = shlex.split(token["text"])
    else: raise IgnoredByContrib

    return []
