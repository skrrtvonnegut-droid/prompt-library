#!/usr/bin/env python3
"""Validate the Prompt Library catalog and registered artifact paths."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:
    raise SystemExit(
        "PyYAML is required. Install it with: python -m pip install pyyaml"
    ) from exc


ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "catalog.yml"

ALLOWED_KINDS = {"prompt", "skill", "macro", "template"}
ALLOWED_STATUSES = {"developing", "active", "review_due", "superseded", "archived"}
ALLOWED_PUBLIC_CLASSIFICATIONS = {"Public", "Professional Portfolio"}
REQUIRED_ARTIFACT_FIELDS = {
    "id",
    "name",
    "kind",
    "path",
    "domain",
    "status",
    "classification",
    "aliases",
    "summary",
}
ID_PATTERN = re.compile(r"^(prompt|skill|macro|template)\.[a-z0-9][a-z0-9.-]*$")
DOMAIN_PATTERN = re.compile(r"^[a-z0-9][a-z0-9.-]*$")


def load_yaml(path: Path) -> dict[str, Any]:
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise SystemExit(f"Catalog not found: {path.relative_to(ROOT)}")
    except yaml.YAMLError as exc:
        raise SystemExit(f"Invalid YAML in {path.relative_to(ROOT)}: {exc}") from exc

    if not isinstance(data, dict):
        raise SystemExit("catalog.yml must contain a mapping at the document root.")
    return data


def selector_key(value: str) -> str:
    """Normalize human-facing selectors while preserving meaningful punctuation."""
    return value.strip().casefold()


def validate_catalog(catalog: dict[str, Any]) -> list[str]:
    errors: list[str] = []

    if catalog.get("schema_version") != 2:
        errors.append("schema_version must be 2.")

    repository = catalog.get("repository")
    if not isinstance(repository, dict):
        errors.append("repository must be a mapping.")
        repository = {}

    for field in (
        "artifact_id",
        "name",
        "canonical_home",
        "classification",
        "contract",
        "schema",
        "invocation",
    ):
        if field not in repository:
            errors.append(f"repository.{field} is required.")

    if repository.get("canonical_home") != "github":
        errors.append("repository.canonical_home must be 'github'.")

    if repository.get("classification") != "Public":
        errors.append("The public registry repository classification must be 'Public'.")

    for metadata_path_field in ("contract", "schema"):
        value = repository.get(metadata_path_field)
        if isinstance(value, str):
            candidate = ROOT / value
            if not candidate.is_file():
                errors.append(
                    f"repository.{metadata_path_field} points to a missing file: {value}"
                )

    schema_path = repository.get("schema")
    if isinstance(schema_path, str) and (ROOT / schema_path).is_file():
        try:
            json.loads((ROOT / schema_path).read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"{schema_path} is not valid JSON: {exc}")

    kinds = catalog.get("artifact_kinds")
    if not isinstance(kinds, dict):
        errors.append("artifact_kinds must be a mapping.")
    else:
        missing_kinds = ALLOWED_KINDS - set(kinds)
        if missing_kinds:
            errors.append(
                "artifact_kinds is missing: " + ", ".join(sorted(missing_kinds))
            )

    artifacts = catalog.get("artifacts")
    if not isinstance(artifacts, list):
        errors.append("artifacts must be a list.")
        return errors

    seen_ids: dict[str, int] = {}
    seen_paths: dict[str, str] = {}
    seen_aliases: dict[str, str] = {}
    seen_names: dict[str, str] = {}

    for index, artifact in enumerate(artifacts, start=1):
        label = f"artifacts[{index}]"
        if not isinstance(artifact, dict):
            errors.append(f"{label} must be a mapping.")
            continue

        missing = REQUIRED_ARTIFACT_FIELDS - set(artifact)
        if missing:
            errors.append(f"{label} is missing: {', '.join(sorted(missing))}")

        artifact_id = artifact.get("id")
        kind = artifact.get("kind")
        path_value = artifact.get("path")
        name = artifact.get("name")
        aliases = artifact.get("aliases")
        status = artifact.get("status")
        classification = artifact.get("classification")
        domain = artifact.get("domain")
        summary = artifact.get("summary")

        if not isinstance(artifact_id, str) or not ID_PATTERN.fullmatch(artifact_id):
            errors.append(f"{label}.id is invalid: {artifact_id!r}")
        else:
            if artifact_id in seen_ids:
                errors.append(
                    f"Duplicate artifact ID {artifact_id!r} in entries "
                    f"{seen_ids[artifact_id]} and {index}."
                )
            seen_ids[artifact_id] = index

        if kind not in ALLOWED_KINDS:
            errors.append(f"{label}.kind must be one of {sorted(ALLOWED_KINDS)}.")
        elif isinstance(artifact_id, str):
            id_kind = artifact_id.split(".", 1)[0]
            if id_kind != kind:
                errors.append(
                    f"{label}.kind {kind!r} does not match ID prefix {id_kind!r}."
                )

        if status not in ALLOWED_STATUSES:
            errors.append(f"{label}.status must be one of {sorted(ALLOWED_STATUSES)}.")

        if classification not in ALLOWED_PUBLIC_CLASSIFICATIONS:
            errors.append(
                f"{label}.classification {classification!r} is not allowed in "
                "the public registry."
            )

        if not isinstance(domain, str) or not DOMAIN_PATTERN.fullmatch(domain):
            errors.append(f"{label}.domain is invalid: {domain!r}")

        if not isinstance(name, str) or not name.strip():
            errors.append(f"{label}.name must be a non-empty string.")
        else:
            name_key = selector_key(name)
            if name_key in seen_names:
                errors.append(
                    f"Duplicate artifact name {name!r} for "
                    f"{seen_names[name_key]!r} and {artifact_id!r}."
                )
            seen_names[name_key] = str(artifact_id)

        if not isinstance(summary, str) or len(summary.strip()) < 12:
            errors.append(f"{label}.summary must be a meaningful one-line description.")

        if not isinstance(path_value, str) or not path_value.strip():
            errors.append(f"{label}.path must be a non-empty relative path.")
        else:
            path = Path(path_value)
            if path.is_absolute() or ".." in path.parts:
                errors.append(f"{label}.path must stay inside the repository: {path_value}")
            else:
                normalized_path = path.as_posix()
                if normalized_path in seen_paths:
                    errors.append(
                        f"Duplicate registered path {normalized_path!r} for "
                        f"{seen_paths[normalized_path]!r} and {artifact_id!r}."
                    )
                seen_paths[normalized_path] = str(artifact_id)
                if not (ROOT / path).is_file():
                    errors.append(
                        f"{label}.path does not exist: {normalized_path}"
                    )

        if not isinstance(aliases, list):
            errors.append(f"{label}.aliases must be a list.")
        else:
            local_aliases: set[str] = set()
            for alias in aliases:
                if not isinstance(alias, str) or not alias.strip():
                    errors.append(f"{label}.aliases contains an invalid alias: {alias!r}")
                    continue
                key = selector_key(alias)
                if key in local_aliases:
                    errors.append(f"{label}.aliases repeats {alias!r}.")
                local_aliases.add(key)
                if key in seen_aliases:
                    errors.append(
                        f"Alias collision {alias!r} between "
                        f"{seen_aliases[key]!r} and {artifact_id!r}."
                    )
                seen_aliases[key] = str(artifact_id)

    artifact_ids = set(seen_ids)
    for index, artifact in enumerate(artifacts, start=1):
        if not isinstance(artifact, dict):
            continue
        successor = artifact.get("superseded_by")
        if successor is not None and successor not in artifact_ids:
            errors.append(
                f"artifacts[{index}].superseded_by references unknown ID {successor!r}."
            )

    return errors


def main() -> int:
    catalog = load_yaml(CATALOG_PATH)
    errors = validate_catalog(catalog)

    if errors:
        print(f"Catalog validation failed with {len(errors)} error(s):", file=sys.stderr)
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
        return 1

    print(
        f"Catalog valid: {len(catalog['artifacts'])} registered artifacts "
        f"across {len(ALLOWED_KINDS)} artifact kinds."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
