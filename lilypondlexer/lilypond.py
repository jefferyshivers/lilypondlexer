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
        'score', 'tempo', 'repeat', 'with', 'new')

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

    contexts = ('ChoirStaff', 'ChordNames', 'CueVoice', 'Devnull',
        'DrumStaff', 'DrumVoice', 'Dynamics', 'FiguredBass', 'FretBoards',
        'Global', 'GrandStaff', 'GregorianTranscriptionStaff',
        'GregorianTranscriptionVoice', 'KievanStaff', 'KievanVoice', 'Lyrics',
        'MensuralStaff', 'MensuralVoice', 'NoteNames', 'NullVoice',
        'PetrucciStaff', 'PetrucciVoice', 'PianoStaff', 'RhythmicStaff',
        'Score', 'Staff', 'StaffGroup', 'TabStaff', 'TabVoice', 'VaticanaStaff',
        'VaticanaVoice', 'Voice')

    engravers_and_performers = ('Accidental_engraver', 'Ambitus_engraver',
        'Arpeggio_engraver', 'Auto_beam_engraver', 'Axis_group_engraver',
        'Balloon_engraver', 'Bar_engraver', 'Bar_number_engraver',
        'Beam_collision_engraver', 'Beam_engraver', 'Beam_performer',
        'Bend_engraver', 'Break_align_engraver', 'Breathing_sign_engraver',
        'Chord_name_engraver', 'Chord_tremolo_engraver', 'Clef_engraver',
        'Cluster_spanner_engraver', 'Collision_engraver',
        'Completion_heads_engraver', 'Completion_rest_engraver',
        'Concurrent_hairpin_engraver', 'Control_track_performer',
        'Cue_clef_engraver', 'Custos_engraver', 'Default_bar_line_engraver',
        'Dot_column_engraver', 'Dots_engraver',
        'Double_percent_repeat_engraver', 'Drum_note_performer',
        'Drum_notes_engraver', 'Dynamic_align_engraver', 'Dynamic_engraver',
        'Dynamic_performer', 'Engraver', 'Episema_engraver',
        'Extender_engraver', 'Figured_bass_engraver',
        'Figured_bass_position_engraver', 'Fingering_column_engraver',
        'Fingering_engraver', 'Font_size_engraver', 'Footnote_engraver',
        'Forbid_line_break_engraver', 'Fretboard_engraver',
        'Glissando_engraver', 'Grace_auto_beam_engraver', 'Grace_beam_engraver',
        'Grace_engraver', 'Grace_spacing_engraver', 'Grid_line_span_engraver',
        'Grid_point_engraver', 'Grob_pq_engraver',
        'Horizontal_bracket_engraver', 'Hyphen_engraver',
        'Instrument_name_engraver', 'Instrument_switch_engraver',
        'Keep_alive_together_engraver', 'Key_engraver', 'Key_performer',
        'Kievan_ligature_engraver', 'Laissez_vibrer_engraver',
        'Ledger_line_engraver', 'Ligature_bracket_engraver', 'Lyric_engraver',
        'Lyric_performer', 'Mark_engraver', 'Measure_grouping_engraver',
        'Melody_engraver', 'Mensural_ligature_engraver',
        'Metronome_mark_engraver', 'Midi_control_function_performer',
        'Multi_measure_rest_engraver', 'New_fingering_engraver',
        'Note_head_line_engraver', 'Note_heads_engraver', 'Note_name_engraver',
        'Note_performer', 'Note_spacing_engraver', 'Ottava_spanner_engraver',
        'Output_property_engraver', 'Page_turn_engraver',
        'Paper_column_engraver', 'Parenthesis_engraver',
        'Part_combine_engraver', 'Percent_repeat_engraver',
        'Phrasing_slur_engraver', 'Piano_pedal_align_engraver',
        'Piano_pedal_engraver', 'Piano_pedal_performer',
        'Pitch_squash_engraver', 'Pitched_trill_engraver',
        'Pure_from_neighbor_engraver', 'Repeat_acknowledge_engraver',
        'Repeat_tie_engraver', 'Rest_collision_engraver', 'Rest_engraver',
        'Rhythmic_column_engraver', 'Scheme_engraver', 'Script_column_engraver',
        'Script_engraver', 'Script_row_engraver',
        'Separating_line_group_engraver', 'Slash_repeat_engraver',
        'Slur_engraver', 'Slur_performer', 'Spacing_engraver',
        'Span_arpeggio_engraver', 'Span_bar_engraver', 'Span_bar_stub_engraver',
        'Spanner_break_forbid_engraver', 'Staff_collecting_engraver',
        'Staff_performer', 'Staff_symbol_engraver',
        'Stanza_number_align_engraver', 'Stanza_number_engraver',
        'Stem_engraver', 'System_start_delimiter_engraver',
        'Tab_note_heads_engraver', 'Tab_staff_symbol_engraver',
        'Tab_tie_follow_engraver', 'Tempo_performer', 'Text_engraver',
        'Text_spanner_engraver', 'Tie_engraver', 'Tie_performer',
        'Time_signature_engraver', 'Time_signature_performer',
        'Timing_translator', 'Translator', 'Trill_spanner_engraver',
        'Tuplet_engraver', 'Tweak_engraver',  'Vaticana_ligature_engraver',
        'Vertical_align_engraver', 'Volta_engraver')

    tokens = {

        'root': [
            # whitespace
            (r'\s+', Text),
            # comments
            (r'%\{', Comment.Multiline, 'comment'),
            (r'%.*$', Comment.Single),

            # \functions
            (r'(\\)(%s)(\s+|\\)' % '|'.join(builtins), Name.Builtin),
            (r'(%s)(\s+|\\)' % '|'.join(contexts), Name.Constant),
            (r'\"(%s)\"' % '|'.join(engravers_and_performers), Name.Constant),
            (r'\\[a-zA-Z]*\s*', Name.Function),

            # uncap/capitalized symbols
            (r'[a-zA-Z][a-zA-Z]+\s*', Keyword),
            (r'(\")(.+?)(\")', String.Single),

            # other non-strings
            (r'[a-z][a-z]+', Text),

            # notes (pitches)
            (r'[a-g]+?', Name.Builtin),

            # push scheme mode
            # ... this must stay before string/token below ...
            #(r'\s*#\(\s*', Punctuation, 'scm-content'),
            (r'\s*\#\(', Punctuation, 'scm-content'),
            #(r'\s*#(\'|\`)\(\s*', Punctuation, 'scm-content'),
            (r'\s*\#(\'|\`)(\()', Punctuation, 'scm-content'),

            # single scheme string ...
            #    #"string" <-- "
            (r'\s*\#\"', Punctuation, 'scm-string'),

            # single scheme tokens that aren't strings ...
            #    #anything <-- ends at whitespace
            # ... not followed by open paren
            #(r'\s*#[^\(\`\'\}]', Punctuation, 'scm-item'),
            (r'\s*\#', Punctuation, 'scm-item'),

            # #} to pop root mode & go back into embedded scm-content
            (r'\#\}', Punctuation, '#pop'),

            # everything else
            (r'(\#|\/|\{|\}|\(|\)|\[|\]\<\>)', Punctuation),
            (r'(\.|\,|\'|\`|\-|\_|\|)', Punctuation),
            (r'\d+', Number.Integer),
            (r'\d+\.\d+', Number.Float),
            (r'(\=|\:|\:\:)', Operator)
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
            (r'(\")(.*)(\")', String.Single),
            (r'(\s*|.+?)(\()',
                bygroups(using(SchemeLexer), Punctuation),
                '#push'),
            (r'(.*)(\))(.*|.*$)',
                bygroups(using(SchemeLexer), Punctuation),
                '#pop'),
            # #{ to push embedded LP (root) mode to stack
            (r'\#\{', Punctuation, 'root')
        ],

        # single scheme string ...
        #    #"string" <-- "
        'scm-string': [
            (r'(.*)(\"|\"$)',
                bygroups(using(SchemeLexer), Punctuation),
                '#pop')
        ],

        # single scheme tokens that aren't strings ...
        #    #anything <-- ends at whitespace
        'scm-item': [
            (r'(.*)(\s*|\s*$)',
                bygroups(using(SchemeLexer), Punctuation),
                '#pop')
        ]

    }
