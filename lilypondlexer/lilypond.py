from pygments.lexer import Lexer, RegexLexer, bygroups, do_insertions, \
    default, include, using

from pygments.token import *

from pygments.lexers.lisp import SchemeLexer

# from pygments import unistring as uni

#__all__ = ['LilyPondLexer', 'LilySchemeLexer']

class LilyPondLexer(RegexLexer):
    name = 'LilyPond'
    aliases = ['lilypond', 'lp']
    filename = ['*.ly', '*.ily']

    builtins = ('set', 'override')

    tokens = {

        'root': [
            # whitespace
            (r'\s+', Text),
            # comments
            (r'%\{', Comment.Multiline, 'comment'),
            (r'%.*$', Comment.Single),
            (r'\\[a-zA-Z]*\s*', Name.Function),

            # notes (pitches)
            (r'[a-g][^a-zA-Z]\s*', Name.Builtin),

            # symbols
            # TODO

            # other non-strings
            (r'\s*[a-zA-Z]+\s*', Keyword),

            # push scheme mode
            (r'\s*#\(\s*', Punctuation, 'scm-content'),
            # scheme quotes
            (r'\s*#\'', Punctuation),

            # common notations
            (r'(\/|\{|\}|\(|\)|\[|\])', Punctuation),
            (r'(\.|\,|\'|\-|\|)', Punctuation),
            (r'\s*[a-g]\s*', Keyword),
            (r'\d+', Number.Integer),
            (r'(\=|\:|\:\:)', Operator),
            (r'(\")(.+?)(\")', String)
        ],

        'comment': [
            (r'[^%\}]', Comment.Multiline),
            (r'%\{', Comment.Multiline, '#push'),
            (r'%\}', Comment.Multiline, '#pop'),
            (r'[%\}]', Comment.Multiline)
        ],

        'scm-content': [
            (r'(\s*|.+?)(\()',
                bygroups(using(SchemeLexer), Punctuation),
                '#push'),
            (r'(.*)(\))(.*|.*$)',
                bygroups(using(SchemeLexer), Punctuation),
                '#pop'),

            # TODO add #{ and #} tokens to push/pop embedded LP (root) mode to stack

        ]

    }
