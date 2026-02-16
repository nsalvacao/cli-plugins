"""Thread-safety tests for discovery CrawlState."""

from __future__ import annotations

import concurrent.futures

from crawler.discovery import CrawlState


def test_mark_visited_is_atomic() -> None:
    state = CrawlState()
    paths = ["demo run"] * 100 + [f"demo cmd-{i}" for i in range(100)]

    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        results = list(pool.map(state.mark_visited, paths))

    assert results.count(True) == 101
    assert len(state.visited) == 101


def test_error_and_warning_updates_are_thread_safe() -> None:
    state = CrawlState()

    def worker(i: int) -> None:
        state.increment_errors()
        state.add_warning(f"warn-{i}")

    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        list(pool.map(worker, range(200)))

    assert state.errors == 200
    assert len(state.warnings) == 200
