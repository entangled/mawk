# ~\~ language=Python filename=test/test_markdown_outliner.py
# ~\~ begin <<README.md|test/test_markdown_outliner.py>>[init]
from dataclasses import dataclass
import mawk
import re


@dataclass
class Outliner(mawk.RuleSet):
    ignore: bool = False

    @mawk.on_match(r"^#.*$")
    def on_header(self, m: re.Match):
        if self.ignore:
            return
        return [m[0]]

    @mawk.on_match(r"^```")
    def on_codeblock(self, _):
        self.ignore = not self.ignore
        return []

    @mawk.always
    def otherwise(self, _):
        return []


if __name__ == "__main__":
    with open("README.md", "r") as f:
        print(Outliner().run(f.read()))
# ~\~ end
