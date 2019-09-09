import urwid

from urwid_pydux import ConnectedComponent

from git_sew.ui.cli.components.gitlogs import Footer, Loading


class App(ConnectedComponent):
    def map_state_to_props(self, state, own_props):
        return {"body": state["box"]}

    def render_component(self, props):
        if props["body"] is None:
            body = Loading()
        else:
            body = props["body"]
        return urwid.Padding(urwid.Frame(body, footer=Footer()), left=2, right=2)
