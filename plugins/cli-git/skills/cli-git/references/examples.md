# git -- Usage Examples

## `git add`

```bash
git add Documentation/\*.txt
```
Note that the asterisk * is quoted from the shell in this example; this lets the command include the files

```bash
from subdirectories of Documentation/ directory.
```
git add git-*.sh

```bash
Because this example lets the shell expand the asterisk (i.e. you are listing the files explicitly), it
```
does not consider subdir/git-foo.sh.

## `git bisect`

```bash
git bisect start HEAD v1.2 --      # HEAD is bad, v1.2 is good
```
git bisect run make                # "make" builds the app

```bash
git bisect reset                   # quit the bisect session
```
git bisect start HEAD origin --    # HEAD is bad, origin is good

```bash
git bisect run make test           # "make test" builds and tests
```
git bisect reset                   # quit the bisect session

```bash
cat ~/test.sh
```
make || exit 125                     # this skips broken builds

```bash
git bisect start HEAD HEAD~10 --   # culprit is among the last 10
```
git bisect run ~/test.sh

```bash
check_test_case.sh should exit 0 if the test case passes, and exit 1 otherwise.
```
It is safer if both test.sh and check_test_case.sh are outside the repository to prevent interactions

```bash
between the bisect, make and test processes and the scripts.
```
cat ~/test.sh

```bash
if      git merge --no-commit --no-ff hot-fix &&
```
make

```bash
then
```
status=$?

```bash
else
```
status=125

```bash
fi
```
git reset --hard

```bash
exit $status
```
This applies modifications from a hot-fix branch before each test run, e.g. in case your build or test

```bash
environment changed so that older revisions may need a fix which newer ones have already. (Make sure the
```
hot-fix branch is based off a commit which is contained in all revisions which you are bisecting, so that

```bash
the merge does not pull in too much, or use git cherry-pick instead of git merge.)
```
git bisect start HEAD HEAD~10 --   # culprit is among the last 10

```bash
git bisect run sh -c "make || exit 125; ~/check_test_case.sh"
```
git bisect reset                   # quit the bisect session

```bash
This shows that you can do without a run script if you write the test on a single line.
```
git bisect start HEAD <known-good-commit> [ <boundary-commit> ... ] --no-checkout

```bash
git bisect run sh -c '
```
GOOD=$(git for-each-ref "--format=%(objectname)" refs/bisect/good-*) &&

```bash
git rev-list --objects BISECT_HEAD --not $GOOD >tmp.$$ &&
```
git pack-objects --stdout >/dev/null <tmp.$$

```bash
rc=$?
```
rm -f tmp.$$

```bash
test $rc = 0'
```
git bisect reset                   # quit the bisect session

```bash
In this case, when git bisect run finishes, bisect/bad will refer to a commit that has at least one parent
```
whose reachable graph is fully traversable in the sense required by git pack objects.

```bash
git bisect start
```
git bisect new HEAD    # current commit is marked as new

```bash
git bisect old HEAD~10 # the tenth commit from now is marked as old
```
or:

```bash
git bisect start --term-old broken --term-new fixed
```
git bisect fixed

## `git branch`

```bash
git clone git://git.kernel.org/pub/scm/.../linux-2.6 my2.6
```
cd my2.6

```bash
git branch my2.6.14 v2.6.14   (1)
```
git switch my2.6.14

```bash
1. This step and the next one could be combined into a single step with "checkout -b
```
my2.6.14 v2.6.14".

```bash
git clone git://git.kernel.org/.../git.git my.git
```
cd my.git

```bash
git branch -d -r origin/todo origin/html origin/man   (1)
```
git branch -D test                                    (2)

```bash
1. Delete the remote-tracking branches "todo", "html" and "man". The next fetch or pull
```
will create them again unless you configure them not to. See git-fetch(1).

```bash
2. Delete the "test" branch even if the "master" branch (or whichever branch is currently
```
checked out) does not have all commits from the test branch.

```bash
git branch -r -l '<remote>/<pattern>'                 (1)
```
git for-each-ref 'refs/remotes/<remote>/<pattern>'    (2)

```bash
1. Using -a would conflate <remote> with any local branches you happen to have been
```
prefixed with the same <remote> pattern.

## `git clone`

```bash
git clone git://git.kernel.org/pub/scm/.../linux.git my-linux
```
cd my-linux

```bash
make
```
git clone -l -s -n . ../copy

```bash
cd ../copy
```
git show-branch

```bash
git clone --reference /git/linux.git \
```
git://git.kernel.org/pub/scm/.../linux.git \

```bash
my-linux
```
cd my-linux

## `git commit`

```bash
edit hello.c
```
git rm goodbye.c

```bash
git add hello.c
```
git commit

