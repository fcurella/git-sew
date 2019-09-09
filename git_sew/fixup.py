import logging
import os

import click

from git import Repo

from .models import ParsedLine, Todo

logger = logging.getLogger(__name__)
outfile = os.path.join(os.path.dirname(__file__), "log.txt")
outfile2 = os.path.join(os.path.dirname(__file__), "log2.txt")


@click.command()
@click.argument("repo_path")
@click.argument("refs", nargs=-1)
@click.argument("todo_path")
def fixup_editor(repo_path, refs, todo_path):
    if len(refs) == 0:
        click.echo("Nothing to do.")
        return

    repo = Repo(repo_path)
    commits = [repo.commit(ref) for ref in refs]

    with open(todo_path, "r") as fh:
        todo_content = fh.readlines()
    with open(outfile, "w") as out:
        out.writelines(todo_content)

    base, *rest = commits
    todo = Todo(repo)
    todo.parse(todo_content)

    head = []
    fixups = []
    tail = []
    for parsed in todo.lines:
        if parsed.commit == base:
            head.append(parsed)
        elif parsed.commit not in rest:
            tail.append(parsed)
        else:
            fixups.append(ParsedLine("fixup", parsed.commit))

    todo_content = head + fixups + tail

    with open(todo_path, "w") as fh:
        for item in todo_content:
            fh.write(item.to_line)


@click.command()
@click.argument("refs", nargs=-1)
@click.option("path", "--path", default=".", type=click.Path(exists=True))
def fixup(refs, path):
    repo_path = os.path.abspath(path)
    repo = Repo(repo_path)
    git = repo.git
    commits = [repo.commit(ref) for ref in refs]
    commits.sort(key=lambda c: c.committed_date)

    if len(refs) == 0:
        click.echo("Nothing to do.")
        return
    base = commits[0].parents[0]
    os.environ[
        "GIT_SEQUENCE_EDITOR"
    ] = f"fixup-editor {repo_path} {' '.join([c.hexsha for c in commits])}"
    git.rebase("-i", base.hexsha)
