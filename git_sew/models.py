class Todo:
    def __init__(self, repo):
        self.repo = repo
        self.lines = []

    def parse(self, content):
        self.lines = []
        for line in content:
            if line.strip() == "" or line.startswith("#"):
                continue
            action, sha, message = line.split(" ", 2)
            commit = self.repo.commit(sha)
            self.lines.append(ParsedLine(action, commit))


class ParsedLine:
    def __init__(self, action, commit):
        self.action = action
        self.commit = commit

    @property
    def to_line(self):
        return f"{self.action} {self.commit.hexsha} {self.commit.message}"