```bash
git commit -a
```
edit hello.c hello.h

```bash
git add hello.c hello.h
```
edit Makefile

```bash
git commit Makefile
```
git commit

```bash
git status | grep unmerged
```
unmerged: hello.c

## `git diff`

```bash
git diff            (1)
```
git diff --cached   (2)

```bash
git diff HEAD       (3)
```
git diff AUTO_MERGE (4)

```bash
1. Changes in the working tree not yet staged for the next commit.
```
2. Changes between the index and your last commit; what you would be committing if you run

```bash
git commit without -a option.
```
3. Changes in the working tree since your last commit; what you would be committing if you

```bash
run git commit -a
```
4. Changes in the working tree you've made to resolve textual conflicts so far.

```bash
git diff test            (1)
```
git diff HEAD -- ./test  (2)

```bash
git diff HEAD^ HEAD      (3)
```
1. Instead of using the tip of the current branch, compare with the tip of "test" branch.

```bash
2. Instead of comparing with the tip of "test" branch, compare with the tip of the current
```
branch, but limit the comparison to the file "test".

```bash
3. Compare the version before the last commit and the last commit.
```
git diff topic master    (1)

```bash
git diff topic..master   (2)
```
git diff topic...master  (3)

```bash
1. Changes between the tips of the topic and the master branches.
```
2. Same as above.

```bash
3. Changes that occurred on the master branch since when the topic branch was started off
```
it.

```bash
git diff --diff-filter=MRC            (1)
```
git diff --name-status                (2)

```bash
git diff arch/i386 include/asm-i386   (3)
```
1. Show only modification, rename, and copy, but not addition or deletion.

```bash
2. Show only names and the nature of change, but not actual diff output.
```
3. Limit diff output to named subtrees.

```bash
git diff --find-copies-harder -B -C  (1)
```
git diff -R                          (2)

```bash
1. Spend extra cycles to find renames, copies and complete rewrites (very expensive).
```
2. Output diff in reverse.

## `git fetch`

```bash
git fetch origin
```
The above command copies all branches from the remote refs/heads/ namespace and stores them to the local

```bash
refs/remotes/origin/ namespace, unless the remote.<repository>.fetch option is used to specify a
```
non-default refspec.

```bash
git fetch origin +seen:seen maint:tmp
```
This updates (or creates, as necessary) branches seen and tmp in the local repository by fetching from the

```bash
branches (respectively) seen and maint from the remote repository.
```
The seen branch will be updated even if it does not fast-forward, because it is prefixed with a plus sign;

```bash
tmp will not be.
```
git fetch git://git.kernel.org/pub/scm/git/git.git maint

```bash
git log FETCH_HEAD
```
The first command fetches the maint branch from the repository at git://git.kernel.org/pub/scm/git/git.git

```bash
and the second command uses FETCH_HEAD to examine the branch with git-log(1). The fetched objects will
```
eventually be removed by git's built-in housekeeping (see git-gc(1)).

## `git grep`

```bash
Looks for time_t in all tracked .c and .h files in the working directory and its subdirectories.
```
Looks for a line that has #define and either MAX_PATH or PATH_MAX.

```bash
Looks for a line that has NODE or Unexpected in files that have lines that match both.
```
Looks for solution, excluding files in Documentation.

## `git init`

```bash
cd /path/to/my/codebase
```
git init      (1)

```bash
git add .     (2)
```
git commit    (3)

```bash
1. Create a /path/to/my/codebase/.git directory.
```
2. Add all existing files to the index.

## `git log`

```bash
Show the whole commit history, but skip any merges
```
Show all commits since version v2.6.12 that changed any file in the include/scsi or drivers/scsi

```bash
subdirectories
```
Show the changes during the last two weeks to the file gitk. The -- is necessary to avoid confusion with

```bash
the branch named gitk
```
Show the commits that are in the "test" branch but not yet in the "release" branch, along with the list of

```bash
paths each commit modifies.
```
Shows the commits that changed builtin/rev-list.c, including those commits that occurred before the file

```bash
was given its present name.
```
Shows all commits that are in any of local branches but not in any of remote-tracking branches for origin

```bash
Shows all commits that are in local master but not in any remote repository master branches.
```
Shows the history including change diffs, but only from the "main branch" perspective, skipping commits

```bash
that come from merged branches, and showing full diffs of changes introduced by the merges. This makes
```
sense only when following a strict policy of merging all topic branches when staying on a single

```bash
integration branch.
```
Shows how the function main() in the file main.c evolved over time.

## `git pull`

```bash
current branch:
```
git pull

```bash
git pull origin
```
Normally the branch merged in is the HEAD of the remote repository, but the choice is determined by the

