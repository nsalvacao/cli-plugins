# perl -- Complete Command Reference

## Global Flags

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `-0` | `-0` | string | specify record separator (\0, if no argument) |
| `-C` | `-C` | string | enables the listed Unicode features |
| `-D` | `-D` | string | set debugging flags (argument is a bit mask or alphabets) |
| `-E` | `-E` | string | like -e, but enables all optional features |
| `-F` | `-F` | string | split() pattern for -a switch (//'s are optional) |
| `-Idirectory` | `-Idirectory` | bool | specify @INC/#include directory (several -I's allowed) |
| `-S` | `-S` | bool | look for programfile using PATH environment variable |
| `-T` | `-T` | bool | enable tainting checks |
| `-U` | `-U` | bool | allow unsafe operations |
| `-V[:configvar]` | `-V[:configvar]` | string | print configuration summary (or a single Config.pm variable) |
| `-W` | `-W` | bool | enable all warnings |
| `-X` | `-X` | bool | disable all warnings |
| `-a` | `-a` | bool | autosplit mode with -n or -p (splits $_ into @F) |
| `-c` | `-c` | bool | check syntax only (runs BEGIN and CHECK blocks) |
| `-d[t][:MOD]` | `-d[t][:MOD]` | string | run program under debugger or module Devel::MOD |
| `-e` | `-e` | string | one line of program (several -e's allowed, omit programfile) |
| `-f` | `-f` | bool | don't do $sitelib/sitecustomize.pl at startup |
| `-g` | `-g` | bool | read all input in one go (slurp), rather than line-by-line (alias for -0777) |
| `-i` | `-i` | string | edit <> files in place (makes backup if extension supplied) |
| `-l` | `-l` | string | enable line ending processing, specifies line terminator |
| `-n` | `-n` | bool | assume "while (<>) { ... }" loop around program |
| `-p` | `-p` | bool | assume loop like -n but print line also, like sed |
| `-s` | `-s` | bool | enable rudimentary parsing for switches after programfile |
| `-t` | `-t` | bool | enable tainting warnings |
| `-u` | `-u` | bool | dump core after parsing program |
| `-v` | `-v` | bool | print version, patchlevel and license |
| `-w` | `-w` | bool | enable many useful warnings |
| `-x` | `-x` | string | ignore text before #!perl line (optionally cd to directory) |

