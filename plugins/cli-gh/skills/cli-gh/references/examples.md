# gh -- Usage Examples

## `gh agent-task`

```bash
gh agent-task list
```
gh agent-task create "Improve the performance of the data processing pipeline"

```bash
gh agent-task view 123
```
gh agent-task view 12345abc-12345-12345-12345-12345abc

### `gh agent-task create`

```bash
gh agent-task create "build me a new app"
```
gh agent-task create "build me a new app" --follow

```bash
gh agent-task create -F task-desc.md
```
echo "build me a new app" | gh agent-task create -F -

```bash
gh agent-task create
```
gh agent-task create -F task-desc.md

```bash
gh agent-task create "fix errors" --base branch
```
gh agent-task create "build me a new app" --custom-agent my-agent

### `gh agent-task view`

```bash
gh agent-task view e2fa49d2-f164-4a56-ab99-498090b8fcdf
```
gh agent-task view 12345

```bash
gh agent-task view --repo OWNER/REPO 12345
```
gh agent-task view OWNER/REPO#12345

### `gh alias import`

```bash
gh alias import aliases.yml
```
gh alias import -

### `gh alias set`

```bash
gh alias set pv 'pr view'
```
gh pv -w 123  #=> gh pr view -w 123

```bash
gh alias set bugs 'issue list --label=bugs'
```
gh bugs

```bash
gh alias set homework 'issue list --assignee @me'
```
gh homework

```bash
gh alias set 'issue mine' 'issue list --mention @me'
```
gh issue mine

```bash
gh alias set epicsBy 'issue list --author="$1" --label="epic"'
```
gh epicsBy vilmibm  #=> gh issue list --author="vilmibm" --label="epic"

```bash
gh alias set --shell igrep 'gh issue list --label="$1" | grep "$2"'
```
gh igrep epic foo  #=> gh issue list --label="epic" | grep "foo"

### `gh attestation download`

```bash
gh attestation download example.bin -o github
```
gh attestation download example.bin -R github/example

### `gh attestation verify`

```bash
gh attestation verify example.bin --repo github/example
```
gh attestation verify example.bin --owner github

```bash
gh attestation verify example.bin --owner github --format json
```
gh attestation verify oci://<image-uri> --owner github --bundle sha256:foo.jsonl

### `gh auth login`

```bash
gh auth login
```
gh auth login --web --clipboard

```bash
gh auth login --with-token < mytoken.txt
```
gh auth login --hostname enterprise.internal

### `gh auth logout`

```bash
gh auth logout
```
gh auth logout --hostname enterprise.internal --user monalisa

### `gh auth refresh`

```bash
gh auth refresh --scopes write:org,read:public_key
```
gh auth refresh

```bash
gh auth refresh --remove-scopes delete_repo
```
gh auth refresh --reset-scopes

### `gh auth setup-git`

```bash
gh auth setup-git
```
gh auth setup-git --hostname enterprise.internal

### `gh auth status`

```bash
gh auth status
```
gh auth status --active --hostname github.example.com

```bash
gh auth status --show-token
```
gh auth status --json hosts

```bash
gh auth status --json hosts --show-token
```
gh auth status --json hosts --jq '.hosts | add'

### `gh auth switch`

```bash
gh auth switch
```
gh auth switch --hostname enterprise.internal --user monalisa

## `gh browse`

```bash
gh browse
```
gh browse script/

```bash
gh browse 217
```
gh browse 77507cd94ccafcf568f8560cfecde965fcfa63

```bash
gh browse --settings
```
gh browse main.go:312

```bash
gh browse main.go --branch bug-fix
```
gh browse main.go --commit=77507cd94ccafcf568f8560cfecde965fcfa63

## `gh cache`

```bash
gh cache list
```
gh cache delete --all

### `gh cache delete`

```bash
gh cache delete 1234
```
gh cache delete cache-key

```bash
gh cache delete 1234 --repo cli/cli
```
gh cache delete cache-key --ref refs/heads/feature-branch

```bash
gh cache delete cache-key --ref refs/pull/<PR-number>/merge
```
gh cache delete --all

```bash
gh cache delete --all --ref refs/pull/<PR-number>/merge
```
gh cache delete --all --succeed-on-no-caches

### `gh cache list`

```bash
gh cache list --sort last_accessed_at --order asc
```
gh cache list --key key-prefix

```bash
gh cache list --ref refs/heads/<branch-name>
```
gh cache list --ref refs/pull/<pr-number>/merge

### `gh codespace cp`

```bash
gh codespace cp -e README.md 'remote:/workspaces/$RepositoryName/'
```
gh codespace cp -e 'remote:~/*.go' ./gofiles/

