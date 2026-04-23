"""Utility helpers for loading existing legacy check functions by file path."""

from __future__ import annotations

import io
from contextlib import redirect_stdout
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


DEFAULT_FAILURE_TOKENS = ("no connection", "offline", "failed", "error")


def load_legacy_function(module_path: Path, function_name: str):
    """Load a function from an existing script without modifying that script."""
    spec = spec_from_file_location(module_path.stem, module_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not create import spec for {module_path}")

    module = module_from_spec(spec)
    spec.loader.exec_module(module)

    if not hasattr(module, function_name):
        raise AttributeError(f"{module_path} does not define {function_name}")

    return getattr(module, function_name)


def run_and_assess(check_func, *args, failure_tokens=DEFAULT_FAILURE_TOKENS) -> bool:
    """Run a legacy function and infer pass/fail from its printed output."""
    try:
        capture = io.StringIO()
        with redirect_stdout(capture):
            check_func(*args)
        output = capture.getvalue().lower()
    except Exception:
        return False

    return not any(token in output for token in failure_tokens)

