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

    builtins = ('once', 'set', 'override', 'paper', 'context', 'layout', 'score',
                'tempo', 'repeat', 'with')

    tokens = {

        'root': [
            # whitespace
            (r'\s+', Text),
            # comments
            (r'%\{', Comment.Multiline, 'comment'),
            (r'%.*$', Comment.Single),

            # \functions
            (r'(\\)(%s)(\s+|\\)' % '|'.join(builtins), Name.Builtin),
            (r'\\[a-zA-Z]*\s*', Name.Function),

            # uncap/capitalized symbols
            (r'[a-zA-Z][a-zA-Z]+\s*', Keyword),

            # other non-strings
            (r'[a-z][a-z]+', Text),

            # notes (pitches)
            (r'[a-g]+?', Name.Builtin),

            # push scheme mode
            (r'\s*#\(\s*', Punctuation, 'scm-content'),
            # scheme quotes
            #(r'\s+#(\'|\`)', Punctuation),

            # common notations
            (r'(\#|\/|\{|\}|\(|\)|\[|\])', Punctuation),
            (r'(\.|\,|\'|\`|\-|\|)', Punctuation),
            (r'\d+', Number.Integer),
            (r'\d+\.\d+', Number.Float),
            (r'(\=|\:|\:\:)', Operator),
            (r'(\")(.+?)(\")', String.Single)
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