```bash
gh codespace cp -e 'remote:/workspaces/myproj/go.{mod,sum}' ./gofiles/
```
gh codespace cp -e -- -F ~/.ssh/codespaces_config 'remote:~/*.go' ./gofiles/

### `gh codespace ssh`

```bash
gh codespace ssh
```
gh codespace ssh --config > ~/.ssh/codespaces

### `gh codespace view`

```bash
gh cs view
```
gh cs view -c codespace-name-12345

```bash
gh cs view --json
```
gh cs view --json displayName,machineDisplayName,state

### `gh config set`

```bash
gh config set editor vim
```
gh config set editor "code --wait"

```bash
gh config set git_protocol ssh --host github.com
```
gh config set prompt disabled

## `gh copilot`

```bash
gh copilot
```
gh copilot -p "Summarize this week's commits" --allow-tool 'shell(git)'

```bash
gh copilot --remove
```
gh copilot -- --help

### `gh extension create`

```bash
gh extension create
```
gh extension create foobar

```bash
gh extension create --precompiled=go foobar
```
gh extension create --precompiled=other foobar

### `gh extension install`

```bash
gh extension install owner/gh-extension
```
gh extension install https://my.ghes.com/owner/gh-extension

### `gh extension search`

```bash
gh ext search
```
gh ext search --limit 300

```bash
gh ext search branch
```
gh ext search --owner github

```bash
gh ext search --sort updated --order asc
```
gh ext search --license MIT

### `gh gist create`

```bash
gh gist create --public hello.py
```
gh gist create hello.py -d "my Hello-World program in Python"

```bash
gh gist create hello.py world.py cool.txt
```
gh gist create *.md *.txt artifact.*

```bash
gh gist create -
```
cat cool.txt | gh gist create

### `gh gist delete`

```bash
gh gist delete
```
gh gist delete 1234

### `gh gist list`

```bash
gh gist list --secret
```
gh gist list --filter octo --include-content

## `gh issue`

```bash
gh issue list
```
gh issue create --label bug

### `gh issue create`

```bash
gh issue create --title "I found a bug" --body "Nothing works"
```
gh issue create --label "bug,help wanted"

```bash
gh issue create --label bug --label "help wanted"
```
gh issue create --assignee monalisa,hubot

```bash
gh issue create --assignee "@me"
```
gh issue create --assignee "@copilot"

```bash
gh issue create --project "Roadmap"
```
gh issue create --template "Bug Report"

### `gh issue develop`

```bash
gh issue develop --list 123
```
gh issue develop --list --repo cli/cli 123

```bash
gh issue develop 123 --base my-feature
```
gh issue develop 123 --checkout

### `gh issue edit`

```bash
gh issue edit 23 --title "I found a bug" --body "Nothing works"
```
gh issue edit 23 --add-label "bug,help wanted" --remove-label "core"

```bash
gh issue edit 23 --add-assignee "@me" --remove-assignee monalisa,hubot
```
gh issue edit 23 --add-assignee "@copilot"

```bash
gh issue edit 23 --add-project "Roadmap" --remove-project v1,v2
```
gh issue edit 23 --milestone "Version 1"

```bash
gh issue edit 23 --remove-milestone
```
gh issue edit 23 --body-file body.txt

### `gh issue list`

```bash
gh issue list --label "bug" --label "help wanted"
```
gh issue list --author monalisa

```bash
gh issue list --assignee "@me"
```
gh issue list --milestone "The big 1.0"

```bash
gh issue list --search "error no:assignee sort:created-asc"
```
gh issue list --state all

### `gh issue pin`

```bash
gh issue pin 23
```
gh issue pin https://github.com/owner/repo/issues/23

### `gh issue unpin`

```bash
gh issue unpin 23
```
gh issue unpin https://github.com/owner/repo/issues/23

### `gh label clone`

```bash
gh label clone cli/cli --force
```
gh label clone cli/cli --repo octocat/cli

### `gh label edit`

```bash
gh label edit bug --color FF0000
```
gh label edit bug --name big-bug --description "Bigger than normal bug"

### `gh label list`

```bash
gh label list --sort name
```
gh label list --search bug

### `gh org list`

```bash
gh org list
```
gh org list --limit 100

## `gh pr`

```bash
gh pr checkout 353
```
gh pr create --fill

### `gh pr checkout`

```bash
gh pr checkout
```
gh pr checkout 32

```bash
gh pr checkout https://github.com/OWNER/REPO/pull/32
```
gh pr checkout feature

### `gh pr create`

```bash
gh pr create --title "The bug is fixed" --body "Everything works again"
```
gh pr create --reviewer monalisa,hubot  --reviewer myorg/team-name

```bash
gh pr create --project "Roadmap"
```
gh pr create --base develop --head monalisa:feature

