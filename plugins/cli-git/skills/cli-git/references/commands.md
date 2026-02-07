# git -- Complete Command Reference

## Commands

### `git add`

Add file contents to the index

```
git add [--verbose | -v] [--dry-run | -n] [--force | -f] [--interactive | -i] [--patch | -p] [--edit | -e] [--[no-]all | --[no-]ignore-removal | [--update | -u]] [--sparse] [--intent-to-add | -N] [--refresh] [--ignore-errors] [--ignore-missing] [--renormalize] [--chmod=(+|-)x] [--pathspec-from-file=<file> [--pathspec-file-nul]] [--] [<pathspec>...]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--all` | `-A` | string | Update the index not only where the working tree has a file matching <pathspec> but also where the index already has an entry. This adds, modifies, and removes index entries to match the working tree. If no <pathspec> is given when -A option is used, all files in the entire working tree are updated (old versions of Git used to limit the update to the current directory and its subdirectories). |
| `--dry-run` | `-n` | string | Don't actually add the file(s), just show if they exist and/or will be ignored. |
| `--edit` | `-e` | bool | Open the diff vs. the index in an editor and let the user edit it. After the editor was closed, adjust the hunk headers and apply the patch to the index. The intent of this option is to pick and choose lines of the patch to apply, or even to modify the contents of lines to be staged. This can be quicker and more flexible than using the interactive hunk selector. However, it is easy to confuse oneself and create a patch that does not apply to the index. See EDITING PATCHES below. |
| `--force` | `-f` | string | Allow adding otherwise ignored files. |
| `--ignore-errors` | `` | string | If some files could not be added because of errors indexing them, do not abort the operation, but continue adding the others. The command shall still exit with non-zero status. The configuration variable add.ignoreErrors can be set to true to make this the default behaviour. |
| `--ignore-missing` | `` | string | This option can only be used together with --dry-run. By using this option the user can check if any of the given files would be ignored, no matter if they are already present in the work tree or not. |
| `--intent-to-add` | `-N` | string | Record only the fact that the path will be added later. An entry for the path is placed in the index with no content. This is useful for, among other things, showing the unstaged content of such files with git diff and committing them with git commit -a. |
| `--interactive` | `-i` | string | Add modified contents in the working tree interactively to the index. Optional path arguments may be supplied to limit operation to a subset of the working tree. See "Interactive mode" for details. |
| `--no-all` | `` | string | Update the index by adding new files that are unknown to the index and files modified in the working tree, but ignore files that have been removed from the working tree. This option is a no-op when no <pathspec> is used. This option is primarily to help users who are used to older versions of Git, whose "git add <pathspec>..." was a synonym for "git add --no-all <pathspec>...", i.e. ignored removed files. |
| `--no-warn-embedded-repo` | `` | bool | By default, git add will warn when adding an embedded repository to the index without using git submodule add to create an entry in .gitmodules. This option will suppress the warning (e.g., if you are manually performing operations on submodules). |
| `--patch` | `-p` | string | Interactively choose hunks of patch between the index and the work tree and add them to the index. This gives the user a chance to review the difference before adding modified contents to the index. This effectively runs add --interactive, but bypasses the initial command menu and directly jumps to the patch subcommand. See "Interactive mode" for details. |
| `--pathspec-file-nul` | `` | string | Only meaningful with --pathspec-from-file. Pathspec elements are separated with NUL character and all other characters are taken literally (including newlines and quotes). |
| `--pathspec-from-file` | `` | string | Pathspec is passed in <file> instead of commandline args. If <file> is exactly - then standard input is used. Pathspec elements are separated by LF or CR/LF. Pathspec elements can be quoted as explained for the configuration variable core.quotePath (see git-config(1)). See also --pathspec-file-nul and global --literal-pathspecs. |
| `--refresh` | `` | string | Don't add the file(s), but only refresh their stat() information in the index. |
| `--renormalize` | `` | string | Apply the "clean" process freshly to all tracked files to forcibly add them again to the index. This is useful after changing core.autocrlf configuration or the text attribute in order to correct files added with wrong CRLF/LF line endings. This option implies -u. Lone CR characters are untouched, thus while a CRLF cleans to LF, a CRCRLF sequence is only partially cleaned to CRLF. |
| `--sparse` | `` | string | Allow updating index entries outside of the sparse-checkout cone. Normally, git add refuses to update index entries whose paths do not fit within the sparse-checkout cone, since those files might be removed from the working tree without warning. See git-sparse-checkout(1) for more details. |
| `--update` | `-u` | string | Update the index just where it already has an entry matching <pathspec>. This removes as well as modifies index entries to match the working tree, but adds no new files. If no <pathspec> is given when -u option is used, all tracked files in the entire working tree are updated (old versions of Git used to limit the update to the current directory and its subdirectories). |
| `--verbose` | `-v` | bool | Be verbose. |

### `git bisect`

Use binary search to find the commit that introduced a bug

```
git bisect <subcommand> <options>
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--first-parent` | `` | bool | Follow only the first parent commit upon seeing a merge commit. In detecting regressions introduced through the merging of a branch, the merge commit will be identified as introduction of the bug and its ancestors will be ignored. This option is particularly useful in avoiding false positives when a merged branch contained broken or non-buildable commits, but the merge itself was OK. |
| `--no-checkout` | `` | string | Do not checkout the new working tree at each iteration of the bisection process. Instead just update a special reference named BISECT_HEAD to make it point to the commit that should be tested. This option may be useful when the test you would perform in each step does not require a checked out tree. If the repository is bare, --no-checkout is assumed. |

### `git branch`

List, create, or delete branches

```
git branch [--color[=<when>] | --no-color] [--show-current] [-v [--abbrev=<n> | --no-abbrev]] [--column[=<options>] | --no-column] [--sort=<key>] [--merged [<commit>]] [--no-merged [<commit>]] [--contains [<commit>]] [--no-contains [<commit>]] [--points-at <object>] [--format=<format>] [(-r | --remotes) | (-a | --all)] [--list] [<pattern>...] git branch [--track[=(direct|inherit)] | --no-track] [-f] [--recurse-submodules] <branchname> [<start-point>] git branch (--set-upstream-to=<upstream> | -u <upstream>) [<branchname>] git branch --unset-upstream [<branchname>] git branch (-m | -M) [<oldbranch>] <newbranch> git branch (-c | -C) [<oldbranch>] <newbranch> git branch (-d | -D) [-r] <branchname>... git branch --edit-description [<branchname>]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--abbrev` | `` | string | In the verbose listing that show the commit object name, show the shortest prefix that is at least <n> hexdigits long that uniquely refers the object. The default value is 7 and can be overridden by the core.abbrev config option. |
| `--all` | `-a` | bool | List both remote-tracking branches and local branches. Combine with --list to match optional pattern(s). |
| `--copy` | `-c` | bool | Copy a branch, together with its config and reflog. |
| `--create-reflog` | `` | string | Create the branch's reflog. This activates recording of all changes made to the branch ref, enabling use of date based sha1 expressions such as "<branchname>@{yesterday}". Note that in non-bare repositories, reflogs are usually enabled by default by the core.logAllRefUpdates config option. The negated form --no-create-reflog only overrides an earlier --create-reflog, but currently does not negate the setting of core.logAllRefUpdates. |
| `--delete` | `-d` | bool | Delete a branch. The branch must be fully merged in its upstream branch, or in HEAD if no upstream was set with --track or --set-upstream-to. |
| `--edit-description` | `` | string | Open an editor and edit the text to explain what the branch is for, to be used by various other commands (e.g.  format-patch, request-pull, and merge (if enabled)). Multi-line explanations may be used. |
| `--force` | `-f` | string | Reset <branchname> to <start-point>, even if <branchname> exists already. Without -f, git branch refuses to change an existing branch. In combination with -d (or --delete), allow deleting the branch irrespective of its merged status, or whether it even points to a valid commit. In combination with -m (or --move), allow renaming the branch even if the new branch name already exists, the same applies for -c (or --copy). Note that git branch -f <branchname> [<start-point>], even with -f, refuses to change an existing branch <branchname> that is checked out in another worktree linked to the same repository. |
| `--format` | `` | string | A string that interpolates %(fieldname) from a branch ref being shown and the object it points at. The format is the same as that of git-for-each-ref(1). |
| `--ignore-case` | `-i` | bool | Sorting and filtering branches are case insensitive. |
| `--list` | `-l` | bool | List branches. With optional <pattern>..., e.g.  git branch --list 'maint-*', list only the branches that match the pattern(s). |
| `--move` | `-m` | string | Move/rename a branch, together with its config and reflog. |
| `--no-abbrev` | `` | bool | Display the full sha1s in the output listing rather than abbreviating them. |
| `--no-color` | `` | string | Turn off branch colors, even when the configuration file gives the default to color output. Same as --color=never. |
| `--no-track` | `` | bool | Do not set up "upstream" configuration, even if the branch.autoSetupMerge configuration variable is set. |
| `--omit-empty` | `` | string | Do not print a newline after formatted refs where the format expands to the empty string. |
| `--points-at` | `` | string | Only list branches of the given object. |
| `--quiet` | `-q` | bool | Be more quiet when creating or deleting a branch, suppressing non-error messages. |
| `--recurse-submodules` | `` | string | THIS OPTION IS EXPERIMENTAL! Causes the current command to recurse into submodules if submodule.propagateBranches is enabled. See submodule.propagateBranches in git-config(1). Currently, only branch creation is supported. When used in branch creation, a new branch <branchname> will be created in the superproject and all of the submodules in the superproject's <start-point>. In submodules, the branch will point to the submodule commit in the superproject's <start-point> but the branch's tracking information will be set up based on the submodule's branches and remotes e.g.  git branch --recurse-submodules topic origin/main will create the submodule branch "topic" that points to the submodule commit in the superproject's "origin/main", but tracks the submodule's "origin/main". |
| `--remotes` | `-r` | bool | List or delete (if used with -d) the remote-tracking branches. Combine with --list to match the optional pattern(s). |
| `--set-upstream` | `` | bool | As this option had confusing syntax, it is no longer supported. Please use --track or --set-upstream-to instead. |
| `--show-current` | `` | string | Print the name of the current branch. In detached HEAD state, nothing is printed. |
| `--sort` | `` | string | Sort based on the key given. Prefix - to sort in descending order of the value. You may use the --sort=<key> option multiple times, in which case the last key becomes the primary key. The keys supported are the same as those in git for-each-ref. Sort order defaults to the value configured for the branch.sort variable if it exists, or to sorting based on the full refname (including refs/...  prefix). This lists detached HEAD (if present) first, then local branches and finally remote-tracking branches. See git- config(1). |
| `--unset-upstream` | `` | string | Remove the upstream information for <branchname>. If no branch is specified it defaults to the current branch. |
| `-C` | `-C` | bool | Shortcut for --copy --force. |
| `-D` | `-D` | bool | Shortcut for --delete --force. |
| `-M` | `-M` | bool | Shortcut for --move --force. |

### `git clone`

Clone a repository into a new directory

