import os

import click
import urwid

from urwid_pydux import subscribe_urwid_redraw

from .actions import change_box
from .components.generics import Container, ListItem, OrderedList
from .containers.App import App
from .containers.CommitList import CommitList
from .containers.StateView import StateView
from .store import store

palette = [
    (None, "light gray", "black"),
    ("heading", "black", "light gray"),
    ("line", "black", "light gray"),
    ("options", "dark gray", "black"),
    ("focus heading", "white", "dark red"),
    ("focus line", "black", "dark red"),
    ("focus options", "black", "light gray"),
    ("selected", "white", "dark blue"),
]

focus_map = {
    "heading": "focus heading",
    "options": "focus options",
    "line": "focus line",
}


def render(repo_path):
    store.dispatch({"type": "LOAD_COMMITS", "payload": repo_path})

    commit_list = CommitList(store=store)
    state_view = StateView(store=store)

    root = App(store=store)

    def show_or_exit(key):
        if key in ("q", "Q"):
            raise urwid.ExitMainLoop()
        elif key in ("d", "D"):
            box = state_view
        elif key in ("l", "L"):
            box = commit_list
        elif key in ("c", "C"):
            store.dispatch({"type": "CLEAR_COMMITS"})
            return
        elif key in ("ctrl w"):
            store.dispatch({"type": "REBASE"})
            return
        else:
            box = Container(OrderedList(items=[ListItem(text=repr(key))]))

        store.dispatch(change_box(box))

    store.dispatch(change_box(commit_list))
    loop = urwid.MainLoop(root, palette, unhandled_input=show_or_exit)
    subscribe_urwid_redraw(store, loop)
    loop.run()


@click.command()
def main():
    repo_path = os.path.abspath(".")

    render(repo_path)
