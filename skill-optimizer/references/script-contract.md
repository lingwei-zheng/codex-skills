# Script Contract

Use this contract whenever a skill contains `scripts/` or another executable
helper.

## Required

- Every Python file parses with `ast.parse`.
- Repeated or fragile operations have a deterministic test, self-test, or
  validator.
- Tests run without network access unless network behavior is the feature under
  test and is explicitly mocked or isolated.
- Paths derive from arguments, the skill root, environment variables, or the
  current workspace rather than a named user's home directory.
- Failures return a non-zero exit code and a concise actionable message.

## Unsafe By Default

- `eval` or `exec`;
- `os.system`;
- `subprocess` with `shell=True`;
- code assembled from untrusted text;
- destructive filesystem actions without resolved-path containment checks;
- Python filenames that shadow standard-library modules.

An exception requires an explicit rationale, bounded input, and a targeted test.

## Test Placement

Use one of:

- `tests/test_*.py`;
- `scripts/test_*.py`;
- a clearly named deterministic `validate_*.py`, `check_*.py`, or
  `verify_*.ps1` for a simple validator-style skill.

Run the narrow test first, then the skill audit. Do not treat an eval transcript
or a human checklist as an executable test.

## Structural Checks

- `SKILL.md` local links resolve.
- Reference links resolve.
- Only the intended parent `SKILL.md` is registered.
- Scripts do not contain user-specific absolute paths.
- Generated caches and temporary outputs are excluded from the skill folder.
