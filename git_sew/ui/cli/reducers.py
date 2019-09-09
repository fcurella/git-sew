import os

import urwid

from git import Repo

from git_sew.fixup import fixup


def load_commits(state, action):
    path = os.path.abspath(action["payload"])
    repo = Repo(path)
    commits = list(repo.iter_commits())

    return state.copy(repo_path=path, commits=commits)


def add_commit(state, action):
    selected = state["selected"]
    selected.insert(0, action["payload"])
    selected = sorted(selected, key=lambda c: c.committed_date)
    return state.copy(selected=selected)


def remove_commit(state, action):
    selected = [commit for commit in state["selected"] if commit != action["payload"]]
    return state.copy(selected=selected)


def clear_commits(state, action):
    return state.copy(selected=[])


def change_box(state, action):
    return state.copy(box=action["payload"])


def rebase(state, action):
    repo_path = state["repo_path"]
    refs = [commit.hexsha for commit in state["selected"]]
    fixup(refs, repo_path)

    raise urwid.ExitMainLoop()
