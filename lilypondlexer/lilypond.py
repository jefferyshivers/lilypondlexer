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

    builtins = ('once', 'set', 'override', 'paper', 'context', 'layout',
        'score', 'tempo', 'repeat', 'with')

    grob_interfaces = ('Accidental', 'AccidentalCautionary',
        'AccidentalPlacement',  'AccidentalSuggestion', 'Ambitus',
        'AmbitusAccidental', 'AmbitusLine', 'AmbitusNoteHead', 'Arpeggio',
        'BalloonTextItem', 'BarLine', 'BarNumber', 'BassFigure',
        'BassFigureAlignment', 'BassFigureAlignmentPositioning',
        'BassFigureBracket', 'BassFigureContinuation', 'BassFigureLine', 'Beam',
        'BendAfter', 'BreakAlignGroup', 'BreakAlignment', 'BreathingSign',
        'ChordName',  'Clef', 'ClefModifier', 'ClusterSpanner',
        'ClusterSpannerBeacon',  'CombineTextScript', 'CueClef', 'CueEndClef',
        'Custos', 'DotColumn',  'Dots', 'DoublePercentRepeat',
        'DoublePercentRepeatCounter', 'DoubleRepeatSlash', 'DynamicLineSpanner',
        'DynamicText', 'DynamicTextSpanner', 'Episema', 'Fingering',
        'FingeringColumn', 'Flag', 'FootnoteItem', 'FootnoteSpanner',
        'FretBoard', 'Glissando', 'GraceSpacing', 'GridLine', 'GridPoint',
        'Hairpin', 'HorizontalBracket', 'HorizontalBracketText',
        'InstrumentName', 'InstrumentSwitch', 'KeyCancellation', 'KeySignature',
        'KievanLigature', 'LaissezVibrerTie', 'LaissezVibrerTieColumn',
        'LedgerLineSpanner', 'LeftEdge', 'LigatureBracket', 'LyricExtender',
        'LyricHyphen', 'LyricSpace', 'LyricText', 'MeasureCounter',
        'MeasureGrouping', 'MelodyItem', 'MensuralLigature', 'MetronomeMark',
        'MultiMeasureRest', 'MultiMeasureRestNumber', 'MultiMeasureRestText',
        'NonMusicalPaperColumn', 'NoteCollision', 'NoteColumn', 'NoteHead',
        'NoteName', 'NoteSpacing', 'OttavaBracket', 'PaperColumn',
        'ParenthesesItem', 'PercentRepeat', 'PercentRepeatCounter',
        'PhrasingSlur', 'PianoPedalBracket', 'RehearsalMark', 'RepeatSlash',
        'RepeatTie', 'RepeatTieColumn', 'Rest', 'RestCollision', 'Script',
        'ScriptColumn', 'ScriptRow', 'Slur', 'SostenutoPedal',
        'SostenutoPedalLineSpanner', 'SpacingSpanner', 'SpanBar', 'SpanBarStub',
        'StaffGrouper', 'StaffSpacing', 'StaffSymbol', 'StanzaNumber', 'Stem',
        'StemStub', 'StemTremolo', 'StringNumber', 'StrokeFinger',
        'SustainPedal', 'SustainPedalLineSpanner', 'System', 'SystemStartBar',
        'SystemStartBrace', 'SystemStartBracket', 'SystemStartSquare',
        'TabNoteHead', 'TextScript', 'TextSpanner', 'Tie', 'TieColumn',
        'TimeSignature', 'TrillPitchAccidental', 'TrillPitchGroup',
        'TrillPitchHead', 'TrillSpanner', 'TupletBracket', 'TupletNumber',
        'UnaCordaPedal', 'UnaCordaPedalLineSpanner', 'VaticanaLigature',
        'VerticalAlignment', 'VerticalAxisGroup', 'VoiceFollower',
        'VoltaBracket', 'VoltaBracketSpanner')

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
            (r'\s*#(\'|\`)\(\s*', Punctuation, 'scm-content'),

            # single scheme tokens
            (r'\s*#[^\(\`\'\}]', Punctuation, 'scm-item'),

            # #} to pop root mode & go back into embedded scm-content
            (r'#\}', Punctuation, '#pop'),

            # common notations
            (r'(\#|\/|\{|\}|\(|\)|\[|\])', Punctuation),
            (r'(\.|\,|\'|\`|\-|\_|\|)', Punctuation),
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

        # scheme within parens
        'scm-content': [
            (r'\s+', Text),
            (r';.*$', Comment.Single),
            (r'(\s*|.+?)(\()',
                bygroups(using(SchemeLexer), Punctuation),
                '#push'),
            (r'(.*)(\))(.*|.*$)',
                bygroups(using(SchemeLexer), Punctuation),
                '#pop'),
            # #{ to push embedded LP (root) mode to stack
            (r'#\{', Punctuation, 'root')
        ],

        # single scheme tokens
        'scm-item': [
            (r'(.*)(\s*|\s*$)',
                bygroups(using(SchemeLexer), Punctuation),
                '#pop')
        ]

    }
