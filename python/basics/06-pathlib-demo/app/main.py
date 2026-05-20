from pathlib import Path


def summarize_path(base: Path) -> dict[str, object]:
    target = base / "notes" / "demo.txt"
    return {
        "target": target,
        "name": target.name,
        "stem": target.stem,
        "suffix": target.suffix,
        "parts": target.parts,
    }


def build_demo_output() -> dict[str, object]:
    return summarize_path(Path("study-record"))


def main() -> None:
    demo_output = build_demo_output()
    print(f"target: {demo_output['target']}")
    print(f"parts: {demo_output['parts']}")


if __name__ == "__main__":
    main()