### `gh pr edit`

```bash
gh pr edit 23 --title "I found a bug" --body "Nothing works"
```
gh pr edit 23 --add-label "bug,help wanted" --remove-label "core"

```bash
gh pr edit 23 --add-reviewer monalisa,hubot  --remove-reviewer myorg/team-name
```
gh pr edit 23 --add-assignee "@me" --remove-assignee monalisa,hubot

```bash
gh pr edit 23 --add-assignee "@copilot"
```
gh pr edit 23 --add-project "Roadmap" --remove-project v1,v2

```bash
gh pr edit 23 --milestone "Version 1"
```
gh pr edit 23 --remove-milestone

### `gh pr list`

```bash
gh pr list --author "@me"
```
gh pr list --head "typo"

```bash
gh pr list --label bug --label "priority 1"
```
gh pr list --search "status:success review:required"

### `gh pr review`

```bash
gh pr review --approve
```
gh pr review --comment -b "interesting"

```bash
gh pr review 123
```
gh pr review 123 -r -b "needs more ASCII art"

### `gh pr update-branch`

```bash
gh pr update-branch 23
```
gh pr update-branch 23 --rebase

## `gh project`

```bash
gh project create --owner monalisa --title "Roadmap"
```
gh project view 1 --owner cli --web

```bash
gh project field-list 1 --owner cli
```
gh project item-list 1 --owner cli

### `gh project close`

```bash
gh project close 1 --owner monalisa
```
gh project close 1 --owner github --undo

### `gh project field-create`

```bash
gh project field-create 1 --owner "@me" --name "new field" --data-type "text"
```
gh project field-create 1 --owner monalisa --name "new field" --data-type "SINGLE_SELECT" --single-select-options "one,two,three"

### `gh project item-edit`

```bash
gh project item-edit --id <item-id> --field-id <field-id> --project-id <project-id> --text "new text"
```
gh project item-edit --id <item-id> --field-id <field-id> --project-id <project-id> --clear

### `gh project link`

```bash
gh project link 1 --owner monalisa --repo my_repo
```
gh project link 1 --owner my_organization --team my_team

### `gh project list`

```bash
gh project list
```
gh project list --owner github --closed

### `gh project mark-template`

```bash
gh project mark-template 1 --owner "github"
```
gh project mark-template 1 --owner "github" --undo

### `gh project unlink`

```bash
gh project unlink 1 --owner monalisa --repo my_repo
```
gh project unlink 1 --owner my_organization --team my_team

### `gh project view`

```bash
gh project view 1
```
gh project view 1 --owner monalisa --web

### `gh release download`

```bash
gh release download v1.2.3
```
gh release download --pattern '*.deb'

```bash
gh release download -p '*.deb' -p '*.rpm'
```
gh release download v1.2.3 --archive=zip

### `gh release edit`

```bash
gh release edit v1.0 --draft=false
```
gh release edit v1.0 --notes-file /path/to/release_notes.md

### `gh release verify`

```bash
gh release verify
```
gh release verify v1.2.3

### `gh release verify-asset`

```bash
gh release verify-asset ./dist/my-asset.zip
```
gh release verify-asset v1.2.3 ./dist/my-asset.zip

## `gh repo`

```bash
gh repo create
```
gh repo clone cli/cli

### `gh repo autolink create`

```bash
gh repo autolink create TICKET- "https://example.com/TICKET?query=<num>"
```
gh repo autolink create STORY- "https://example.com/STORY?id=<num>" --numeric

### `gh repo clone`

```bash
gh repo clone cli/cli
```
gh repo clone myrepo

```bash
gh repo clone https://github.com/cli/cli
```
gh repo clone git@github.com:cli/cli.git

```bash
gh repo clone cli/cli workspace/cli
```
gh repo clone cli/cli -- --depth=1

### `gh repo create`

```bash
gh repo create my-org/my-project --public
```
gh repo create my-project --private --source=. --remote=upstream

### `gh repo deploy-key add`

```bash
ssh-keygen -t ed25519 -C "my description" -N "" -f ~/.ssh/gh-test
```
gh repo deploy-key add ~/.ssh/gh-test.pub

### `gh repo edit`

```bash
gh repo edit --enable-issues --enable-wiki
```
gh repo edit --enable-projects=false

### `gh repo gitignore view`

```bash
gh repo gitignore view Go
```
gh repo gitignore view Python

```bash
gh repo gitignore view Go > .gitignore
```
gh repo gitignore view Python > .gitignore

### `gh repo license view`

```bash
gh repo license view MIT
```
gh repo license view mit

```bash
gh repo license view AGPL-3.0
```
gh repo license view agpl-3.0

### `gh repo rename`

