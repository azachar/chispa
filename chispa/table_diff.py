import difflib
from wasabi import color
from chispa.bcolors import *


class DataFramesNotEqualError(Exception):
    """The DataFrames are not equal"""
    pass


class TableDiff:

    def show_failure(self, df1, df2, t):
        df1_as_text = self._getShowString(df1)
        df2_as_text = self._getShowString(df2)
        raise DataFramesNotEqualError(
            "\n" + bcolors.NC +
            "\n** Actual **\n" + df1_as_text +
            "\n** Expected **\n" + df2_as_text +
            "\n** Diff **\n" + self.diff_strings(df1_as_text, df2_as_text) +
            "\n** Comparison **\n" + t.get_string())

    def _getShowString(self, df, n=20, truncate=True, vertical=False):
        if isinstance(truncate, bool) and truncate:
            return(df._jdf.showString(n, 20, vertical))
        else:
            return(df._jdf.showString(n, int(truncate), vertical))

    def diff_strings(self, a, b):
        output = []
        matcher = difflib.SequenceMatcher(None, a, b)
        for opcode, a0, a1, b0, b1 in matcher.get_opcodes():
            if opcode == "equal":
                output.append(a[a0:a1])
            elif opcode == "insert":
                output.append(color(b[b0:b1], fg=16, bg="green"))
            elif opcode == "delete":
                output.append(color(a[a0:a1], fg=16, bg="red"))
            elif opcode == "replace":
                output.append(color(b[b0:b1], fg=16, bg="green"))
                output.append(color(a[a0:a1], fg=16, bg="red"))
        return "".join(output)
