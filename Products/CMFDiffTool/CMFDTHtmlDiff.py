from Globals import InitializeClass
from TextDiff import TextDiff
from interfaces.portal_diff import IDifference
from libs import htmldiff

# Give it a dumb name so it doesn't conflict with all the other html diffs
# around.  This uses Ian Bicking's very nice htmldiff.py from Web Ware for
# Python.
class CMFDTHtmlDiff(TextDiff):
    """Text difference"""

    __implements__ = (IDifference)

    meta_type = "HTML Diff"

    def inline_diff(self):
        """Return a specialized diff for HTML"""
        a = '\n'.join(self._parseField(self.oldValue))
        b = '\n'.join(self._parseField(self.newValue))
        return htmldiff.htmldiff(a, b)

InitializeClass(CMFDTHtmlDiff)
