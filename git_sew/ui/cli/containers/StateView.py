from urwid_pydux import ConnectedComponent

from git_sew.ui.cli.components.generics import ListItem, OrderedList


class StateView(ConnectedComponent):
    def map_state_to_props(self, state, own_props):
        return {"items": [ListItem(text=f"{k}: {v}") for k, v in state.items()]}

    def render_component(self, props):
        return OrderedList(items=props["items"])
