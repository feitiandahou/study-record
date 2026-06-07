from dataclasses import dataclass, field
from typing import Protocol


class Command(Protocol):
    def execute(self) -> str:
        ...

    def undo(self) -> str:
        ...


@dataclass(slots=True)
class TextEditor:
    content: str = ""

    def append(self, text: str) -> str:
        self.content += text
        return self.content

    def replace(self, text: str) -> str:
        self.content = text
        return self.content


@dataclass(slots=True)
class AppendTextCommand:
    editor: TextEditor
    text: str

    def execute(self) -> str:
        return self.editor.append(self.text)

    def undo(self) -> str:
        self.editor.content = self.editor.content[: -len(self.text)]
        return self.editor.content


@dataclass(slots=True)
class ReplaceTextCommand:
    editor: TextEditor
    text: str
    _previous_content: str = ""

    def execute(self) -> str:
        self._previous_content = self.editor.content
        return self.editor.replace(self.text)

    def undo(self) -> str:
        return self.editor.replace(self._previous_content)


@dataclass(slots=True)
class EditorInvoker:
    _history: list[Command] = field(default_factory=list)

    def run(self, command: Command) -> str:
        self._history.append(command)
        return command.execute()

    def undo_last(self) -> str | None:
        if not self._history:
            return None
        return self._history.pop().undo()


def main() -> None:
    editor = TextEditor()
    invoker = EditorInvoker()

    print(invoker.run(AppendTextCommand(editor, "Design patterns")))
    print(invoker.run(ReplaceTextCommand(editor, "Design patterns in Python")))
    print(invoker.undo_last())


if __name__ == "__main__":
    main()
