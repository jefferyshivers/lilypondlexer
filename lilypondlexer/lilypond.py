from pygments.lexer import Lexer, RegexLexer, bygroups, do_insertions, \
    default, include, using

from pygments.token import *

from pygments.lexers.lisp import SchemeLexer

import re

# from pygments import unistring as uni

#__all__ = ['LilyPondLexer', 'LilySchemeLexer']

# line_re = re.compile('.*?\n')

class LilyPondLexer(RegexLexer):
    name = 'LilyPond'
    aliases = ['lilypond', 'lp']
    filename = ['*.ly', '*.ily']

    flags = re.IGNORECASE | re.DOTALL
    tokens = {
        'root': [
            # whitespace
            (r'\s+', Text),
            # comments
            (r'%\{', Comment.Multiline, 'comment'),
            (r'%.*?$', Comment.Singleline),
            #(r'\\[a-zA-Z]*(\{|\\|\s*)', Name.Function),
            (r'\\[a-zA-Z]*', Name.Function),
            # push scheme mode
            (r'\s*#\(\s*', Punctuation, 'scm-content'),
            (r'(\{|\}|\(|\)|\[|\])', Punctuation)
        ],
        'comment': [
            (r'[^%\}]', Comment.Multiline),
            (r'%\{', Comment.Multiline, '#push'),
            (r'%\}', Comment.Multiline, '#pop'),
            (r'[%\}]', Comment.Multiline)
        ],
        'scm-content': [
            (r'(.+?)(\()',
                bygroups(using(SchemeLexer), Punctuation),
                '#push'),
            (r'(.+?)(\)\s*)',
                bygroups(using(SchemeLexer), Punctuation),
                '#pop'),
        # TODO add #{ and #} tokens to push/pop embedded LP (root) mode to stack
        ]
    }
