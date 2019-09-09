def toggle_commit(commit, state):
    action_type = "ADD_COMMIT" if state is True else "REMOVE_COMMIT"
    return {"type": action_type, "payload": commit}


def change_box(box):
    return {"type": "CHANGE_BOX", "payload": box}
