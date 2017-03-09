from pygments.lexer import RegexLexer
from pygments.token import *

class LilyPondLexer(RegexLexer):
    name = 'LilyPond'
    aliases = ['lilypond', 'lp']
    filename = ['*.ly', '*.ily']

    reserved = ('version', 'override', 'set', 'once', 'context',
                'layout', 'paper', 'score')
                # TODO complete this list, but also determine
                # how extensive it should be.

    tokens = {
        'root': [
            (r' .*\n', Text),
            (r'%\{', Comment.Multiline, 'comment'),
            (r'%.*?$', Comment.Singleline),
            (r'.*\n', Text),
        ],
        'comment': [
            (r'[^%\}]', Comment.Multiline),
            (r'%\{', Comment.Multiline, '#push'),
            (r'%\}', Comment.Multiline, '#pop'),
            (r'[%\}]', Comment.Multiline)
        ]
    }
