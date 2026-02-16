# python -- Complete Command Reference

## Global Flags

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--check-hash-based-pycs` | `` | string |  |
| `--help-all` | `` | string |  |
| `--help-env` | `` | string |  |
| `--help-xoptions` | `-X` | string |  |
| `-B` | `-B` | bool | : don't write .pyc files on import; also PYTHONDONTWRITEBYTECODE=x |
| `-E` | `-E` | bool | : ignore PYTHON* environment variables (such as PYTHONPATH) |
| `-I` | `-I` | bool | : isolate Python from the user's environment (implies -E and -s) |
| `-O` | `-O` | bool | : remove assert and __debug__-dependent statements; add .opt-1 before |
| `-P` | `-P` | bool | : don't prepend a potentially unsafe path to sys.path; also |
| `-S` | `-S` | bool | : don't imply 'import site' on initialization |
| `-V` | `-V` | bool | : print the Python version number and exit (also --version) |
| `-W` | `-W` | string | warning control; arg is action:message:category:module:lineno |
| `-X` | `-X` | string | set implementation-specific option |
| `-b` | `-b` | bool | : issue warnings about converting bytes/bytearray to str and comparing |
| `-c` | `-c` | string | program passed in as string (terminates option list) |
| `-d` | `-d` | bool | : turn on parser debugging output (for experts only, only works on |
| `-h` | `-h` | bool | : print this help message and exit (also -? or --help) |
| `-i` | `-i` | bool | : inspect interactively after running script; forces a prompt even |
| `-m` | `-m` | string | run library module as a script (terminates option list) |
| `-q` | `-q` | bool | : don't print version and copyright messages on interactive startup |
| `-s` | `-s` | bool | : don't add user site directory to sys.path; also PYTHONNOUSERSITE=x |
| `-u` | `-u` | bool | : force the stdout and stderr streams to be unbuffered; |
| `-v` | `-v` | bool | : verbose (trace import statements); also PYTHONVERBOSE=x |
| `-x` | `-x` | bool | : skip first line of source, allowing use of non-Unix forms of #!cmd |