```bash
gh repo rename baz
```
gh repo rename -R qux/quux baz

### `gh repo set-default`

```bash
gh repo set-default
```
gh repo set-default owner/repo

```bash
gh repo set-default origin
```
gh repo set-default --view

```bash
git remote add newrepo https://github.com/owner/repo
```
gh repo set-default

### `gh repo sync`

```bash
gh repo sync
```
gh repo sync --branch v1

```bash
gh repo sync owner/cli-fork
```
gh repo sync owner/repo --source owner2/repo2

## `gh ruleset`

```bash
gh ruleset list
```
gh ruleset view --repo OWNER/REPO --web

### `gh ruleset check`

```bash
gh ruleset check
```
gh ruleset check my-branch --repo owner/repo

```bash
gh ruleset check --default --repo owner/repo
```
gh ruleset view 23 --repo owner/repo

### `gh ruleset view`

```bash
gh ruleset view
```
gh ruleset view --no-parents

```bash
gh ruleset view 43
```
gh ruleset view 23 --repo owner/repo

### `gh run delete`

```bash
gh run delete
```
gh run delete 12345

### `gh run download`

```bash
gh run download <run-id>
```
gh run download <run-id> -n <name>

```bash
gh run download -n <name1> -n <name2>
```
gh run download

### `gh run view`

```bash
gh run view
```
gh run view 12345

```bash
gh run view 12345 --attempt 3
```
gh run view --job 456789

```bash
gh run view --log --job 456789
```
gh run view 0451 --exit-status && echo "run pending or passed"

### `gh run watch`

```bash
gh run watch
```
gh run watch --compact

### `gh search code`

```bash
gh search code react lifecycle
```
gh search code "error handling"

```bash
gh search code deque --language=python
```
gh search code cli --owner=microsoft

```bash
gh search code panic --repo cli/cli
```
gh search code lint --filename package.json

### `gh search commits`

```bash
gh search commits readme typo
```
gh search commits "bug fix"

```bash
gh search commits --committer=monalisa
```
gh search commits --author-name="Jane Doe"

```bash
gh search commits --hash=8dd03144ffdc6c0d486d6b705f9c7fba871ee7c3
```
gh search commits --author-date="<2022-02-01"

### `gh search issues`

```bash
gh search issues readme typo
```
gh search issues "broken feature"

```bash
gh search issues --include-prs --owner=cli
```
gh search issues --assignee=@me --state=open

```bash
gh search issues --comments=">100"
```
gh search issues -- -label:bug

### `gh search prs`

```bash
gh search prs fix bug
```
gh search prs --repo=cli/cli --draft

```bash
gh search prs --review-requested=@me --state=open
```
gh search prs --assignee=@me --merged

```bash
gh search prs --reactions=">100"
```
gh search prs -- -label:bug

### `gh search repos`

```bash
gh search repos cli shell
```
gh search repos "vim plugin"

```bash
gh search repos --owner=microsoft --visibility=public
```
gh search repos --topic=unix,terminal

```bash
gh search repos --language=go --good-first-issues=">=10"
```
gh search repos -- -topic:linux

### `gh secret set`

```bash
gh secret set MYSECRET
```
gh secret set MYSECRET --body "$ENV_VALUE"

```bash
gh secret set MYSECRET --repo origin/repo --body "$ENV_VALUE"
```
gh secret set MYSECRET < myfile.txt

```bash
gh secret set MYSECRET --env myenvironment
```
gh secret set MYSECRET --org myOrg --visibility all

```bash
gh secret set MYSECRET --org myOrg --repos repo1,repo2,repo3
```
gh secret set MYSECRET --org myOrg --no-repos-selected

```bash
gh secret set MYSECRET --user
```
gh secret set MYSECRET --app dependabot

```bash
gh secret set -f .env
```
gh secret set -f - < myfile.txt

## `gh status`

```bash
gh status -e cli/cli -e cli/go-gh # Exclude multiple repositories
```
gh status -o cli # Limit results to a single organization

### `gh variable set`

```bash
gh variable set MYVARIABLE
```
gh variable set MYVARIABLE --body "$ENV_VALUE"

```bash
gh variable set MYVARIABLE < myfile.txt
```
gh variable set MYVARIABLE --env myenvironment

```bash
gh variable set MYVARIABLE --org myOrg --visibility all
```
gh variable set MYVARIABLE --org myOrg --repos repo1,repo2,repo3

### `gh workflow run`

```bash
gh workflow run
```
gh workflow run triage.yml

```bash
gh workflow run triage.yml --ref my-branch
```
gh workflow run triage.yml -f name=scully -f greeting=hello

### `gh workflow view`

```bash
gh workflow view
```
gh workflow view 0451

