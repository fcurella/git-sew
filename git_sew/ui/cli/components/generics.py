import urwid

from urwid_pydux import Component


class Container(urwid.Padding):
    def __init__(self, box):
        super().__init__(box, left=2, right=2)


class OrderedList(Component):
    prop_types = {"items": list}

    def render_component(self, props):
        return urwid.ListBox(urwid.SimpleFocusListWalker(props["items"]))


class ListItem(Component):
    prop_types = {
        "text": str,
        # "on_click": callable,
    }

    def render_component(self, props):
        return urwid.AttrMap(
            urwid.SelectableIcon([u"  \N{BULLET} ", props["text"].strip()], 2),
            None,
            "selected",
        )

    def on_click(self):
        self.props["on_click"]()


class CheckBoxItem(Component):
    prop_types = {
        "text": str,
        "on_state_change": callable,
        "user_data": dict,
        "selected": bool,
    }

    def render_component(self, props):
        return urwid.AttrMap(
            urwid.CheckBox(
                props["text"].strip(),
                state=props["selected"],
                on_state_change=props["on_state_change"],
                user_data=props.get("user_data"),
            ),
            None,
            "selected",
        )
