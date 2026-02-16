# git -- Usage Examples

## `git add`

```bash
o   Adds content from all *.txt files under Documentation directory and its subdirectories:
```
o   Considers adding content from all git-*.sh scripts:

## `git clone`

```bash
o   Clone from upstream:
```
o   Make a local clone that borrows from the current directory, without checking things out:

```bash
o   Clone from upstream while borrowing from an existing local directory:
```
o   Create a bare repository to publish your changes to the public:

## `git commit`

```bash
staging area called the "index" with git add. A file can be reverted back, only in the index but not in the
```
working tree, to that of the last commit with git restore --staged <file>, which effectively reverts git add

```bash
and prevents the changes to this file from participating in the next commit. After building the state to be
```
committed incrementally with these commands, git commit (without any pathname parameter) is used to record

```bash
what has been staged so far. This is the most basic form of the command. An example:
```
files whose contents are tracked in your working tree and do corresponding git add and git rm for you. That

```bash
to git commit. When pathnames are given, the command makes a commit that only records the changes made to the
```
named paths:

```bash
not included in the resulting commit. However, their changes are not lost -- they are still staged and merely
```
held back. After the above sequence, if you do:

```bash
already staged to be committed for you, and paths that conflicted are left in unmerged state. You would have
```
to first check which paths are conflicting with git status and after fixing them manually in your working

```bash
during a merge resolution, you cannot use git commit with pathnames to alter the order the changes are
```
given pathnames (but see -i option).

## `git fetch`

```bash
o   Update the remote-tracking branches:
```
o   Using refspecs explicitly:

## `git grep`

```bash
git grep 'time_t' -- '*.[ch]'
```
git grep -e '#define' --and \( -e MAX_PATH -e PATH_MAX \)

```bash
git grep --all-match -e NODE -e Unexpected
```
git grep solution -- :^Documentation

## `git log`

```bash
git log --no-merges
```
git log v2.6.12.. include/scsi drivers/scsi

```bash
git log --since="2 weeks ago" -- gitk
```
git log --name-status release..test

```bash
git log --follow builtin/rev-list.c
```
git log --branches --not --remotes=origin

```bash
git log master --not --remotes=*/master
```
git log -p -m --first-parent

```bash
git log -L '/int main/',/^}/:main.c
```
git log -3

## `git pull`

```bash
o   Update the remote-tracking branches for the repository you cloned from, then merge one of them into your
```
o   Merge into the current branch the remote branch next:

## `git push`

```bash
git push
```
git push origin

```bash
git push origin :
```
git push origin master

```bash
git push origin HEAD
```
git push mothership master:satellite/master dev:satellite/dev

```bash
git push origin HEAD:master
```
git push origin master:refs/heads/experimental

```bash
git push origin :experimental
```
git push origin +dev:master

## `git restore`

```bash
hello.c by mistake, and gets it back from the index.
```
take a file out of another commit

```bash
restore hello.c from the index
```
or to restore all working tree files with top pathspec magic (see gitglossary(7))

```bash
or you can restore both the index and the working tree (this is the same as using git-checkout(1))
```
or the short form which is more practical but less readable:

## `git rm`

```bash
git rm Documentation/\*.txt
```
git rm -f git-*.sh

## `git show`

```bash
git show v1.0.0
```
git show v1.0.0^{tree}

```bash
git show -s --format=%s v1.0.0^{commit}
```
git show next~10:Documentation/README

## `git switch`

```bash
in which case the above switch would fail like this:
```
show you what changes you made since the tip of the new branch.

