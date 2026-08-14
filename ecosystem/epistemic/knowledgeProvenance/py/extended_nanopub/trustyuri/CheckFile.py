import codecs
import logging
import sys

from extended_nanopub.trustyuri import ModuleDirectory, TrustyUriUtils
from extended_nanopub.trustyuri.TrustyUriResource import TrustyUriResource

try:
    from urllib.request import urlopen
except Exception:
    from urllib.request import urlopen


def check(args):
    filename = args[0]

    tail = TrustyUriUtils.get_trustyuri_tail(filename)
    module_id = tail[:2]
    module = ModuleDirectory.get_module(module_id)
    try:
        content = codecs.open(filename, 'r', 'utf-8').read()
    except Exception:
        content = urlopen(filename).read()
    resource = TrustyUriResource(filename, content, tail)
    if module.has_correct_hash(resource):
        print("Correct hash: " + tail)
    else:
        print("*** INCORRECT HASH ***")


if __name__ == "__main__":
    logging.basicConfig(level=logging.ERROR)
    args = sys.argv
    args.pop(0)
    check(args)
