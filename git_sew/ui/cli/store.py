import warnings

import pydux

from frozendict import frozendict

from . import reducers

reducers_map = {
    "CHANGE_BOX": reducers.change_box,
    "ADD_COMMIT": reducers.add_commit,
    "REMOVE_COMMIT": reducers.remove_commit,
    "CLEAR_COMMITS": reducers.clear_commits,
    "LOAD_COMMITS": reducers.load_commits,
    "REBASE": reducers.rebase,
}


initial = {"commits": [], "selected": [], "box": None}


def reducer(state, action):
    if action["type"] not in reducers_map:
        warnings.warn(f"Unhandled action \"{action['type']}\".", UserWarning)
        return state.copy()
    return reducers_map[action["type"]](state, action)


store = pydux.create_store(reducer, initial_state=frozendict(initial))
