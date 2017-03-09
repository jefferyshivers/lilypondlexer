from setuptools import setup, find_packages

setup (
  name='lilypondlexer',
  packages=find_packages(),
  entry_points =
  """
  [pygments.lexers]
  lilypondlexer = lilypondlexer.lilypond:LilyPondLexer
  """,
)
