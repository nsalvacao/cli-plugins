---
name: cli-node
description: >-
  This skill should be used when the user needs help with node CLI commands, flags, and troubleshooting.
---

# node CLI Reference

Compact command reference for **node** v25.2.1.

- **0** total commands
- **0** command flags + **144** global flags
- **0** extracted usage examples
- Max nesting depth: 0

## When to Use

- Constructing or validating `node` commands
- Looking up flags/options fast
- Troubleshooting failed invocations

## Top-Level Commands

Command format examples: 

### Global Flags

| Flag | Short | Type | Description |
| --- | --- | --- | --- |
| `--abort-on-uncaught-exception` | `` | string | aborting instead of exiting causes a core file to be generated for analysis |
| `--allow-addons` | `` | bool | allow use of addons when any |
| `--allow-child-process` | `` | bool | allow use of child process when any |
| `--allow-fs-read` | `` | string | allow permissions to read the |
| `--allow-fs-write` | `` | string | allow permissions to write in the |
| `--allow-inspector` | `` | bool | allow use of inspector when any |
| `--allow-net` | `` | bool | allow use of network when any |
| `--allow-wasi` | `` | bool | allow wasi when any permissions are set |
| `--allow-worker` | `` | bool | allow worker threads when any |
| `--build-snapshot` | `` | bool | Generate a snapshot blob when the |
| `--check` | `-c` | bool | syntax check script without executing |
| `--completion-bash` | `` | bool | print source-able bash completion |
| `--conditions` | `-C` | string | additional user conditions for |
| `--cpu-prof` | `` | string | Start the V8 CPU profiler on start up, |
| `--cpu-prof-dir` | `` | string | Directory where the V8 profiles |
| `--cpu-prof-interval` | `` | string | specified sampling interval in |
| `--cpu-prof-name` | `` | string | specified file name of the V8 CPU |
| `--diagnostic-dir` | `` | string | set dir for all output files (default: |
| `--disable-proto` | `` | string | disable Object.prototype.__proto__ |
| `--disable-sigusr1` | `` | bool | Disable inspector thread to be |
| `--disable-warning` | `` | string | silence specific process warnings |
| `--disallow-code-generation-from-strings` | `` | bool | disallow eval and friends |
| `--dns-result-order` | `` | string | set default value of verbatim in |
| `--enable-etw-stack-walking` | `` | bool | provides heap data to ETW Windows |
| `--enable-fips` | `` | bool | enable FIPS crypto at startup |
| `--enable-source-maps` | `` | bool | Source Map V3 support for stack traces |
| `--entry-url` | `` | string | Treat the entrypoint as a URL |
| `--env-file` | `` | string | set environment variables from supplied |
| `--env-file-if-exists` | `` | string | set environment variables from supplied |
| `--eval` | `-e` | string | evaluate script |
| `--experimental-addon-modules` | `` | bool | experimental import support for addons |
| `--experimental-default-config-file` | `` | string | set config file from default config file |
| `--experimental-eventsource` | `` | bool | experimental EventSource API |
| `--experimental-import-meta-resolve` | `` | string | experimental ES Module import.meta.resolve() parentURL support |
| `--experimental-inspector-network-resource` | `` | bool | experimental load network resources via the inspector |
| `--experimental-network-inspection` | `` | bool | experimental network inspection support |
| `--experimental-print-required-tla` | `` | bool | Print pending top-level await. If |
| `--experimental-quic` | `` | bool | experimental QUIC support |
| `--experimental-test-coverage` | `` | bool | enable code coverage in the test runner |
| `--experimental-test-module-mocks` | `` | bool | enable module mocking in the test runner |
| `--experimental-transform-types` | `` | bool | enable transformation of TypeScript-onlysyntax into JavaScript code |
| `--experimental-vm-modules` | `` | bool | experimental ES Module support in vm |
| `--experimental-worker-inspection` | `` | bool | experimental worker inspection support |
| `--expose-gc` | `` | bool | expose gc extension |
| `--force-context-aware` | `` | bool | disable loading non-context-aware |
| `--force-fips` | `` | bool | force FIPS crypto (cannot be disabled) |
| `--force-node-api-uncaught-exceptions-policy` | `` | bool | enforces 'uncaughtException' event on Node API asynchronous callbacks |
| `--frozen-intrinsics` | `` | bool | experimental frozen intrinsics support |
| `--heap-prof` | `` | string | Start the V8 heap profiler on start up, |
| `--heap-prof-dir` | `` | string | Directory where the V8 heap profiles |
| `--heap-prof-interval` | `` | string | specified sampling interval in bytes |
| `--heap-prof-name` | `` | string | specified file name of the V8 heap |
| `--heapsnapshot-signal` | `` | string | Generate heap snapshot on specified |
| `--help` | `-h` | bool | print node command line options |
| `--icu-data-dir` | `` | string | set ICU data load path to dir |
| `--import` | `` | string | ES module to preload (option can be |
| `--input-type` | `` | string | set module type for string input |
| `--insecure-http-parser` | `` | bool | use an insecure HTTP parser that |
| `--inspect-publish-uid` | `` | string | comma separated list of destinations |
| `--interactive` | `-i` | bool | always enter the REPL even if stdin |
| `--interpreted-frames-native-stack` | `` | string | help system profilers to translate JavaScript interpreted frames |
| `--jitless` | `` | bool | disable runtime allocation of |
| `--localstorage-file` | `` | string | file used to persist localStorage data |
| `--max-http-header-size` | `` | string | set the maximum size of HTTP headers |
| `--no-addons` | `` | bool | disable loading native addons |
| `--no-async-context-frame` | `` | bool | Improve AsyncLocalStorage performance |
| `--no-deprecation` | `` | bool | silence deprecation warnings |
| `--no-experimental-detect-module` | `` | bool | when ambiguous modules fail to evaluate because they contain ES module syntax, try again to evaluate them as ES modules |
| `--no-experimental-global-navigator` | `` | bool | expose experimental Navigator API on the global scope |
| `--no-experimental-repl-await` | `` | bool | experimental await keyword support in REPL |
| `--no-experimental-require-module` | `` | bool | Allow loading synchronous ES Modules in require(). |
| `--no-experimental-sqlite` | `` | bool | experimental node:sqlite module |
| `--no-extra-info-on-fatal-exception` | `` | bool | hide extra information on fatal exception that causes exit |
| `--no-force-async-hooks-checks` | `` | bool | disable checks for async_hooks |
| `--no-global-search-paths` | `` | bool | disable global module search paths |
| `--no-warnings` | `` | bool | silence all process warnings |
| `--node-memory-debug` | `` | bool | Run with extra debug checks for memory |
| `--openssl-config` | `` | string | load OpenSSL configuration from the |
| `--openssl-legacy-provider` | `` | bool | enable OpenSSL 3.0 legacy provider |
| `--openssl-shared-config` | `` | bool | enable OpenSSL shared configuration |
| `--pending-deprecation` | `` | bool | emit pending deprecation warnings |
| `--permission` | `` | bool | enable the permission system |
| `--preserve-symlinks` | `` | bool | preserve symbolic links when resolving |
| `--preserve-symlinks-main` | `` | bool | preserve symbolic links when resolving |
| `--print` | `-p` | string | evaluate script and print result |
| `--prof` | `` | string | Generate V8 profiler output. |
| `--prof-process` | `` | string | process V8 profiler output generated |
| `--redirect-warnings` | `` | string | write warnings to file instead of |
| `--report-compact` | `` | bool | output compact single-line JSON |
| `--report-exclude-env` | `` | bool | Exclude environment variables when |
| `--report-exclude-network` | `` | bool | exclude network interface diagnostics. |
| `--report-filename` | `` | string | define custom report file name. |
| `--report-on-fatalerror` | `` | bool | generate diagnostic report on fatal |
| `--report-on-signal` | `` | bool | generate diagnostic report upon |
| `--report-signal` | `` | string | causes diagnostic report to be produced |
| `--require` | `-r` | string | CommonJS module to preload (option can |
| `--run` | `` | string | Run a script specified in package.json |
| `--secure-heap` | `` | string | total size of the OpenSSL secure heap |
| `--secure-heap-min` | `` | string | minimum allocation size from the |
| `--snapshot-blob` | `` | string | Path to the snapshot blob that's either |
| `--test` | `` | bool | launch test runner on startup |
| `--test-concurrency` | `` | string | specify test runner concurrency |
| `--test-coverage-lines` | `` | string | the line coverage minimum threshold |
| `--test-force-exit` | `` | bool | force test runner to exit upon |
| `--test-global-setup` | `` | string | specifies the path to the global setup |
| `--test-name-pattern` | `` | string | run tests whose name matches this |
| `--test-only` | `` | bool | run tests with 'only' option set |
| `--test-reporter` | `` | string | report test output using the given |
| `--test-rerun-failures` | `` | string | specifies the path to the rerun state |
| `--test-shard` | `` | string | run test at specific shard |
| `--test-skip-pattern` | `` | string | run tests whose name do not match this |
| `--test-timeout` | `` | string | specify test runner timeout |
| `--test-update-snapshots` | `` | bool | regenerate test snapshots |
| `--throw-deprecation` | `` | bool | throw an exception on deprecations |
| `--title` | `` | string | the process title to use on startup |
| `--tls-cipher-list` | `` | string | use an alternative default TLS cipher |
| `--tls-keylog` | `` | string | log TLS decryption keys to named file |
| `--trace-deprecation` | `` | bool | show stack traces on deprecations |
| `--trace-env` | `` | bool | Print accesses to the environment |
| `--trace-env-js-stack` | `` | bool | Print accesses to the environment |
| `--trace-env-native-stack` | `` | bool | Print accesses to the environment |
| `--trace-exit` | `` | bool | show stack trace when an environment |
| `--trace-promises` | `` | bool | show stack traces on promise |
| `--trace-require-module` | `` | string | Print access to require(esm). Options |
| `--trace-sigint` | `` | bool | enable printing JavaScript stacktrace |
| `--trace-sync-io` | `` | bool | show stack trace when use of sync IO is |
| `--trace-tls` | `` | bool | prints TLS packet trace information to |
| `--trace-uncaught` | `` | bool | show stack traces for the `throw` |
| `--trace-warnings` | `` | bool | show stack traces on process warnings |
| `--track-heap-objects` | `` | bool | track heap object allocations for heap |
| `--unhandled-rejections` | `` | string | define unhandled rejections behavior. |
| `--use-bundled-ca` | `` | bool | use bundled CA store (default) |
| `--use-env-proxy` | `` | bool | parse proxy settings from |
| `--use-largepages` | `` | string | Map the Node.js static code to large |
| `--use-openssl-ca` | `` | bool | use OpenSSL's default CA store |
| `--use-system-ca` | `` | bool | use system's CA store |
| `--v8-options` | `` | bool | print V8 command line options |
| `--v8-pool-size` | `` | string | set V8's thread pool size |
| `--version` | `-v` | bool | print Node.js version |
| `--watch` | `` | bool | run in watch mode |
| `--watch-kill-signal` | `` | string | kill signal to send to the process on |
| `--watch-path` | `` | string | path to watch |
| `--watch-preserve-output` | `` | bool | preserve outputs on watch mode restart |
| `--zero-fill-buffers` | `` | bool | automatically zero-fill all newly |

## Common Usage Patterns (Compact)

_No examples extracted._
## Detailed References

- Full command tree: `references/commands.md`
- Full examples catalog: `references/examples.md`

## Re-Scanning

After a CLI update, run `/scan-cli` or execute crawler + generator again.
