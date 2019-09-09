from git import Commit
from urwid_pydux import ConnectedComponent

from git_sew.ui.cli.actions import toggle_commit
from git_sew.ui.cli.components.generics import CheckBoxItem


class CommitItem(ConnectedComponent):
    prop_types = {"store": dict, "commit": Commit}

    def map_state_to_props(self, state, own_props):
        return {
            "text": own_props["commit"].message,
            "user_data": {"commit": own_props["commit"]},
            "selected": own_props["commit"] in state["selected"],
        }

    def map_dispatch_to_props(self, dispatch, own_props):
        def on_commit_change(item, state, user_data):
            dispatch(toggle_commit(user_data["commit"], state))

        return {"on_state_change": on_commit_change}

    def render_component(self, props):
        return CheckBoxItem(
            text=props["text"],
            on_state_change=props["on_state_change"],
            user_data=props["user_data"],
            selected=props["selected"],
        )