```
git clone [--template=<template-directory>] [-l] [-s] [--no-hardlinks] [-q] [-n] [--bare] [--mirror] [-o <name>] [-b <name>] [-u <upload-pack>] [--reference <repository>] [--dissociate] [--separate-git-dir <git-dir>] [--depth <depth>] [--[no-]single-branch] [--no-tags] [--recurse-submodules[=<pathspec>]] [--[no-]shallow-submodules] [--[no-]remote-submodules] [--jobs <n>] [--sparse] [--[no-]reject-shallow] [--filter=<filter> [--also-filter-submodules]] [--] <repository> [<directory>]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--also-filter-submodules` | `` | bool | Also apply the partial clone filter to any submodules in the repository. Requires --filter and --recurse-submodules. This can be turned on by default by setting the clone.filterSubmodules config option. |
| `--bare` | `` | string | Make a bare Git repository. That is, instead of creating <directory> and placing the administrative files in <directory>/.git, make the <directory> itself the $GIT_DIR. This obviously implies the --no-checkout because there is nowhere to check out the working tree. Also the branch heads at the remote are copied directly to corresponding local branch heads, without mapping them to refs/remotes/origin/. When this option is used, neither remote-tracking branches nor the related configuration variables are created. |
| `--bundle-uri` | `` | string | Before fetching from the remote, fetch a bundle from the given <uri> and unbundle the data into the local repository. The refs in the bundle will be stored under the hidden refs/bundle/* namespace. This option is incompatible with --depth, --shallow-since, and --shallow-exclude. |
| `--depth` | `` | string | Create a shallow clone with a history truncated to the specified number of commits. Implies --single-branch unless --no-single-branch is given to fetch the histories near the tips of all branches. If you want to clone submodules shallowly, also pass --shallow-submodules. |
| `--dissociate` | `` | bool | Borrow the objects from reference repositories specified with the --reference options only to reduce network transfer, and stop borrowing from them after a clone is made by making necessary local copies of borrowed objects. This option can also be used when cloning locally from a repository that already borrows objects from another repository--the new repository will borrow objects from the same repository, and this option can be used to stop the borrowing. |
| `--filter` | `` | string | Use the partial clone feature and request that the server sends a subset of reachable objects according to a given object filter. When using --filter, the supplied <filter-spec> is used for the partial clone filter. For example, --filter=blob:none will filter out all blobs (file contents) until needed by Git. Also, --filter=blob:limit=<size> will filter out all blobs of size at least <size>. For more details on filter specifications, see the --filter option in git-rev-list(1). |
| `--local` | `-l` | string | When the repository to clone from is on a local machine, this flag bypasses the normal "Git aware" transport mechanism and clones the repository by making a copy of HEAD and everything under objects and refs directories. The files under .git/objects/ directory are hardlinked to save space when possible. If the repository is specified as a local path (e.g., /path/to/repo), this is the default, and --local is essentially a no-op. If the repository is specified as a URL, then this flag is ignored (and we never use the local optimizations). Specifying --no-local will override the default when /path/to/repo is given, using the regular Git transport instead. If the repository's $GIT_DIR/objects has symbolic links or is a symbolic link, the clone will fail. This is a security measure to prevent the unintentional copying of files by dereferencing the symbolic links. NOTE: this operation can race with concurrent modification to the source repository, similar to running cp -r src dst while modifying src. |
| `--mirror` | `` | bool | Set up a mirror of the source repository. This implies --bare. Compared to --bare, --mirror not only maps local branches of the source to local branches of the target, it maps all refs (including remote-tracking branches, notes etc.) and sets up a refspec configuration such that all these refs are overwritten by a git remote update in the target repository. |
| `--no-checkout` | `-n` | bool | No checkout of HEAD is performed after the clone is complete. |
| `--no-hardlinks` | `` | string | Force the cloning process from a repository on a local filesystem to copy the files under the .git/objects directory instead of using hardlinks. This may be desirable if you are trying to make a back-up of your repository. |
| `--no-tags` | `` | bool | Don't clone any tags, and set remote.<remote>.tagOpt=--no-tags in the config, ensuring that future git pull and git fetch operations won't follow any tags. Subsequent explicit tag fetches will still work, (see git-fetch(1)). Can be used in conjunction with --single-branch to clone and maintain a branch with no references other than a single cloned branch. This is useful e.g. to maintain minimal clones of the default branch of some repository for search indexing. |
| `--progress` | `` | bool | Progress status is reported on the standard error stream by default when it is attached to a terminal, unless --quiet is specified. This flag forces progress status even if the standard error stream is not directed to a terminal. |
| `--quiet` | `-q` | bool | Operate quietly. Progress is not reported to the standard error stream. |
| `--separate-git-dir` | `` | string | Instead of placing the cloned repository where it is supposed to be, place the cloned repository at the specified directory, then make a filesystem-agnostic Git symbolic link to there. The result is Git repository can be separated from working tree. |
| `--server-option` | `` | string | Transmit the given string to the server when communicating using protocol version 2. The given string must not contain a NUL or LF character. The server's handling of server options, including unknown ones, is server-specific. When multiple --server-option=<option> are given, they are all sent to the other side in the order listed on the command line. |
| `--shallow-exclude` | `` | string | Create a shallow clone with a history, excluding commits reachable from a specified remote branch or tag. This option can be specified multiple times. |
| `--shallow-since` | `` | string | Create a shallow clone with a history after the specified time. |
| `--shared` | `-s` | bool | When the repository to clone is on the local machine, instead of using hard links, automatically setup .git/objects/info/alternates to share the objects with the source repository. The resulting repository starts out without any object of its own. NOTE: this is a possibly dangerous operation; do not use it unless you understand what it does. If you clone your repository using this option and then delete branches (or use any other Git command that makes any existing commit unreferenced) in the source repository, some objects may become unreferenced (or dangling). These objects may be removed by normal Git operations (such as git commit) which automatically call git maintenance run --auto. (See git-maintenance(1).) If these objects are removed and were referenced by the cloned repository, then the cloned repository will become corrupt. Note that running git repack without the --local option in a repository cloned with --shared will copy objects from the source repository into a pack in the cloned repository, removing the disk space savings of clone --shared. It is safe, however, to run git gc, which uses the --local option by default. If you want to break the dependency of a repository cloned with --shared on its source repository, you can simply run git repack -a to copy all objects from the source repository into a pack in the cloned repository. |
| `--sparse` | `` | string | Employ a sparse-checkout, with only files in the toplevel directory initially being present. The git- sparse-checkout(1) command can be used to grow the working directory as needed. |
| `--template` | `` | string | Specify the directory from which templates will be used; (See the "TEMPLATE DIRECTORY" section of git- init(1).) |
| `--verbose` | `-v` | bool | Run verbosely. Does not affect the reporting of progress status to the standard error stream. |

### `git commit`

Record changes to the repository

```
git commit [-a | --interactive | --patch] [-s] [-v] [-u<mode>] [--amend] [--dry-run] [(-c | -C | --squash) <commit> | --fixup [(amend|reword):]<commit>)] [-F <file> | -m <msg>] [--reset-author] [--allow-empty] [--allow-empty-message] [--no-verify] [-e] [--author=<author>] [--date=<date>] [--cleanup=<mode>] [--[no-]status] [-i | -o] [--pathspec-from-file=<file> [--pathspec-file-nul]] [(--trailer <token>[(=|:)<value>])...] [-S[<keyid>]] [--] [<pathspec>...]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--all` | `-a` | string | Tell the command to automatically stage files that have been modified and deleted, but new files you have not told Git about are not affected. |
| `--allow-empty` | `` | bool | Usually recording a commit that has the exact same tree as its sole parent commit is a mistake, and the command prevents you from making such a commit. This option bypasses the safety, and is primarily for use by foreign SCM interface scripts. |
| `--allow-empty-message` | `` | bool | Like --allow-empty this command is primarily for use by foreign SCM interface scripts. It allows you to create a commit with an empty commit message without using plumbing commands like git-commit-tree(1). |
| `--amend` | `` | string | Replace the tip of the current branch by creating a new commit. The recorded tree is prepared as usual (including the effect of the -i and -o options and explicit pathspec), and the message from the original commit is used as the starting point, instead of an empty message, when no other message is specified from the command line via options such as -m, -F, -c, etc. The new commit has the same parents and author as the current one (the --reset-author option can countermand this). It is a rough equivalent for: $ git reset --soft HEAD^ $ ... do something else to come up with the right tree ... $ git commit -c ORIG_HEAD but can be used to amend a merge commit. You should understand the implications of rewriting history if you amend a commit that has already been published. (See the "RECOVERING FROM UPSTREAM REBASE" section in git-rebase(1).) |
| `--author` | `` | string | Override the commit author. Specify an explicit author using the standard A U Thor <author@example.com> format. Otherwise <author> is assumed to be a pattern and is used to search for an existing commit by that author (i.e. rev-list --all -i --author=<author>); the commit author is then copied from the first such commit found. |
| `--branch` | `` | string | Show the branch and tracking info even in short-format. |
| `--cleanup` | `` | string | This option determines how the supplied commit message should be cleaned up before committing. The <mode> can be strip, whitespace, verbatim, scissors or default. strip Strip leading and trailing empty lines, trailing whitespace, commentary and collapse consecutive empty lines. whitespace Same as strip except #commentary is not removed. verbatim Do not change the message at all. scissors Same as whitespace except that everything from (and including) the line found below is truncated, if the message is to be edited. "#" can be customized with core.commentChar. # ------------------------ >8 ------------------------ default Same as strip if the message is to be edited. Otherwise whitespace. The default can be changed by the commit.cleanup configuration variable (see git-config(1)). |
| `--date` | `` | string | Override the author date used in the commit. |
| `--dry-run` | `` | string | Do not create a commit, but show a list of paths that are to be committed, paths with local changes that will be left uncommitted and paths that are untracked. |
| `--edit` | `-e` | string | The message taken from file with -F, command line with -m, and from commit object with -C are usually used as the commit log message unmodified. This option lets you further edit the message taken from these sources. |
| `--include` | `-i` | string | Before making a commit out of staged contents so far, stage the contents of paths given on the command line as well. This is usually not what you want unless you are concluding a conflicted merge. |
| `--long` | `` | string | When doing a dry-run, give the output in the long-format. Implies --dry-run. |
| `--no-edit` | `` | bool | Use the selected commit message without launching an editor. For example, git commit --amend --no-edit amends a commit without changing its commit message. |
| `--no-post-rewrite` | `` | bool | Bypass the post-rewrite hook. |
| `--no-status` | `` | bool | Do not include the output of git-status(1) in the commit message template when using an editor to prepare the default commit message. |
| `--null` | `-z` | string | When showing short or porcelain status output, print the filename verbatim and terminate the entries with NUL, instead of LF. If no format is given, implies the --porcelain output format. Without the -z option, filenames with "unusual" characters are quoted as explained for the configuration variable core.quotePath (see git-config(1)). |
| `--only` | `-o` | string | Make a commit by taking the updated working tree contents of the paths specified on the command line, disregarding any contents that have been staged for other paths. This is the default mode of operation of git commit if any paths are given on the command line, in which case this option can be omitted. If this option is specified together with --amend, then no paths need to be specified, which can be used to amend the last commit without committing changes that have already been staged. If used together with --allow-empty paths are also not required, and an empty commit will be created. |
| `--patch` | `-p` | bool | Use the interactive patch selection interface to choose which changes to commit. See git-add(1) for details. |
| `--pathspec-file-nul` | `` | string | Only meaningful with --pathspec-from-file. Pathspec elements are separated with NUL character and all other characters are taken literally (including newlines and quotes). |
| `--pathspec-from-file` | `` | string | Pathspec is passed in <file> instead of commandline args. If <file> is exactly - then standard input is used. Pathspec elements are separated by LF or CR/LF. Pathspec elements can be quoted as explained for the configuration variable core.quotePath (see git-config(1)). See also --pathspec-file-nul and global --literal-pathspecs. |
| `--porcelain` | `` | string | When doing a dry-run, give the output in a porcelain-ready format. See git-status(1) for details. Implies --dry-run. |
| `--quiet` | `-q` | bool | Suppress commit summary message. |
| `--reset-author` | `` | bool | When used with -C/-c/--amend options, or when committing after a conflicting cherry-pick, declare that the authorship of the resulting commit now belongs to the committer. This also renews the author timestamp. |
| `--short` | `` | string | When doing a dry-run, give the output in the short-format. See git-status(1) for details. Implies --dry-run. |
| `--signoff` | `-s` | bool | Add a Signed-off-by trailer by the committer at the end of the commit log message. The meaning of a signoff depends on the project to which you're committing. For example, it may certify that the committer has the rights to submit the work under the project's license or agrees to some contributor representation, such as a Developer Certificate of Origin. (See http://developercertificate.org for the one used by the Linux kernel and Git projects.) Consult the documentation or leadership of the project to which you're contributing to understand how the signoffs are used in that project. The --no-signoff option can be used to countermand an earlier --signoff option on the command line. |
| `--squash` | `` | string | Construct a commit message for use with rebase --autosquash. The commit message subject line is taken from the specified commit with a prefix of "squash! ". Can be used with additional commit message options (-m/-c/-C/-F). See git-rebase(1) for details. |
| `--status` | `` | bool | Include the output of git-status(1) in the commit message template when using an editor to prepare the commit message. Defaults to on, but can be used to override configuration variable commit.status. |
| `--verbose` | `-v` | string | Show unified diff between the HEAD commit and what would be committed at the bottom of the commit message template to help the user describe the commit by reminding what changes the commit has. Note that this diff output doesn't have its lines prefixed with #. This diff will not be a part of the commit message. See the commit.verbose configuration variable in git-config(1). If specified twice, show in addition the unified diff between what would be committed and the worktree files, i.e. the unstaged changes to tracked files. |

### `git diff`

Show changes between commits, commit and working tree, etc

```
git diff [<options>] [<commit>] [--] [<path>...] git diff [<options>] --cached [--merge-base] [<commit>] [--] [<path>...] git diff [<options>] [--merge-base] <commit> [<commit>...] <commit> [--] [<path>...] git diff [<options>] <commit>...<commit> [--] [<path>...] git diff [<options>] <blob> <blob> git diff [<options>] --no-index [--] <path> <path>
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--anchored` | `` | string | Generate a diff using the "anchored diff" algorithm. This option may be specified more than once. If a line exists in both the source and destination, exists only once, and starts with this text, this algorithm attempts to prevent it from appearing as a deletion or addition in the output. It uses the "patience diff" algorithm internally. |
| `--binary` | `` | bool | In addition to --full-index, output a binary diff that can be applied with git-apply. Implies --patch. |
| `--check` | `` | bool | Warn if changes introduce conflict markers or whitespace errors. What are considered whitespace errors is controlled by core.whitespace configuration. By default, trailing whitespaces (including lines that consist solely of whitespaces) and a space character that is immediately followed by a tab character inside the initial indent of the line are considered whitespace errors. Exits with non-zero status if problems are found. Not compatible with --exit-code. |
| `--color-moved-ws` | `` | string | This configures how whitespace is ignored when performing the move detection for --color-moved. It can be set by the diff.colorMovedWS configuration setting. These modes can be given as a comma separated list: no Do not ignore whitespace when performing move detection. ignore-space-at-eol Ignore changes in whitespace at EOL. ignore-space-change Ignore changes in amount of whitespace. This ignores whitespace at line end, and considers all other sequences of one or more whitespace characters to be equivalent. ignore-all-space Ignore whitespace when comparing lines. This ignores differences even if one line has whitespace where the other line has none. allow-indentation-change Initially ignore any whitespace in the move detection, then group the moved code blocks only into a block if the change in whitespace is the same per line. This is incompatible with the other modes. |
| `--compact-summary` | `` | string | Output a condensed summary of extended header information such as file creations or deletions ("new" or "gone", optionally "+l" if it's a symlink) and mode changes ("+x" or "-x" for adding or removing executable bit respectively) in diffstat. The information is put between the filename part and the graph part. Implies --stat. |
| `--cumulative` | `` | bool | Synonym for --dirstat=cumulative |
| `--default-prefix` | `` | bool | Use the default source and destination prefixes ("a/" and "b/"). This is usually the default already, but may be used to override config such as diff.noprefix. |
| `--dst-prefix` | `` | string | Show the given destination prefix instead of "b/". |
| `--exit-code` | `` | bool | Make the program exit with codes similar to diff(1). That is, it exits with 1 if there were differences and 0 means no differences. |
| `--ext-diff` | `` | bool | Allow an external diff helper to be executed. If you set an external diff driver with gitattributes(5), you need to use this option with git-log(1) and friends. |
| `--find-copies-harder` | `` | string | For performance reasons, by default, -C option finds copies only if the original file of the copy was modified in the same changeset. This flag makes the command inspect unmodified files as candidates for the source of copy. This is a very expensive operation for large projects, so use it with caution. Giving more than one -C option has the same effect. |
| `--find-object` | `` | string | Look for differences that change the number of occurrences of the specified object. Similar to -S, just the argument is different in that it doesn't search for a specific string but for a specific object id. The object can be a blob or a submodule commit. It implies the -t option in git-log to also find trees. |
| `--full-index` | `` | string | Instead of the first handful of characters, show the full pre- and post-image blob object names on the "index" line when generating patch format output. |
| `--function-context` | `-W` | string | Show whole function as context lines for each change. The function names are determined in the same way as git diff works out patch hunk headers (see Defining a custom hunk-header in gitattributes(5)). |
| `--histogram` | `` | bool | Generate a diff using the "histogram diff" algorithm. |
| `--ignore-all-space` | `-w` | bool | Ignore whitespace when comparing lines. This ignores differences even if one line has whitespace where the other line has none. |
| `--ignore-blank-lines` | `` | bool | Ignore changes whose lines are all blank. |
| `--ignore-cr-at-eol` | `` | bool | Ignore carriage-return at the end of line when doing a comparison. |
| `--ignore-space-at-eol` | `` | bool | Ignore changes in whitespace at EOL. |
| `--ignore-space-change` | `-b` | bool | Ignore changes in amount of whitespace. This ignores whitespace at line end, and considers all other sequences of one or more whitespace characters to be equivalent. |
| `--indent-heuristic` | `` | bool | Enable the heuristic that shifts diff hunk boundaries to make patches easier to read. This is the default. |
| `--inter-hunk-context` | `` | string | Show the context between diff hunks, up to the specified number of lines, thereby fusing hunks that are close to each other. Defaults to diff.interHunkContext or 0 if the config option is unset. |
| `--irreversible-delete` | `-D` | string | Omit the preimage for deletes, i.e. print only the header but not the diff between the preimage and /dev/null. The resulting patch is not meant to be applied with patch or git apply; this is solely for people who want to just concentrate on reviewing the text after the change. In addition, the output obviously lacks enough information to apply such a patch in reverse, even manually, hence the name of the option. When used together with -B, omit also the preimage in the deletion part of a delete/create pair. |
| `--ita-invisible-in-index` | `` | string | By default entries added by "git add -N" appear as an existing empty file in "git diff" and a new file in "git diff --cached". This option makes the entry appear as a new file in "git diff" and non-existent in "git diff --cached". This option could be reverted with --ita-visible-in-index. Both options are experimental and could be removed in future. |
| `--line-prefix` | `` | string | Prepend an additional prefix to every line of output. |
| `--minimal` | `` | bool | Spend extra time to make sure the smallest possible diff is produced. |
| `--name-only` | `` | string | Show only names of changed files. The file names are often encoded in UTF-8. For more information see the discussion about encoding in the git-log(1) manual page. |
| `--name-status` | `` | string | Show only names and status of changed files. See the description of the --diff-filter option on what the status letters mean. Just like --name-only the file names are often encoded in UTF-8. |
| `--no-color` | `` | bool | Turn off colored diff. This can be used to override configuration settings. It is the same as --color=never. |
| `--no-color-moved` | `` | bool | Turn off move detection. This can be used to override configuration settings. It is the same as --color-moved=no. |
| `--no-color-moved-ws` | `` | bool | Do not ignore whitespace when performing move detection. This can be used to override configuration settings. It is the same as --color-moved-ws=no. |
| `--no-ext-diff` | `` | bool | Disallow external diff drivers. |
| `--no-indent-heuristic` | `` | bool | Disable the indent heuristic. |
| `--no-patch` | `-s` | bool | Suppress all output from the diff machinery. Useful for commands like git show that show the patch by default to squelch their output, or to cancel the effect of options like --patch, --stat earlier on the command line in an alias. |
| `--no-prefix` | `` | bool | Do not show any source or destination prefix. |
| `--no-renames` | `` | string | Turn off rename detection, even when the configuration file gives the default to do so. |
| `--numstat` | `` | string | Similar to --stat, but shows number of added and deleted lines in decimal notation and pathname without abbreviation, to make it more machine friendly. For binary files, outputs two - instead of saying 0 0. |
| `--output` | `` | string | Output to a specific file instead of stdout. |
| `--patch-with-raw` | `` | bool | Synonym for -p --raw. |
| `--patch-with-stat` | `` | bool | Synonym for -p --stat. |
| `--patience` | `` | bool | Generate a diff using the "patience diff" algorithm. |
| `--pickaxe-all` | `` | string | When -S or -G finds a change, show all the changes in that changeset, not just the files that contain the change in <string>. |
| `--pickaxe-regex` | `` | bool | Treat the <string> given to -S as an extended POSIX regular expression to match. |
| `--quiet` | `` | bool | Disable all output of the program. Implies --exit-code. |
| `--raw` | `` | string | Generate the diff in raw format. |
| `--shortstat` | `` | string | Output only the last line of the --stat format containing total number of modified files, as well as number of added and deleted lines. |
| `--src-prefix` | `` | string | Show the given source prefix instead of "a/". |
| `--summary` | `` | string | Output a condensed summary of extended header information such as creations, renames and mode changes. |
| `--text` | `-a` | string | Treat all files as text. |
| `--textconv` | `` | string | Allow (or disallow) external text conversion filters to be run when comparing binary files. See gitattributes(5) for details. Because textconv filters are typically a one-way conversion, the resulting diff is suitable for human consumption, but cannot be applied. For this reason, textconv filters are enabled by default only for git-diff(1) and git-log(1), but not for git-format-patch(1) or diff plumbing commands. |
| `--word-diff-regex` | `` | string | Use <regex> to decide what a word is, instead of considering runs of non-whitespace to be a word. Also implies --word-diff unless it was already enabled. Every non-overlapping match of the <regex> is considered a word. Anything between these matches is considered whitespace and ignored(!) for the purposes of finding differences. You may want to append |[^[:space:]] to your regular expression to make sure that it matches all non-whitespace characters. A match that contains a newline is silently truncated(!) at the newline. For example, --word-diff-regex=.  will treat each character as a word and, correspondingly, show differences character by character. The regex can also be set via a diff driver or configuration option, see gitattributes(5) or git- config(1). Giving it explicitly overrides any diff driver or configuration setting. Diff drivers override configuration settings. |
| `--ws-error-highlight` | `` | string | Highlight whitespace errors in the context, old or new lines of the diff. Multiple values are separated by comma, none resets previous values, default reset the list to new and all is a shorthand for old,new,context. When this option is not given, and the configuration variable diff.wsErrorHighlight is not set, only whitespace errors in new lines are highlighted. The whitespace errors are colored with color.diff.whitespace. |
| `-0` | `-0` | bool | Omit diff output for unmerged entries and just show "Unmerged". Can be used only when comparing the working tree with the index. |
| `-R` | `-R` | bool | Swap two inputs; that is, show differences from index or on-disk file to tree contents. |
| `-z` | `-z` | bool | When --raw, --numstat, --name-only or --name-status has been given, do not munge pathnames and use NULs as output field terminators. Without this option, pathnames with "unusual" characters are quoted as explained for the configuration variable core.quotePath (see git-config(1)). |

### `git fetch`

Download objects and refs from another repository

```
git fetch [<options>] [<repository> [<refspec>...]] git fetch [<options>] <group> git fetch --multiple [<options>] [(<repository> | <group>)...] git fetch --all [<options>]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--all` | `` | bool | Fetch all remotes. |
| `--append` | `-a` | string | Append ref names and object names of fetched refs to the existing contents of .git/FETCH_HEAD. Without this option old data in .git/FETCH_HEAD will be overwritten. |
| `--atomic` | `` | bool | Use an atomic transaction to update local refs. Either all refs are updated, or on error, no refs are updated. |
| `--deepen` | `` | string | Similar to --depth, except it specifies the number of commits from the current shallow boundary instead of from the tip of each remote branch history. |
| `--depth` | `` | string | Limit fetching to the specified number of commits from the tip of each remote branch history. If fetching to a shallow repository created by git clone with --depth=<depth> option (see git-clone(1)), deepen or shorten the history to the specified number of commits. Tags for the deepened commits are not fetched. |
| `--dry-run` | `` | bool | Show what would be done, without making any changes. |
| `--force` | `-f` | bool | When git fetch is used with <src>:<dst> refspec, it may refuse to update the local branch as discussed in the <refspec> part below. This option overrides that check. |
| `--ipv4` | `-4` | bool | Use IPv4 addresses only, ignoring IPv6 addresses. |
| `--ipv6` | `-6` | bool | Use IPv6 addresses only, ignoring IPv4 addresses. |
| `--jobs` | `-j` | string | Number of parallel children to be used for all forms of fetching. If the --multiple option was specified, the different remotes will be fetched in parallel. If multiple submodules are fetched, they will be fetched in parallel. To control them independently, use the config settings fetch.parallel and submodule.fetchJobs (see git-config(1)). Typically, parallel recursive and multi-remote fetches will be faster. By default fetches are performed sequentially, not in parallel. |
| `--keep` | `-k` | bool | Keep downloaded pack. |
| `--multiple` | `` | bool | Allow several <repository> and <group> arguments to be specified. No <refspec>s may be specified. |
| `--negotiate-only` | `` | bool | Do not fetch anything from the server, and instead print the ancestors of the provided --negotiation-tip=* arguments, which we have in common with the server. This is incompatible with --recurse-submodules=[yes|on-demand]. Internally this is used to implement the push.negotiate option, see git-config(1). |
| `--negotiation-tip` | `` | string | By default, Git will report, to the server, commits reachable from all local refs to find common commits in an attempt to reduce the size of the to-be-received packfile. If specified, Git will only report commits reachable from the given tips. This is useful to speed up fetches when the user knows which local ref is likely to have commits in common with the upstream ref being fetched. This option may be specified more than once; if so, Git will report commits reachable from any of the given commits. The argument to this option may be a glob on ref names, a ref, or the (possibly abbreviated) SHA-1 of a commit. Specifying a glob is equivalent to specifying this option multiple times, one for each matching ref name. See also the fetch.negotiationAlgorithm and push.negotiate configuration variables documented in git- config(1), and the --negotiate-only option below. |
| `--no-recurse-submodules` | `` | bool | Disable recursive fetching of submodules (this has the same effect as using the --recurse-submodules=no option). |
| `--no-show-forced-updates` | `` | bool | By default, git checks if a branch is force-updated during fetch. Pass --no-show-forced-updates or set fetch.showForcedUpdates to false to skip this check for performance reasons. If used during git-pull the --ff-only option will still check for forced updates before attempting a fast-forward update. See git- config(1). |
| `--no-tags` | `-n` | string | By default, tags that point at objects that are downloaded from the remote repository are fetched and stored locally. This option disables this automatic tag following. The default behavior for a remote may be specified with the remote.<name>.tagOpt setting. See git-config(1). |
| `--porcelain` | `` | string | Print the output to standard output in an easy-to-parse format for scripts. See section OUTPUT in git- fetch(1) for details. This is incompatible with --recurse-submodules=[yes|on-demand] and takes precedence over the fetch.output config option. |
| `--prefetch` | `` | string | Modify the configured refspec to place all refs into the refs/prefetch/ namespace. See the prefetch task in git-maintenance(1). |
| `--progress` | `` | bool | Progress status is reported on the standard error stream by default when it is attached to a terminal, unless -q is specified. This flag forces progress status even if the standard error stream is not directed to a terminal. |
| `--prune` | `-p` | bool | Before fetching, remove any remote-tracking references that no longer exist on the remote. Tags are not subject to pruning if they are fetched only because of the default tag auto-following or due to a --tags option. However, if tags are fetched due to an explicit refspec (either on the command line or in the remote configuration, for example if the remote was cloned with the --mirror option), then they are also subject to pruning. Supplying --prune-tags is a shorthand for providing the tag refspec. See the PRUNING section below for more details. |
| `--prune-tags` | `-P` | bool | Before fetching, remove any local tags that no longer exist on the remote if --prune is enabled. This option should be used more carefully, unlike --prune it will remove any local references (local tags) that have been created. This option is a shorthand for providing the explicit tag refspec along with --prune, see the discussion about that in its documentation. See the PRUNING section below for more details. |
| `--quiet` | `-q` | bool | Pass --quiet to git-fetch-pack and silence any other internally used git commands. Progress is not reported to the standard error stream. |
| `--refetch` | `` | bool | Instead of negotiating with the server to avoid transferring commits and associated objects that are already present locally, this option fetches all objects as a fresh clone would. Use this to reapply a partial clone filter from configuration or using --filter= when the filter definition has changed. Automatic post-fetch maintenance will perform object database pack consolidation to remove any duplicate objects. |
| `--refmap` | `` | string | When fetching refs listed on the command line, use the specified refspec (can be given more than once) to map the refs to remote-tracking branches, instead of the values of remote.*.fetch configuration variables for the remote repository. Providing an empty <refspec> to the --refmap option causes Git to ignore the configured refspecs and rely entirely on the refspecs supplied as command-line arguments. See section on "Configured Remote-tracking Branches" for details. |
| `--set-upstream` | `` | string | If the remote is fetched successfully, add upstream (tracking) reference, used by argument-less git- pull(1) and other commands. For more information, see branch.<name>.merge and branch.<name>.remote in git- config(1). |
| `--shallow-exclude` | `` | string | Deepen or shorten the history of a shallow repository to exclude commits reachable from a specified remote branch or tag. This option can be specified multiple times. |
| `--shallow-since` | `` | string | Deepen or shorten the history of a shallow repository to include all reachable commits after <date>. |
| `--show-forced-updates` | `` | bool | By default, git checks if a branch is force-updated during fetch. This can be disabled through fetch.showForcedUpdates, but the --show-forced-updates option guarantees this check occurs. See git- config(1). |
| `--stdin` | `` | string | Read refspecs, one per line, from stdin in addition to those provided as arguments. The "tag <name>" format is not supported. |
| `--submodule-prefix` | `` | string | Prepend <path> to paths printed in informative messages such as "Fetching submodule foo". This option is used internally when recursing over submodules. |
| `--tags` | `-t` | string | Fetch all tags from the remote (i.e., fetch remote tags refs/tags/* into local tags with the same name), in addition to whatever else would otherwise be fetched. Using this option alone does not subject tags to pruning, even if --prune is used (though tags may be pruned anyway if they are also the destination of an explicit refspec; see --prune). |
| `--unshallow` | `` | bool | If the source repository is complete, convert a shallow repository to a complete one, removing all the limitations imposed by shallow repositories. If the source repository is shallow, fetch as much as possible so that the current repository has the same history as the source repository. |
| `--update-head-ok` | `-u` | bool | By default git fetch refuses to update the head which corresponds to the current branch. This flag disables the check. This is purely for the internal use for git pull to communicate with git fetch, and unless you are implementing your own Porcelain you are not supposed to use it. |
| `--update-shallow` | `` | bool | By default when fetching from a shallow repository, git fetch refuses refs that require updating .git/shallow. This option updates .git/shallow and accepts such refs. |
| `--upload-pack` | `` | string | When given, and the repository to fetch from is handled by git fetch-pack, --exec=<upload-pack> is passed to the command to specify non-default path for the command run on the other end. |
| `--verbose` | `-v` | bool | Be verbose. |

### `git grep`

Print lines matching a pattern

```
git grep [-a | --text] [-I] [--textconv] [-i | --ignore-case] [-w | --word-regexp] [-v | --invert-match] [-h|-H] [--full-name] [-E | --extended-regexp] [-G | --basic-regexp] [-P | --perl-regexp] [-F | --fixed-strings] [-n | --line-number] [--column] [-l | --files-with-matches] [-L | --files-without-match] [(-O | --open-files-in-pager) [<pager>]] [-z | --null] [ -o | --only-matching ] [-c | --count] [--all-match] [-q | --quiet] [--max-depth <depth>] [--[no-]recursive] [--color[=<when>] | --no-color] [--break] [--heading] [-p | --show-function] [-A <post-context>] [-B <pre-context>] [-C <context>] [-W | --function-context] [(-m | --max-count) <num>] [--threads <num>] [-f <file>] [-e] <pattern> [--and|--or|--not|(|)|-e <pattern>...] [--recurse-submodules] [--parent-basename <basename>] [ [--[no-]exclude-standard] [--cached | --no-index | --untracked] | <tree>...] [--] [<pathspec>...]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--all-match` | `` | string | When giving multiple pattern expressions combined with --or, this flag is specified to limit the match to files that have lines to match all of them. |
| `--break` | `` | string | Print an empty line between matches from different files. |
| `--cached` | `` | string | Instead of searching tracked files in the working tree, search blobs registered in the index file. |
| `--column` | `` | bool | Prefix the 1-indexed byte-offset of the first match from the start of the matching line. |
| `--count` | `-c` | string | Instead of showing every matched line, show the number of lines that match. |
| `--exclude-standard` | `` | string | Do not pay attention to ignored files specified via the .gitignore mechanism. Only useful when searching files in the current directory with --no-index. |
| `--fixed-strings` | `-F` | bool | Use fixed strings for patterns (don't interpret pattern as a regex). |
| `--full-name` | `` | string | When run from a subdirectory, the command usually outputs paths relative to the current directory. This option forces paths to be output relative to the project top directory. |
| `--function-context` | `-W` | string | Show the surrounding text from the previous line containing a function name up to the one before the next function name, effectively showing the whole function in which the match was found. The function names are determined in the same way as git diff works out patch hunk headers (see Defining a custom hunk-header in gitattributes(5)). |
| `--heading` | `` | string | Show the filename above the matches in that file instead of at the start of each shown line. |
| `--ignore-case` | `-i` | string | Ignore case differences between the patterns and the files. |
| `--invert-match` | `-v` | bool | Select non-matching lines. |
| `--line-number` | `-n` | string | Prefix the line number to matching lines. |
| `--max-depth` | `` | string | For each <pathspec> given on command line, descend at most <depth> levels of directories. A value of -1 means no limit. This option is ignored if <pathspec> contains active wildcards. In other words if "a*" matches a directory named "a*", "*" is matched literally so --max-depth is still effective. |
| `--no-color` | `` | string | Turn off match highlighting, even when the configuration file gives the default to color output. Same as --color=never. |
| `--no-exclude-standard` | `` | string | Also search in ignored files by not honoring the .gitignore mechanism. Only useful with --untracked. |
| `--no-index` | `` | string | Search files in the current directory that is not managed by Git. |
| `--no-recursive` | `` | bool | Same as --max-depth=0. |
| `--no-textconv` | `` | bool | Do not honor textconv filter settings. This is the default. |
| `--null` | `-z` | string | Use \0 as the delimiter for pathnames in the output, and print them verbatim. Without this option, pathnames with "unusual" characters are quoted as explained for the configuration variable core.quotePath (see git-config(1)). |
| `--only-matching` | `-o` | bool | Print only the matched (non-empty) parts of a matching line, with each such part on a separate output line. |
| `--perl-regexp` | `-P` | bool | Use Perl-compatible regular expressions for patterns. Support for these types of regular expressions is an optional compile-time dependency. If Git wasn't compiled with support for them providing this option will cause it to die. |
| `--quiet` | `-q` | bool | Do not output matched lines; instead, exit with status 0 when there is a match and with non-zero status when there isn't. |
| `--recurse-submodules` | `` | string | Recursively search in each submodule that is active and checked out in the repository. When used in combination with the <tree> option the prefix of all submodule output will be the name of the parent project's <tree> object. This option has no effect if --no-index is given. |
| `--recursive` | `-r` | bool | Same as --max-depth=-1; this is the default. |
| `--show-function` | `-p` | string | Show the preceding line that contains the function name of the match, unless the matching line is a function name itself. The name is determined in the same way as git diff works out patch hunk headers (see Defining a custom hunk-header in gitattributes(5)). |
| `--text` | `-a` | string | Process binary files as if they were text. |
| `--textconv` | `` | bool | Honor textconv filter settings. |
| `--threads` | `` | string | Number of grep worker threads to use. See grep.threads in CONFIGURATION for more information. |
| `--untracked` | `` | string | In addition to searching in the tracked files in the working tree, search also in untracked files. |
| `--word-regexp` | `-w` | bool | Match the pattern only at word boundary (either begin at the beginning of a line, or preceded by a non-word character; end at the end of a line or followed by a non-word character). |
| `-I` | `-I` | bool | Don't match the pattern in binary files. |
| `-e` | `-e` | bool | The next parameter is the pattern. This option has to be used for patterns starting with - and should be used in scripts passing user input to grep. Multiple patterns are combined by or. |

### `git init`

Create an empty Git repository or reinitialize an existing one

```
git init [-q | --quiet] [--bare] [--template=<template-directory>] [--separate-git-dir <git-dir>] [--object-format=<format>] [-b <branch-name> | --initial-branch=<branch-name>] [--shared[=<permissions>]] [<directory>]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--bare` | `` | string | Create a bare repository. If GIT_DIR environment is not set, it is set to the current working directory. |
| `--object-format` | `` | string | Specify the given object format (hash algorithm) for the repository. The valid values are sha1 and (if enabled) sha256.  sha1 is the default. Note: At present, there is no interoperability between SHA-256 repositories and SHA-1 repositories. |
| `--quiet` | `-q` | bool | Only print error and warning messages; all other output will be suppressed. |
| `--separate-git-dir` | `` | string | Instead of initializing the repository as a directory to either $GIT_DIR or ./.git/, create a text file there containing the path to the actual repository. This file acts as a filesystem-agnostic Git symbolic link to the repository. If this is a reinitialization, the repository will be moved to the specified path. |
| `--template` | `` | string | Specify the directory from which templates will be used. (See the "TEMPLATE DIRECTORY" section below.) |

### `git log`

Show commit logs

```
git log [<options>] [<revision-range>] [[--] <path>...]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--abbrev-commit` | `` | string | Instead of showing the full 40-byte hexadecimal commit object name, show a prefix that names the object uniquely. "--abbrev=<n>" (which also modifies diff output, if it is displayed) option can be used to specify the minimum length of the prefix. This should make "--pretty=oneline" a whole lot more readable for people using 80-column terminals. |
| `--all` | `` | bool | Pretend as if all the refs in refs/, along with HEAD, are listed on the command line as <commit>. |
| `--all-match` | `` | bool | Limit the commits output to ones that match all given --grep, instead of ones that match at least one. |
| `--alternate-refs` | `` | string | Pretend as if all objects mentioned as ref tips of alternate repositories were listed on the command line. An alternate repository is any repository whose object directory is specified in objects/info/alternates. The set of included objects may be modified by core.alternateRefsCommand, etc. See git-config(1). |
| `--author-date-order` | `` | bool | Show no parents before all of its children are shown, but otherwise show commits in the author timestamp order. |
| `--basic-regexp` | `` | bool | Consider the limiting patterns to be basic regular expressions; this is the default. |
| `--bisect` | `` | bool | Pretend as if the bad bisection ref refs/bisect/bad was listed and as if it was followed by --not and the good bisection refs refs/bisect/good-* on the command line. |
| `--boundary` | `` | bool | Output excluded boundary commits. Boundary commits are prefixed with -. |
| `--cherry` | `` | bool | A synonym for --right-only --cherry-mark --no-merges; useful to limit the output to the commits on our side and mark those that have been applied to the other side of a forked history with git log --cherry upstream...mybranch, similar to git cherry upstream mybranch. |
| `--cherry-mark` | `` | bool | Like --cherry-pick (see below) but mark equivalent commits with = rather than omitting them, and inequivalent ones with +. |
| `--cherry-pick` | `` | bool | Omit any commit that introduces the same change as another commit on the "other side" when the set of commits are limited with symmetric difference. For example, if you have two branches, A and B, a usual way to list all commits on only one side of them is with --left-right (see the example below in the description of the --left-right option). However, it shows the commits that were cherry-picked from the other branch (for example, "3rd on b" may be cherry-picked from branch A). With this option, such pairs of commits are excluded from the output. |
| `--children` | `` | bool | Print also the children of the commit (in the form "commit child..."). Also enables parent rewriting, see History Simplification above. |
| `--clear-decorations` | `` | string | When specified, this option clears all previous --decorate-refs or --decorate-refs-exclude options and relaxes the default decoration filter to include all references. This option is assumed if the config value log.initialDecorationSet is set to all. |
| `--date` | `` | string | Only takes effect for dates shown in human-readable format, such as when using --pretty.  log.date config variable sets a default value for the log command's --date option. By default, dates are shown in the original time zone (either committer's or author's). If -local is appended to the format (e.g., iso-local), the user's local time zone is used instead. --date=relative shows dates relative to the current time, e.g. "2 hours ago". The -local option has no effect for --date=relative. --date=local is an alias for --date=default-local. --date=iso (or --date=iso8601) shows timestamps in a ISO 8601-like format. The differences to the strict ISO 8601 format are: o   a space instead of the T date/time delimiter o   a space between time and time zone o   no colon between hours and minutes of the time zone --date=iso-strict (or --date=iso8601-strict) shows timestamps in strict ISO 8601 format. --date=rfc (or --date=rfc2822) shows timestamps in RFC 2822 format, often found in email messages. --date=short shows only the date, but not the time, in YYYY-MM-DD format. --date=raw shows the date as seconds since the epoch (1970-01-01 00:00:00 UTC), followed by a space, and then the timezone as an offset from UTC (a + or - with four digits; the first two are hours, and the second two are minutes). I.e., as if the timestamp were formatted with strftime("%s %z")). Note that the -local option does not affect the seconds-since-epoch value (which is always measured in UTC), but does switch the accompanying timezone value. --date=human shows the timezone if the timezone does not match the current time-zone, and doesn't print the whole date if that matches (ie skip printing year for dates that are "this year", but also skip the whole date itself if it's in the last few days and we can just say what weekday it was). For older dates the hour and minute is also omitted. --date=unix shows the date as a Unix epoch timestamp (seconds since 1970). As with --raw, this is always in UTC and therefore -local has no effect. --date=format:...  feeds the format ...  to your system strftime, except for %s, %z, and %Z, which are handled internally. Use --date=format:%c to show the date in your system locale's preferred format. See the strftime manual for a complete list of format placeholders. When using -local, the correct syntax is --date=format-local:.... --date=default is the default format, and is based on ctime(3) output. It shows a single line with three-letter day of the week, three-letter month, day-of-month, hour-minute-seconds in "HH:MM:SS" format, followed by 4-digit year, plus timezone information, unless the local time zone is used, e.g.  Thu Jan 1 00:00:00 1970 +0000. |
| `--date-order` | `` | bool | Show no parents before all of its children are shown, but otherwise show commits in the commit timestamp order. |
| `--dense` | `` | bool | Only the selected commits are shown, plus some to have a meaningful history. |
| `--dense` | `` | bool | Commits that are walked are included if they are not TREESAME to any parent. |
| `--do-walk` | `` | bool | Overrides a previous --no-walk. |
| `--encoding` | `` | string | Commit objects record the character encoding used for the log message in their encoding header; this option can be used to tell the command to re-code the commit log message in the encoding preferred by the user. For non plumbing commands this defaults to UTF-8. Note that if an object claims to be encoded in X and we are outputting in X, we will output the object verbatim; this means that invalid sequences in the original commit may be copied to the output. Likewise, if iconv(3) fails to convert the commit, we will quietly output the original object verbatim. |
| `--exclude` | `` | string | Do not include refs matching <glob-pattern> that the next --all, --branches, --tags, --remotes, or --glob would otherwise consider. Repetitions of this option accumulate exclusion patterns up to the next --all, --branches, --tags, --remotes, or --glob option (other options or arguments do not clear accumulated patterns). The patterns given should not begin with refs/heads, refs/tags, or refs/remotes when applied to --branches, --tags, or --remotes, respectively, and they must begin with refs/ when applied to --glob or --all. If a trailing /* is intended, it must be given explicitly. |
| `--exclude-first-parent-only` | `` | bool | When finding commits to exclude (with a ^), follow only the first parent commit upon seeing a merge commit. This can be used to find the set of changes in a topic branch from the point where it diverged from the remote branch, given that arbitrary merges can be valid topic branch changes. |
| `--extended-regexp` | `-E` | bool | Consider the limiting patterns to be extended regular expressions instead of the default basic regular expressions. |
| `--first-parent` | `` | string | When finding commits to include, follow only the first parent commit upon seeing a merge commit. This option can give a better overview when viewing the evolution of a particular topic branch, because merges into a topic branch tend to be only about adjusting to updated upstream from time to time, and this option allows you to ignore the individual commits brought in to your history by such a merge. This option also changes default diff format for merge commits to first-parent, see --diff-merges=first-parent for details. |
| `--fixed-strings` | `-F` | bool | Consider the limiting patterns to be fixed strings (don't interpret pattern as a regular expression). |
| `--follow` | `` | string | Continue listing the history of a file beyond renames (works only for a single file). |
| `--full-diff` | `` | string | Without this flag, git log -p <path>...  shows commits that touch the specified paths, and diffs about the same specified paths. With this, the full diff is shown for commits that touch the specified paths; this means that "<path>..." limits only commits, and doesn't limit diff for those commits. Note that this affects all diff-based output types, e.g. those produced by --stat, etc. |
| `--full-history` | `` | string | Same as the default mode, but does not prune some history. |
| `--glob` | `` | string | Pretend as if all the refs matching shell glob <glob-pattern> are listed on the command line as <commit>. Leading refs/, is automatically prepended if missing. If pattern lacks ?, *, or [, /* at the end is implied. |
| `--graph` | `` | bool | Draw a text-based graphical representation of the commit history on the left hand side of the output. This may cause extra lines to be printed in between commits, in order for the graph history to be drawn properly. Cannot be combined with --no-walk. This enables parent rewriting, see History Simplification above. This implies the --topo-order option by default, but the --date-order option may also be specified. |
| `--grep` | `` | string | Limit the commits output to ones with a log message that matches the specified pattern (regular expression). With more than one --grep=<pattern>, commits whose message matches any of the given patterns are chosen (but see --all-match). When --notes is in effect, the message from the notes is matched as if it were part of the log message. |
| `--grep-reflog` | `` | string | Limit the commits output to ones with reflog entries that match the specified pattern (regular expression). With more than one --grep-reflog, commits whose reflog message matches any of the given patterns are chosen. It is an error to use this option unless --walk-reflogs is in use. |
| `--ignore-missing` | `` | string | Upon seeing an invalid object name in the input, pretend as if the bad input was not given. |
| `--invert-grep` | `` | bool | Limit the commits output to ones with a log message that do not match the pattern specified with --grep=<pattern>. |
| `--left-only` | `` | bool | List only commits on the respective side of a symmetric difference, i.e. only those which would be marked < resp.  > by --left-right. For example, --cherry-pick --right-only A...B omits those commits from B which are in A or are patch-equivalent to a commit in A. In other words, this lists the + commits from git cherry A B. More precisely, --cherry-pick --right-only --no-merges gives the exact list. |
| `--left-right` | `` | bool | Mark which side of a symmetric difference a commit is reachable from. Commits from the left side are prefixed with < and those from the right with >. If combined with --boundary, those commits are prefixed with -. For example, if you have this topology: y---b---b  branch B / \ / /   . /   / \ o---x---a---a  branch A you would get an output like this: $ git rev-list --left-right --boundary --pretty=oneline A...B >bbbbbbb... 3rd on b >bbbbbbb... 2nd on b <aaaaaaa... 3rd on a <aaaaaaa... 2nd on a -yyyyyyy... 1st on b -xxxxxxx... 1st on a |
| `--log-size` | `` | string | Include a line "log size <number>" in the output for each commit, where <number> is the length of that commit's message in bytes. Intended to speed up tools that read log messages from git log output by allowing them to allocate space in advance. |
| `--merge` | `` | string | After a failed merge, show refs that touch files having a conflict and don't exist on all heads to merge. |
| `--merges` | `` | bool | Print only merge commits. This is exactly the same as --min-parents=2. |
| `--no-abbrev-commit` | `` | string | Show the full 40-byte hexadecimal commit object name. This negates --abbrev-commit, either explicit or implied by other options such as "--oneline". It also overrides the log.abbrevCommit variable. |
| `--no-merges` | `` | bool | Do not print commits with more than one parent. This is exactly the same as --max-parents=1. |
| `--no-notes` | `` | bool | Do not show notes. This negates the above --notes option, by resetting the list of notes refs from which notes are shown. Options are parsed in the order given on the command line, so e.g. "--notes --notes=foo --no-notes --notes=bar" will only show notes from "refs/notes/bar". |
| `--not` | `` | bool | Reverses the meaning of the ^ prefix (or lack thereof) for all following revision specifiers, up to the next --not. When used on the command line before --stdin, the revisions passed through stdin will not be affected by it. Conversely, when passed via standard input, the revisions passed on the command line will not be affected by it. |
| `--oneline` | `` | bool | This is a shorthand for "--pretty=oneline --abbrev-commit" used together. |
| `--parents` | `` | bool | Print also the parents of the commit (in the form "commit parent..."). Also enables parent rewriting, see History Simplification above. |
| `--perl-regexp` | `-P` | bool | Consider the limiting patterns to be Perl-compatible regular expressions. Support for these types of regular expressions is an optional compile-time dependency. If Git wasn't compiled with support for them providing this option will cause it to die. |
| `--reflog` | `` | bool | Pretend as if all objects mentioned by reflogs are listed on the command line as <commit>. |
| `--regexp-ignore-case` | `-i` | bool | Match the regular expression limiting patterns without regard to letter case. |
| `--relative-date` | `` | bool | Synonym for --date=relative. |
| `--remove-empty` | `` | string | Stop when a given path disappears from the tree. |
| `--reverse` | `` | bool | Output the commits chosen to be shown (see Commit Limiting section above) in reverse order. Cannot be combined with --walk-reflogs. |
| `--show-notes-by-default` | `` | bool | Show the default notes unless options for displaying specific notes are given. |
| `--show-pulls` | `` | string | Include all commits from the default mode, but also any merge commits that are not TREESAME to the first parent but are TREESAME to a later parent. This mode is helpful for showing the merge commits that "first introduced" a change to a branch. |
| `--show-pulls` | `` | string | In addition to the commits shown in the default history, show each merge commit that is not TREESAME to its first parent but is TREESAME to a later parent. When a merge commit is included by --show-pulls, the merge is treated as if it "pulled" the change from another branch. When using --show-pulls on this example (and no other options) the resulting graph is: I---X---R---N Here, the merge commits R and N are included because they pulled the commits X and R into the base branch, respectively. These merges are the reason the commits A and B do not appear in the default history. When --show-pulls is paired with --simplify-merges, the graph includes all of the necessary information: .-A---M--.   N /     /    \ / I     B      R \   /      / \ /      / `---X--' Notice that since M is reachable from R, the edge from N to M was simplified away. However, N still appears in the history as an important commit because it "pulled" the change R into the main branch. |
| `--show-signature` | `` | bool | Check the validity of a signed commit object by passing the signature to gpg --verify and show the output. |
| `--simplify-by-decoration` | `` | bool | Commits that are referred by some branch or tag are selected. |
| `--simplify-merges` | `` | bool | Additional option to --full-history to remove some needless merges from the resulting history, as there are no selected commits contributing to this merge. |
| `--simplify-merges` | `` | bool | First, build a history graph in the same way that --full-history with parent rewriting does (see above). Then simplify each commit C to its replacement C' in the final history according to the following rules: o   Set C' to C. o   Replace each parent P of C' with its simplification P'. In the process, drop parents that are ancestors of other parents or that are root commits TREESAME to an empty tree, and remove duplicates, but take care to never drop all parents that we are TREESAME to. o   If after this parent rewriting, C' is a root or merge commit (has zero or >1 parents), a boundary commit, or !TREESAME, it remains. Otherwise, it is replaced with its only parent. The effect of this is best shown by way of comparing to --full-history with parent rewriting. The example turns into: .-A---M---N---O /     /       / I     B       D \   /       / `---------' Note the major differences in N, P, and Q over --full-history: o   N's parent list had I removed, because it is an ancestor of the other parent M. Still, N remained because it is !TREESAME. o   P's parent list similarly had I removed.  P was then removed completely, because it had one parent and is TREESAME. o   Q's parent list had Y simplified to X.  X was then removed, because it was a TREESAME root.  Q was then removed completely, because it had one parent and is TREESAME. |
| `--since-as-filter` | `` | string | Show all commits more recent than a specific date. This visits all commits in the range, rather than stopping at the first commit which is older than a specific date. |
| `--single-worktree` | `` | bool | By default, all working trees will be examined by the following options when there are more than one (see git-worktree(1)): --all, --reflog and --indexed-objects. This option forces them to examine the current working tree only. |
| `--skip` | `` | string | Skip number commits before starting to show the commit output. |
| `--source` | `` | string | Print out the ref name given on the command line by which each commit was reached. |
| `--sparse` | `` | bool | All commits in the simplified history are shown. |
| `--sparse` | `` | bool | All commits that are walked are included. Note that without --full-history, this still simplifies merges: if one of the parents is TREESAME, we follow only that one, so the other sides of the merge are never walked. |
| `--stdin` | `` | string | In addition to getting arguments from the command line, read them from standard input as well. This accepts commits and pseudo-options like --all and --glob=. When a -- separator is seen, the following input is treated as paths and used to limit the result. Flags like --not which are read via standard input are only respected for arguments passed in the same way and will not influence any subsequent command line arguments. |
| `--topo-order` | `` | string | Show no parents before all of its children are shown, and avoid showing commits on multiple lines of history intermixed. For example, in a commit history like this: ---1----2----4----7 \              \ 3----5----6----8--- where the numbers denote the order of commit timestamps, git rev-list and friends with --date-order show the commits in the timestamp order: 8 7 6 5 4 3 2 1. With --topo-order, they would show 8 6 5 3 7 4 2 1 (or 8 7 4 2 6 5 3 1); some older commits are shown before newer ones in order to avoid showing the commits from two parallel development track mixed together. |
| `--walk-reflogs` | `-g` | string | Instead of walking the commit ancestry chain, walk reflog entries from the most recent one to older ones. When this option is used you cannot specify commits to exclude (that is, ^commit, commit1..commit2, and commit1...commit2 notations cannot be used). With --pretty format other than oneline and reference (for obvious reasons), this causes the output to have two extra lines of information taken from the reflog. The reflog designator in the output may be shown as ref@{Nth} (where Nth is the reverse-chronological index in the reflog) or as ref@{timestamp} (with the timestamp for that entry), depending on a few rules: 1. If the starting point is specified as ref@{Nth}, show the index format. 2. If the starting point was specified as ref@{now}, show the timestamp format. 3. If neither was used, but --date was given on the command line, show the timestamp in the format requested by --date. 4. Otherwise, show the index format. Under --pretty=oneline, the commit message is prefixed with this information on the same line. This option cannot be combined with --reverse. See also git-reflog(1). Under --pretty=reference, this information will not be shown at all. |

### `git merge`

or: git merge --abort

```
git merge [<options>] [<commit>...]
```

### `git mv`

Move or rename a file, a directory, or a symlink

```
git mv [<options>] <source>... <destination>
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--dry-run` | `-n` | bool | Do nothing; only show what would happen |
| `--force` | `-f` | string | Force renaming or moving of a file even if the <destination> exists. |
| `--verbose` | `-v` | string | Report the names of files as they are moved. |
| `-k` | `-k` | bool | Skip move or rename actions which would lead to an error condition. An error happens when a source is neither existing nor controlled by Git, or when it would overwrite an existing file unless -f is given. |

### `git pull`

Fetch from and integrate with another repository or a local branch

```
git pull [<options>] [<repository> [<refspec>...]]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--all` | `` | bool | Fetch all remotes. |
| `--allow-unrelated-histories` | `` | bool | By default, git merge command refuses to merge histories that do not share a common ancestor. This option can be used to override this safety when merging histories of two projects that started their lives independently. As that is a very rare occasion, no configuration variable to enable this by default exists and will not be added. Only useful when merging. |
| `--append` | `-a` | string | Append ref names and object names of fetched refs to the existing contents of .git/FETCH_HEAD. Without this option old data in .git/FETCH_HEAD will be overwritten. |
| `--atomic` | `` | bool | Use an atomic transaction to update local refs. Either all refs are updated, or on error, no refs are updated. |
| `--autostash` | `` | bool | Automatically create a temporary stash entry before the operation begins, record it in the special ref MERGE_AUTOSTASH and apply it after the operation ends. This means that you can run the operation on a dirty worktree. However, use with care: the final stash application after a successful merge might result in non-trivial conflicts. |
| `--cleanup` | `` | string | This option determines how the merge message will be cleaned up before committing. See git-commit(1) for more details. In addition, if the <mode> is given a value of scissors, scissors will be appended to MERGE_MSG before being passed on to the commit machinery in the case of a merge conflict. |
| `--commit` | `` | bool | Perform the merge and commit the result. This option can be used to override --no-commit. Only useful when merging. With --no-commit perform the merge and stop just before creating a merge commit, to give the user a chance to inspect and further tweak the merge result before committing. Note that fast-forward updates do not create a merge commit and therefore there is no way to stop those merges with --no-commit. Thus, if you want to ensure your branch is not changed or updated by the merge command, use --no-ff with --no-commit. |
| `--deepen` | `` | string | Similar to --depth, except it specifies the number of commits from the current shallow boundary instead of from the tip of each remote branch history. |
| `--depth` | `` | string | Limit fetching to the specified number of commits from the tip of each remote branch history. If fetching to a shallow repository created by git clone with --depth=<depth> option (see git-clone(1)), deepen or shorten the history to the specified number of commits. Tags for the deepened commits are not fetched. |
| `--dry-run` | `` | bool | Show what would be done, without making any changes. |
| `--ff` | `` | bool | When merging rather than rebasing, specifies how a merge is handled when the merged-in history is already a descendant of the current history. If merging is requested, --ff is the default unless merging an annotated (and possibly signed) tag that is not stored in its natural place in the refs/tags/ hierarchy, in which case --no-ff is assumed. With --ff, when possible resolve the merge as a fast-forward (only update the branch pointer to match the merged branch; do not create a merge commit). When not possible (when the merged-in history is not a descendant of the current history), create a merge commit. With --no-ff, create a merge commit in all cases, even when the merge could instead be resolved as a fast-forward. |
| `--ff-only` | `` | bool | Only update to the new history if there is no divergent local history. This is the default when no method for reconciling divergent histories is provided (via the --rebase=* flags). |
| `--force` | `-f` | bool | When git fetch is used with <src>:<dst> refspec, it may refuse to update the local branch as discussed in the <refspec> part of the git-fetch(1) documentation. This option overrides that check. |
| `--ipv4` | `-4` | bool | Use IPv4 addresses only, ignoring IPv6 addresses. |
| `--ipv6` | `-6` | bool | Use IPv6 addresses only, ignoring IPv4 addresses. |
| `--jobs` | `-j` | string | Number of parallel children to be used for all forms of fetching. If the --multiple option was specified, the different remotes will be fetched in parallel. If multiple submodules are fetched, they will be fetched in parallel. To control them independently, use the config settings fetch.parallel and submodule.fetchJobs (see git-config(1)). Typically, parallel recursive and multi-remote fetches will be faster. By default fetches are performed sequentially, not in parallel. |
| `--keep` | `-k` | bool | Keep downloaded pack. |
| `--negotiate-only` | `` | bool | Do not fetch anything from the server, and instead print the ancestors of the provided --negotiation-tip=* arguments, which we have in common with the server. This is incompatible with --recurse-submodules=[yes|on-demand]. Internally this is used to implement the push.negotiate option, see git-config(1). |
| `--negotiation-tip` | `` | string | By default, Git will report, to the server, commits reachable from all local refs to find common commits in an attempt to reduce the size of the to-be-received packfile. If specified, Git will only report commits reachable from the given tips. This is useful to speed up fetches when the user knows which local ref is likely to have commits in common with the upstream ref being fetched. This option may be specified more than once; if so, Git will report commits reachable from any of the given commits. The argument to this option may be a glob on ref names, a ref, or the (possibly abbreviated) SHA-1 of a commit. Specifying a glob is equivalent to specifying this option multiple times, one for each matching ref name. See also the fetch.negotiationAlgorithm and push.negotiate configuration variables documented in git- config(1), and the --negotiate-only option below. |
| `--no-rebase` | `` | bool | This is shorthand for --rebase=false. |
| `--no-show-forced-updates` | `` | bool | By default, git checks if a branch is force-updated during fetch. Pass --no-show-forced-updates or set fetch.showForcedUpdates to false to skip this check for performance reasons. If used during git-pull the --ff-only option will still check for forced updates before attempting a fast-forward update. See git- config(1). |
| `--no-tags` | `` | string | By default, tags that point at objects that are downloaded from the remote repository are fetched and stored locally. This option disables this automatic tag following. The default behavior for a remote may be specified with the remote.<name>.tagOpt setting. See git-config(1). |
| `--porcelain` | `` | string | Print the output to standard output in an easy-to-parse format for scripts. See section OUTPUT in git- fetch(1) for details. This is incompatible with --recurse-submodules=[yes|on-demand] and takes precedence over the fetch.output config option. |
| `--prefetch` | `` | string | Modify the configured refspec to place all refs into the refs/prefetch/ namespace. See the prefetch task in git-maintenance(1). |
| `--progress` | `` | bool | Progress status is reported on the standard error stream by default when it is attached to a terminal, unless -q is specified. This flag forces progress status even if the standard error stream is not directed to a terminal. |
| `--prune` | `-p` | bool | Before fetching, remove any remote-tracking references that no longer exist on the remote. Tags are not subject to pruning if they are fetched only because of the default tag auto-following or due to a --tags option. However, if tags are fetched due to an explicit refspec (either on the command line or in the remote configuration, for example if the remote was cloned with the --mirror option), then they are also subject to pruning. Supplying --prune-tags is a shorthand for providing the tag refspec. |
| `--quiet` | `-q` | bool | This is passed to both underlying git-fetch to squelch reporting of during transfer, and underlying git-merge to squelch output during merging. |
| `--refmap` | `` | string | When fetching refs listed on the command line, use the specified refspec (can be given more than once) to map the refs to remote-tracking branches, instead of the values of remote.*.fetch configuration variables for the remote repository. Providing an empty <refspec> to the --refmap option causes Git to ignore the configured refspecs and rely entirely on the refspecs supplied as command-line arguments. See section on "Configured Remote-tracking Branches" for details. |
| `--set-upstream` | `` | string | If the remote is fetched successfully, add upstream (tracking) reference, used by argument-less git- pull(1) and other commands. For more information, see branch.<name>.merge and branch.<name>.remote in git- config(1). |
| `--shallow-exclude` | `` | string | Deepen or shorten the history of a shallow repository to exclude commits reachable from a specified remote branch or tag. This option can be specified multiple times. |
| `--shallow-since` | `` | string | Deepen or shorten the history of a shallow repository to include all reachable commits after <date>. |
| `--show-forced-updates` | `` | bool | By default, git checks if a branch is force-updated during fetch. This can be disabled through fetch.showForcedUpdates, but the --show-forced-updates option guarantees this check occurs. See git- config(1). |
| `--signoff` | `` | bool | Add a Signed-off-by trailer by the committer at the end of the commit log message. The meaning of a signoff depends on the project to which you're committing. For example, it may certify that the committer has the rights to submit the work under the project's license or agrees to some contributor representation, such as a Developer Certificate of Origin. (See http://developercertificate.org for the one used by the Linux kernel and Git projects.) Consult the documentation or leadership of the project to which you're contributing to understand how the signoffs are used in that project. The --no-signoff option can be used to countermand an earlier --signoff option on the command line. |
| `--squash` | `` | string | Produce the working tree and index state as if a real merge happened (except for the merge information), but do not actually make a commit, move the HEAD, or record $GIT_DIR/MERGE_HEAD (to cause the next git commit command to create a merge commit). This allows you to create a single commit on top of the current branch whose effect is the same as merging another branch (or more in case of an octopus). With --no-squash perform the merge and commit the result. This option can be used to override --squash. With --squash, --commit is not allowed, and will fail. Only useful when merging. |
| `--summary` | `` | bool | Synonyms to --stat and --no-stat; these are deprecated and will be removed in the future. |
| `--tags` | `-t` | string | Fetch all tags from the remote (i.e., fetch remote tags refs/tags/* into local tags with the same name), in addition to whatever else would otherwise be fetched. Using this option alone does not subject tags to pruning, even if --prune is used (though tags may be pruned anyway if they are also the destination of an explicit refspec; see --prune). |
| `--unshallow` | `` | bool | If the source repository is complete, convert a shallow repository to a complete one, removing all the limitations imposed by shallow repositories. If the source repository is shallow, fetch as much as possible so that the current repository has the same history as the source repository. |
| `--update-shallow` | `` | bool | By default when fetching from a shallow repository, git fetch refuses refs that require updating .git/shallow. This option updates .git/shallow and accepts such refs. |
| `--upload-pack` | `` | string | When given, and the repository to fetch from is handled by git fetch-pack, --exec=<upload-pack> is passed to the command to specify non-default path for the command run on the other end. |
| `--verbose` | `-v` | bool | Pass --verbose to git-fetch and git-merge. |
| `--verify-signatures` | `` | string | Verify that the tip commit of the side branch being merged is signed with a valid key, i.e. a key that has a valid uid: in the default trust model, this means the signing key has been signed by a trusted key. If the tip commit of the side branch is not signed with a valid key, the merge is aborted. Only useful when merging. |

### `git push`

Update remote refs along with associated objects

```
git push [--all | --branches | --mirror | --tags] [--follow-tags] [--atomic] [-n | --dry-run] [--receive-pack=<git-receive-pack>] [--repo=<repository>] [-f | --force] [-d | --delete] [--prune] [-q | --quiet] [-v | --verbose] [-u | --set-upstream] [-o <string> | --push-option=<string>] [--[no-]signed|--signed=(true|false|if-asked)] [--force-with-lease[=<refname>[:<expect>]] [--force-if-includes]] [--no-verify] [<repository> [<refspec>...]]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--all` | `` | bool | Push all branches (i.e. refs under refs/heads/); cannot be used with other <refspec>. |
| `--delete` | `-d` | bool | All listed refs are deleted from the remote repository. This is the same as prefixing all refs with a colon. |
| `--dry-run` | `-n` | bool | Do everything except actually send the updates. |
| `--follow-tags` | `` | string | Push all the refs that would be pushed without this option, and also push annotated tags in refs/tags that are missing from the remote but are pointing at commit-ish that are reachable from the refs being pushed. This can also be specified with configuration variable push.followTags. For more information, see push.followTags in git-config(1). |
| `--force` | `-f` | string | Usually, the command refuses to update a remote ref that is not an ancestor of the local ref used to overwrite it. Also, when --force-with-lease option is used, the command refuses to update a remote ref whose current value does not match what is expected. This flag disables these checks, and can cause the remote repository to lose commits; use it with care. Note that --force applies to all the refs that are pushed, hence using it with push.default set to matching or with multiple push destinations configured with remote.*.push may overwrite refs other than the current branch (including local refs that are strictly behind their remote counterpart). To force a push to only one branch, use a + in front of the refspec to push (e.g git push origin +master to force a push to the master branch). See the <refspec>...  section above for details. |
| `--ipv4` | `-4` | bool | Use IPv4 addresses only, ignoring IPv6 addresses. |
| `--ipv6` | `-6` | bool | Use IPv6 addresses only, ignoring IPv4 addresses. |
| `--mirror` | `` | bool | Instead of naming each ref to push, specifies that all refs under refs/ (which includes but is not limited to refs/heads/, refs/remotes/, and refs/tags/) be mirrored to the remote repository. Newly created local refs will be pushed to the remote end, locally updated refs will be force updated on the remote end, and deleted refs will be removed from the remote end. This is the default if the configuration option remote.<remote>.mirror is set. |
| `--porcelain` | `` | string | Produce machine-readable output. The output status line for each ref will be tab-separated and sent to stdout instead of stderr. The full symbolic names of the refs will be given. |
| `--progress` | `` | bool | Progress status is reported on the standard error stream by default when it is attached to a terminal, unless -q is specified. This flag forces progress status even if the standard error stream is not directed to a terminal. |
| `--prune` | `` | string | Remove remote branches that don't have a local counterpart. For example a remote branch tmp will be removed if a local branch with the same name doesn't exist any more. This also respects refspecs, e.g. git push --prune remote refs/heads/*:refs/tmp/* would make sure that remote refs/tmp/foo will be removed if refs/heads/foo doesn't exist. |
| `--quiet` | `-q` | bool | Suppress all output, including the listing of updated refs, unless an error occurs. Progress is not reported to the standard error stream. |
| `--repo` | `` | string | This option is equivalent to the <repository> argument. If both are specified, the command-line argument takes precedence. |
| `--set-upstream` | `-u` | string | For every branch that is up to date or successfully pushed, add upstream (tracking) reference, used by argument-less git-pull(1) and other commands. For more information, see branch.<name>.merge in git- config(1). |
| `--tags` | `` | bool | All refs under refs/tags are pushed, in addition to refspecs explicitly listed on the command line. |
| `--verbose` | `-v` | bool | Run verbosely. |

### `git rebase`

Reapply commits on top of another base tip

```
git rebase [-i | --interactive] [<options>] [--exec <cmd>] [--onto <newbase> | --keep-base] [<upstream> [<branch>]] git rebase [-i | --interactive] [<options>] [--exec <cmd>] [--onto <newbase>] --root [<branch>] git rebase (--continue | --skip | --abort | --quit | --edit-todo | --show-current-patch)
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--allow-empty-message` | `` | bool | No-op. Rebasing commits with an empty message used to fail and this option would override that behavior, allowing commits with empty messages to be rebased. Now commits with an empty message do not cause rebasing to halt. See also INCOMPATIBLE OPTIONS below. |
| `--apply` | `` | bool | Use applying strategies to rebase (calling git-am internally). This option may become a no-op in the future once the merge backend handles everything the apply one does. See also INCOMPATIBLE OPTIONS below. |
| `--autosquash` | `` | bool | When the commit log message begins with "squash! ..." or "fixup! ..." or "amend! ...", and there is already a commit in the todo list that matches the same ..., automatically modify the todo list of rebase -i, so that the commit marked for squashing comes right after the commit to be modified, and change the action of the moved commit from pick to squash or fixup or fixup -C respectively. A commit matches the ... if the commit subject matches, or if the ...  refers to the commit's hash. As a fall-back, partial matches of the commit subject work, too. The recommended way to create fixup/amend/squash commits is by using the --fixup, --fixup=amend: or --fixup=reword: and --squash options respectively of git-commit(1). If the --autosquash option is enabled by default using the configuration variable rebase.autoSquash, this option can be used to override and disable this setting. See also INCOMPATIBLE OPTIONS below. |
| `--autostash` | `` | bool | Automatically create a temporary stash entry before the operation begins, and apply it after the operation ends. This means that you can run rebase on a dirty worktree. However, use with care: the final stash application after a successful rebase might result in non-trivial conflicts. |
| `--committer-date-is-author-date` | `` | bool | Instead of using the current time as the committer date, use the author date of the commit being rebased as the committer date. This option implies --force-rebase. |
| `--fork-point` | `` | bool | Use reflog to find a better common ancestor between <upstream> and <branch> when calculating which commits have been introduced by <branch>. When --fork-point is active, fork_point will be used instead of <upstream> to calculate the set of commits to rebase, where fork_point is the result of git merge-base --fork-point <upstream> <branch> command (see git-merge-base(1)). If fork_point ends up being empty, the <upstream> will be used as a fallback. If <upstream> or --keep-base is given on the command line, then the default is --no-fork-point, otherwise the default is --fork-point. See also rebase.forkpoint in git-config(1). If your branch was based on <upstream> but <upstream> was rewound and your branch contains commits which were dropped, this option can be used with --keep-base in order to drop those commits from your branch. See also INCOMPATIBLE OPTIONS below. |
| `--ignore-date` | `` | bool | Instead of using the author date of the original commit, use the current time as the author date of the rebased commit. This option implies --force-rebase. See also INCOMPATIBLE OPTIONS below. |
| `--ignore-whitespace` | `` | string | Ignore whitespace differences when trying to reconcile differences. Currently, each backend implements an approximation of this behavior: apply backend When applying a patch, ignore changes in whitespace in context lines. Unfortunately, this means that if the "old" lines being replaced by the patch differ only in whitespace from the existing file, you will get a merge conflict instead of a successful patch application. merge backend Treat lines with only whitespace changes as unchanged when merging. Unfortunately, this means that any patch hunks that were intended to modify whitespace and nothing else will be dropped, even if the other side had no changes that conflicted. |
| `--interactive` | `-i` | string | Make a list of the commits which are about to be rebased. Let the user edit that list before rebasing. This mode can also be used to split commits (see SPLITTING COMMITS below). The commit list format can be changed by setting the configuration option rebase.instructionFormat. A customized instruction format will automatically have the long commit hash prepended to the format. See also INCOMPATIBLE OPTIONS below. |
| `--keep-base` | `` | bool | Set the starting point at which to create the new commits to the merge base of <upstream> and <branch>. Running git rebase --keep-base <upstream> <branch> is equivalent to running git rebase --reapply-cherry-picks --no-fork-point --onto <upstream>...<branch> <upstream> <branch>. This option is useful in the case where one is developing a feature on top of an upstream branch. While the feature is being worked on, the upstream branch may advance and it may not be the best idea to keep rebasing on top of the upstream but to keep the base commit as-is. As the base commit is unchanged this option implies --reapply-cherry-picks to avoid losing commits. Although both this option and --fork-point find the merge base between <upstream> and <branch>, this option uses the merge base as the starting point on which new commits will be created, whereas --fork-point uses the merge base to determine the set of commits which will be rebased. See also INCOMPATIBLE OPTIONS below. |
| `--merge` | `-m` | bool | Using merging strategies to rebase (default). Note that a rebase merge works by replaying each commit from the working branch on top of the <upstream> branch. Because of this, when a merge conflict happens, the side reported as ours is the so-far rebased series, starting with <upstream>, and theirs is the working branch. In other words, the sides are swapped. See also INCOMPATIBLE OPTIONS below. |
| `--no-keep-empty` | `` | bool | Do not keep commits that start empty before the rebase (i.e. that do not change anything from its parent) in the result. The default is to keep commits which start empty, since creating such commits requires passing the --allow-empty override flag to git commit, signifying that a user is very intentionally creating such a commit and thus wants to keep it. Usage of this flag will probably be rare, since you can get rid of commits that start empty by just firing up an interactive rebase and removing the lines corresponding to the commits you don't want. This flag exists as a convenient shortcut, such as for cases where external tools generate many empty commits and you want them all removed. For commits which do not start empty but become empty after rebasing, see the --empty flag. See also INCOMPATIBLE OPTIONS below. |
| `--no-stat` | `-n` | bool | Do not show a diffstat as part of the rebase process. |
| `--no-verify` | `` | bool | This option bypasses the pre-rebase hook. See also githooks(5). |
| `--onto` | `` | string | Starting point at which to create the new commits. If the --onto option is not specified, the starting point is <upstream>. May be any valid commit, and not just an existing branch name. As a special case, you may use "A...B" as a shortcut for the merge base of A and B if there is exactly one merge base. You can leave out at most one of A and B, in which case it defaults to HEAD. |
| `--quiet` | `-q` | bool | Be quiet. Implies --no-stat. |
| `--reapply-cherry-picks` | `` | string | Reapply all clean cherry-picks of any upstream commit instead of preemptively dropping them. (If these commits then become empty after rebasing, because they contain a subset of already upstream changes, the behavior towards them is controlled by the --empty flag.) In the absence of --keep-base (or if --no-reapply-cherry-picks is given), these commits will be automatically dropped. Because this necessitates reading all upstream commits, this can be expensive in repositories with a large number of upstream commits that need to be read. When using the merge backend, warnings will be issued for each dropped commit (unless --quiet is given). Advice will also be issued unless advice.skippedCherryPicks is set to false (see git-config(1)). --reapply-cherry-picks allows rebase to forgo reading all upstream commits, potentially improving performance. See also INCOMPATIBLE OPTIONS below. |
| `--rerere-autoupdate` | `` | string | After the rerere mechanism reuses a recorded resolution on the current conflict to update the files in the working tree, allow it to also update the index with the result of resolution.  --no-rerere-autoupdate is a good way to double-check what rerere did and catch potential mismerges, before committing the result to the index with a separate git add. |
| `--reschedule-failed-exec` | `` | string | Automatically reschedule exec commands that failed. This only makes sense in interactive mode (or when an --exec option was provided). Even though this option applies once a rebase is started, it's set for the whole rebase at the start based on either the rebase.rescheduleFailedExec configuration (see git-config(1) or "CONFIGURATION" below) or whether this option is provided. Otherwise an explicit --no-reschedule-failed-exec at the start would be overridden by the presence of rebase.rescheduleFailedExec=true configuration. |
| `--root` | `` | bool | Rebase all commits reachable from <branch>, instead of limiting them with an <upstream>. This allows you to rebase the root commit(s) on a branch. See also INCOMPATIBLE OPTIONS below. |
| `--signoff` | `` | bool | Add a Signed-off-by trailer to all the rebased commits. Note that if --interactive is given then only commits marked to be picked, edited or reworded will have the trailer added. See also INCOMPATIBLE OPTIONS below. |
| `--stat` | `` | bool | Show a diffstat of what changed upstream since the last rebase. The diffstat is also controlled by the configuration option rebase.stat. |
| `--update-refs` | `` | bool | Automatically force-update any branches that point to commits that are being rebased. Any branches that are checked out in a worktree are not updated in this way. If the configuration variable rebase.updateRefs is set, then this option can be used to override and disable this setting. See also INCOMPATIBLE OPTIONS below. |
| `--verbose` | `-v` | bool | Be verbose. Implies --stat. |
| `--verify` | `` | bool | Allows the pre-rebase hook to run, which is the default. This option can be used to override --no-verify. See also githooks(5). |
| `--whitespace` | `` | string | This flag is passed to the git apply program (see git-apply(1)) that applies the patch. Implies --apply. See also INCOMPATIBLE OPTIONS below. |

### `git reset`

fatal: not a git repository (or any parent up to mount point /mnt)

### `git restore`

Restore working tree files

```
git restore [<options>] [--source=<tree>] [--staged] [--worktree] [--] <pathspec>... git restore [<options>] [--source=<tree>] [--staged] [--worktree] --pathspec-from-file=<file> [--pathspec-file-nul] git restore (-p|--patch) [<options>] [--source=<tree>] [--staged] [--worktree] [--] [<pathspec>...]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--conflict` | `` | string | The same as --merge option above, but changes the way the conflicting hunks are presented, overriding the merge.conflictStyle configuration variable. Possible values are "merge" (default), "diff3", and "zdiff3". |
| `--ignore-skip-worktree-bits` | `` | string | In sparse checkout mode, the default is to only update entries matched by <pathspec> and sparse patterns in $GIT_DIR/info/sparse-checkout. This option ignores the sparse patterns and unconditionally restores any files in <pathspec>. |
| `--ignore-unmerged` | `` | string | When restoring files on the working tree from the index, do not abort the operation if there are unmerged entries and neither --ours, --theirs, --merge or --conflict is specified. Unmerged paths on the working tree are left alone. |
| `--merge` | `-m` | string | When restoring files on the working tree from the index, recreate the conflicted merge in the unmerged paths. This option cannot be used when checking out paths from a tree-ish (i.e. with the --source option). |
| `--ours` | `` | string | When restoring files in the working tree from the index, use stage #2 (ours) or #3 (theirs) for unmerged paths. This option cannot be used when checking out paths from a tree-ish (i.e. with the --source option). Note that during git rebase and git pull --rebase, ours and theirs may appear swapped. See the explanation of the same options in git-checkout(1) for details. |
| `--overlay` | `` | string | In overlay mode, the command never removes files when restoring. In no-overlay mode, tracked files that do not appear in the --source tree are removed, to make them match <tree> exactly. The default is no-overlay mode. |
| `--patch` | `-p` | string | Interactively select hunks in the difference between the restore source and the restore location. See the "Interactive Mode" section of git-add(1) to learn how to operate the --patch mode. Note that --patch can accept no pathspec and will prompt to restore all modified paths. |
| `--pathspec-file-nul` | `` | string | Only meaningful with --pathspec-from-file. Pathspec elements are separated with NUL character and all other characters are taken literally (including newlines and quotes). |
| `--pathspec-from-file` | `` | string | Pathspec is passed in <file> instead of commandline args. If <file> is exactly - then standard input is used. Pathspec elements are separated by LF or CR/LF. Pathspec elements can be quoted as explained for the configuration variable core.quotePath (see git-config(1)). See also --pathspec-file-nul and global --literal-pathspecs. |
| `--progress` | `` | bool | Progress status is reported on the standard error stream by default when it is attached to a terminal, unless --quiet is specified. This flag enables progress reporting even if not attached to a terminal, regardless of --quiet. |
| `--quiet` | `-q` | bool | Quiet, suppress feedback messages. Implies --no-progress. |
| `--recurse-submodules` | `` | string | If <pathspec> names an active submodule and the restore location includes the working tree, the submodule will only be updated if this option is given, in which case its working tree will be restored to the commit recorded in the superproject, and any local modifications overwritten. If nothing (or --no-recurse-submodules) is used, submodules working trees will not be updated. Just like git-checkout(1), this will detach HEAD of the submodule. |

### `git rm`

Remove files from the working tree and from the index

```
git rm [-f | --force] [-n] [-r] [--cached] [--ignore-unmatch] [--quiet] [--pathspec-from-file=<file> [--pathspec-file-nul]] [--] [<pathspec>...]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--cached` | `` | string | Use this option to unstage and remove paths only from the index. Working tree files, whether modified or not, will be left alone. |
| `--dry-run` | `-n` | string | Don't actually remove any file(s). Instead, just show if they exist in the index and would otherwise be removed by the command. |
| `--force` | `-f` | bool | Override the up-to-date check. |
| `--ignore-unmatch` | `` | string | Exit with a zero status even if no files matched. |
| `--pathspec-file-nul` | `` | string | Only meaningful with --pathspec-from-file. Pathspec elements are separated with NUL character and all other characters are taken literally (including newlines and quotes). |
| `--pathspec-from-file` | `` | string | Pathspec is passed in <file> instead of commandline args. If <file> is exactly - then standard input is used. Pathspec elements are separated by LF or CR/LF. Pathspec elements can be quoted as explained for the configuration variable core.quotePath (see git-config(1)). See also --pathspec-file-nul and global --literal-pathspecs. |
| `--quiet` | `-q` | string | git rm normally outputs one line (in the form of an rm command) for each file removed. This option suppresses that output. |
| `--sparse` | `` | string | Allow updating index entries outside of the sparse-checkout cone. Normally, git rm refuses to update index entries whose paths do not fit within the sparse-checkout cone. See git-sparse-checkout(1) for more. |
| `-r` | `-r` | bool | Allow recursive removal when a leading directory name is given. |

### `git show`

Show various types of objects

```
git show [<options>] [<object>...]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--abbrev-commit` | `` | string | Instead of showing the full 40-byte hexadecimal commit object name, show a prefix that names the object uniquely. "--abbrev=<n>" (which also modifies diff output, if it is displayed) option can be used to specify the minimum length of the prefix. This should make "--pretty=oneline" a whole lot more readable for people using 80-column terminals. |
| `--encoding` | `` | string | Commit objects record the character encoding used for the log message in their encoding header; this option can be used to tell the command to re-code the commit log message in the encoding preferred by the user. For non plumbing commands this defaults to UTF-8. Note that if an object claims to be encoded in X and we are outputting in X, we will output the object verbatim; this means that invalid sequences in the original commit may be copied to the output. Likewise, if iconv(3) fails to convert the commit, we will quietly output the original object verbatim. |
| `--no-abbrev-commit` | `` | string | Show the full 40-byte hexadecimal commit object name. This negates --abbrev-commit, either explicit or implied by other options such as "--oneline". It also overrides the log.abbrevCommit variable. |
| `--no-notes` | `` | bool | Do not show notes. This negates the above --notes option, by resetting the list of notes refs from which notes are shown. Options are parsed in the order given on the command line, so e.g. "--notes --notes=foo --no-notes --notes=bar" will only show notes from "refs/notes/bar". |
| `--oneline` | `` | bool | This is a shorthand for "--pretty=oneline --abbrev-commit" used together. |
| `--show-notes-by-default` | `` | bool | Show the default notes unless options for displaying specific notes are given. |
| `--show-signature` | `` | bool | Check the validity of a signed commit object by passing the signature to gpg --verify and show the output. |

### `git status`

Show the working tree status

```
git status [<options>] [--] [<pathspec>...]
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--ahead-behind` | `` | bool | Display or do not display detailed ahead/behind counts for the branch relative to its upstream branch. Defaults to true. |
| `--branch` | `-b` | string | Show the branch and tracking info even in short-format. |
| `--long` | `` | string | Give the output in the long-format. This is the default. |
| `--renames` | `` | string | Turn on/off rename detection regardless of user configuration. See also git-diff(1) --no-renames. |
| `--short` | `-s` | string | Give the output in the short-format. |
| `--show-stash` | `` | string | Show the number of entries currently stashed away. |
| `--verbose` | `-v` | string | In addition to the names of files that have been changed, also show the textual changes that are staged to be committed (i.e., like the output of git diff --cached). If -v is specified twice, then also show the changes in the working tree that have not yet been staged (i.e., like the output of git diff). |
| `-z` | `-z` | bool | Terminate entries with NUL, instead of LF. This implies the --porcelain=v1 output format if no other format is given. |

### `git switch`

Switch branches

```
git switch [<options>] [--no-guess] <branch> git switch [<options>] --detach [<start-point>] git switch [<options>] (-c|-C) <new-branch> [<start-point>] git switch [<options>] --orphan <new-branch>
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--conflict` | `` | string | The same as --merge option above, but changes the way the conflicting hunks are presented, overriding the merge.conflictStyle configuration variable. Possible values are "merge" (default), "diff3", and "zdiff3". |
| `--detach` | `-d` | bool | Switch to a commit for inspection and discardable experiments. See the "DETACHED HEAD" section in git- checkout(1) for details. |
| `--discard-changes` | `` | bool | Proceed even if the index or the working tree differs from HEAD. Both the index and working tree are restored to match the switching target. If --recurse-submodules is specified, submodule content is also restored to match the switching target. This is used to throw away local changes. |
| `--force` | `-f` | bool | An alias for --discard-changes. |
| `--guess` | `` | string | If <branch> is not found but there does exist a tracking branch in exactly one remote (call it <remote>) with a matching name, treat as equivalent to $ git switch -c <branch> --track <remote>/<branch> If the branch exists in multiple remotes and one of them is named by the checkout.defaultRemote configuration variable, we'll use that one for the purposes of disambiguation, even if the <branch> isn't unique across all remotes. Set it to e.g.  checkout.defaultRemote=origin to always checkout remote branches from there if <branch> is ambiguous but exists on the origin remote. See also checkout.defaultRemote in git-config(1). --guess is the default behavior. Use --no-guess to disable it. The default behavior can be set via the checkout.guess configuration variable. |
| `--ignore-other-worktrees` | `` | bool | git switch refuses when the wanted ref is already checked out by another worktree. This option makes it check the ref out anyway. In other words, the ref can be held by more than one worktree. |
| `--merge` | `-m` | string | If you have local modifications to one or more files that are different between the current branch and the branch to which you are switching, the command refuses to switch branches in order to preserve your modifications in context. However, with this option, a three-way merge between the current branch, your working tree contents, and the new branch is done, and you will be on the new branch. When a merge conflict happens, the index entries for conflicting paths are left unmerged, and you need to resolve the conflicts and mark the resolved paths with git add (or git rm if the merge should result in deletion of the path). |
| `--no-track` | `` | bool | Do not set up "upstream" configuration, even if the branch.autoSetupMerge configuration variable is true. |
| `--orphan` | `` | string | Create a new orphan branch, named <new-branch>. All tracked files are removed. |
| `--progress` | `` | bool | Progress status is reported on the standard error stream by default when it is attached to a terminal, unless --quiet is specified. This flag enables progress reporting even if not attached to a terminal, regardless of --quiet. |
| `--quiet` | `-q` | bool | Quiet, suppress feedback messages. |
| `--recurse-submodules` | `` | bool | Using --recurse-submodules will update the content of all active submodules according to the commit recorded in the superproject. If nothing (or --no-recurse-submodules) is used, submodules working trees will not be updated. Just like git-submodule(1), this will detach HEAD of the submodules. |

### `git tag`

Create, list, delete or verify a tag object signed with GPG

```
git tag [-a | -s | -u <key-id>] [-f] [-m <msg> | -F <file>] [-e] <tagname> [<commit> | <object>] git tag -d <tagname>... git tag [-n[<num>]] -l [--contains <commit>] [--no-contains <commit>] [--points-at <object>] [--column[=<options>] | --no-column] [--create-reflog] [--sort=<key>] [--format=<format>] [--merged <commit>] [--no-merged <commit>] [<pattern>...] git tag -v [--format=<format>] <tagname>...
```

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--annotate` | `-a` | bool | Make an unsigned, annotated tag object |
| `--cleanup` | `` | string | This option sets how the tag message is cleaned up. The <mode> can be one of verbatim, whitespace and strip. The strip mode is default. The verbatim mode does not change message at all, whitespace removes just leading/trailing whitespace lines and strip removes both whitespace and commentary. |
| `--create-reflog` | `` | bool | Create a reflog for the tag. To globally enable reflogs for tags, see core.logAllRefUpdates in git- config(1). The negated form --no-create-reflog only overrides an earlier --create-reflog, but currently does not negate the setting of core.logAllRefUpdates. |
| `--delete` | `-d` | string | Delete existing tags with the given names. |
| `--edit` | `-e` | string | The message taken from file with -F and command line with -m are usually used as the tag message unmodified. This option lets you further edit the message taken from these sources. |
| `--force` | `-f` | string | Replace an existing tag with the given name (instead of failing) |
| `--format` | `` | string | A string that interpolates %(fieldname) from a tag ref being shown and the object it points at. The format is the same as that of git-for-each-ref(1). When unspecified, defaults to %(refname:strip=2). |
| `--ignore-case` | `-i` | bool | Sorting and filtering tags are case insensitive. |
| `--list` | `-l` | bool | List tags. With optional <pattern>..., e.g.  git tag --list 'v-*', list only the tags that match the pattern(s). Running "git tag" without arguments also lists all tags. The pattern is a shell wildcard (i.e., matched using fnmatch(3)). Multiple patterns may be given; if any of them matches, the tag is shown. This option is implicitly supplied if any other list-like option such as --contains is provided. See the documentation for each of those options for details. |
| `--no-sign` | `` | string | Override tag.gpgSign configuration variable that is set to force each and every tag to be signed. |
| `--omit-empty` | `` | string | Do not print a newline after formatted refs where the format expands to the empty string. |
| `--points-at` | `` | string | Only list tags of the given object (HEAD if not specified). Implies --list. |
| `--sign` | `-s` | bool | Make a GPG-signed tag, using the default e-mail address's key. The default behavior of tag GPG-signing is controlled by tag.gpgSign configuration variable if it exists, or disabled otherwise. See git-config(1). |
| `--sort` | `` | string | Sort based on the key given. Prefix - to sort in descending order of the value. You may use the --sort=<key> option multiple times, in which case the last key becomes the primary key. Also supports "version:refname" or "v:refname" (tag names are treated as versions). The "version:refname" sort order can also be affected by the "versionsort.suffix" configuration variable. The keys supported are the same as those in git for-each-ref. Sort order defaults to the value configured for the tag.sort variable if it exists, or lexicographic order otherwise. See git-config(1). |
| `--verify` | `-v` | string | Verify the GPG signature of the given tag names. |