```bash
branch.<name>.remote and branch.<name>.merge options; see git-config(1) for details.
```
git pull origin next

```bash
This leaves a copy of next temporarily in FETCH_HEAD, and updates the remote-tracking branch origin/next.
```
The same can be done by invoking fetch and merge:

## `git push`

```bash
Works like git push <remote>, where <remote> is the current branch's remote (or origin, if no remote is
```
configured for the current branch).

```bash
Without additional configuration, pushes the current branch to the configured upstream
```
without pushing otherwise.

```bash
The default behavior of this command when no <refspec> is given can be configured by setting the push
```
option of the remote, or the push.default configuration variable.

```bash
For example, to default to pushing only the current branch to origin use git config remote.origin.push
```
HEAD. Any valid <refspec> (like the ones in the examples below) can be configured as the default for git

```bash
push origin.
```
Push "matching" branches to origin. See <refspec> in the OPTIONS section above for a description of

```bash
Find a ref that matches master in the source repository (most likely, it would find refs/heads/master),
```
and update the same ref (e.g.  refs/heads/master) in origin repository with it. If master did not exist

```bash
remotely, it would be created.
```
A handy way to push the current branch to the same name on the remote.

```bash
Use the source ref that matches master (e.g.  refs/heads/master) to update the ref that matches
```
satellite/master (most probably refs/remotes/satellite/master) in the mothership repository; do the same

```bash
for dev and satellite/dev.
```
See the section describing <refspec>...  above for a discussion of the matching semantics.

```bash
This is to emulate git fetch run on the mothership using git push that is run in the opposite direction in
```
order to integrate the work done on satellite, and is often necessary when you can only make connection in

```bash
one way (i.e. satellite can ssh into mothership but mothership cannot initiate connection to satellite
```
because the latter is behind a firewall or does not run sshd).

```bash
After running this git push on the satellite machine, you would ssh into the mothership and run git merge
```
there to complete the emulation of git pull that were run on mothership to pull changes made on satellite.

```bash
Push the current branch to the remote ref matching master in the origin repository. This form is
```
convenient to push the current branch without thinking about its local name.

```bash
Create the branch experimental in the origin repository by copying the current master branch. This form is
```
only needed to create a new branch or tag in the remote repository when the local name and the remote name

```bash
are different; otherwise, the ref name on its own will work.
```
Find a ref that matches experimental in the origin repository (e.g.  refs/heads/experimental), and delete

```bash
it.
```
Update the origin repository's master branch with the dev branch, allowing non-fast-forward updates.  This

```bash
can leave unreferenced commits dangling in the origin repository.  Consider the following situation, where
```
a fast-forward is not possible:

```bash
o---o---o---A---B  origin/master
```
X---Y---Z  dev

```bash
The above command would change the origin repository to
```
A---B  (unnamed branch)

```bash
/
```
o---o---o---X---Y---Z  master

```bash
Commits A and B would no longer belong to a branch with a symbolic name, and so would be unreachable. As
```
such, these commits would be removed by a git gc command on the origin repository.

## `git restore`

```bash
git switch master
```
git restore --source master~2 Makefile  (1)

```bash
rm -f hello.c
```
git restore hello.c                     (2)

```bash
1. take a file out of another commit
```
2. restore hello.c from the index

```bash
git restore '*.c'
```
git restore .

```bash
git restore :/
```
git restore --staged hello.c

```bash
git restore --source=HEAD --staged --worktree hello.c
```
git restore -s@ -SW hello.c

## `git rm`

```bash
Removes all *.txt files from the index that are under the Documentation directory and any of its
```
subdirectories.

```bash
Note that the asterisk * is quoted from the shell in this example; this lets Git, and not the shell,
```
expand the pathnames of files and subdirectories under the Documentation/ directory.

## `git show`

```bash
Shows the tag v1.0.0, along with the object the tag points at.
```
Shows the tree pointed to by the tag v1.0.0.

```bash
Shows the subject of the commit pointed to by the tag v1.0.0.
```
Shows the contents of the file Documentation/README as they were current in the 10th last commit of the

```bash
branch next.
```
Concatenates the contents of said Makefiles in the head of the branch master.

## `git switch`

```bash
git switch mytopic
```
error: You have local changes to 'frotz'; not switching branches.

```bash
git switch -m mytopic
```
Auto-merging frotz

```bash
git switch -
```
git switch -c fixup HEAD~3

```bash
Switched to a new branch 'fixup'
```
git switch new-topic

```bash
Branch 'new-topic' set up to track remote branch 'new-topic' from 'origin'
```
Switched to a new branch 'new-topic'

```bash
git switch --detach HEAD~3
```
HEAD is now at 9fc9555312 Merge branch 'cc/shared-index-permbits'

