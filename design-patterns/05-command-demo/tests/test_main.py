from app.main import AppendTextCommand, EditorInvoker, ReplaceTextCommand, TextEditor


def test_editor_invoker_executes_append_command() -> None:
    editor = TextEditor()
    invoker = EditorInvoker()

    result = invoker.run(AppendTextCommand(editor, "Hello"))

    assert result == "Hello"
    assert editor.content == "Hello"


def test_editor_invoker_can_undo_replace_command() -> None:
    editor = TextEditor(content="Draft")
    invoker = EditorInvoker()

    invoker.run(ReplaceTextCommand(editor, "Published"))
    reverted = invoker.undo_last()

    assert reverted == "Draft"
    assert editor.content == "Draft"
