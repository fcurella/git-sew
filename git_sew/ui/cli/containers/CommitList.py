from urwid_pydux import ConnectedComponent

from ..components.generics import OrderedList
from .CommitItem import CommitItem


class CommitList(ConnectedComponent):
    def map_state_to_props(self, state, own_props):
        return {"commits": state["commits"]}

    def render_component(self, props):
        items = [
            CommitItem(store=props["store"], commit=commit)
            for commit in props["commits"]
        ]
        return OrderedList(items=items)
