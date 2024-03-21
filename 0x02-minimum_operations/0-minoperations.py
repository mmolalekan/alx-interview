#!/usr/bin/python3
"""
module documentation
"""


def minOperations(n):
    """
    function documentation
    """
    if not isinstance(n, int):
        return 0
    operation_count = 0
    clipboard_contents = 0
    complet = 1
    while complet < n:
        if clipboard_contents == 0:
            clipboard_contents = complet
            complet += clipboard_contents
            operation_count += 2
        elif n - complet > 0 and (n - complet) % complet == 0:
            clipboard_contents = complet
            complet += clipboard_contents
            operation_count += 2
        elif clipboard_contents > 0:
            complet += clipboard_contents
            operation_count += 1
    return operation_count
