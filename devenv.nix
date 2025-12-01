{
  pkgs,
  lib,
  config,
  inputs,
  ...
}:

{
  # https://devenv.sh/packages/
  packages = [
    pkgs.git
  ];

  # https://devenv.sh/languages/
  languages.python.enable = true;
  languages.python.version = "3.14";
  languages.python.uv.enable = true;

  # https://devenv.sh/scripts/
  scripts.aoc.exec = ''
    uv run src/main.py "$@"
  '';

  # https://devenv.sh/integrations/dotenv/
  dotenv.enable = true;

  # See full reference at https://devenv.sh/reference/options/
}
