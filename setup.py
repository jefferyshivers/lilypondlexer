from setuptools import setup, find_packages

setup (
  name='lilypondlexer',
  packages=find_packages(),
  entry_points =
  """
  [pygments.lexers]
  lilypondlexer = lilypondlexer.lilypond:LilyPondLexer
  """,
  # append to string above to include other lexers, like:
  # lilyfoolexer = lilypondlexer.lilypond:LilyFooLexer
  # where alias = <sub dir>.<lexer file>:<unique class name>
)
