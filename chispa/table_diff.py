import difflib
from wasabi import color, diff_strings
from chispa.bcolors import *


class DataFramesNotEqualError(Exception):
    """The DataFrames are not equal"""
    pass


class TableDiff:

    def show_failure(self, df1, df2, t):
        df1_as_text = self._getShowString(df1)
        df2_as_text = self._getShowString(df2)
        raise DataFramesNotEqualError(
            bcolors.NC + "\n\n" +
            color("** Actual **", fg=16, bg="red") + "\n" +
            df1_as_text + "\n" +
            color("** Expected **", fg=16, bg="green") + "\n" +
            df2_as_text +
            "\n** Diff **\n" + 
            self.diff_strings(df1_as_text, df2_as_text) +
            "\n** Comparison **\n" + t.get_string())

    def _getShowString(self, df, n=20, truncate=True, vertical=False):
        if isinstance(truncate, bool) and truncate:
            return(df._jdf.showString(n, 20, vertical))
        else:
            return(df._jdf.showString(n, int(truncate), vertical))

    def diff_strings(self, a, b):
        return diff_strings(a, b)
