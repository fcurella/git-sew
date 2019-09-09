import urwid

from urwid_pydux import Component


class Loading(Component):
    def render_component(self, props):
        return urwid.Padding(urwid.Filler(urwid.Text("")), left=2, right=2)


class Footer(Component):
    def render_component(self, props):
        return urwid.Text("(Q)uit (C)lear (^w)rite to disk")
