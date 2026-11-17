"""Minimal Paradox script parser for HOI4 focus files.

Produces a list of Node(key, op, value, start, end) where value is either a
string or a list of Nodes (block). start/end are character offsets into the
source text so raw block text can be copied verbatim.
"""

import re

_TOKEN_RE = re.compile(
    r'\s+|#[^\n]*|"(?:[^"\\]|\\.)*"|<=|>=|!=|[{}=<>]|[^\s{}=<>#"]+',
)


class Node(object):
    __slots__ = ("key", "op", "value", "start", "end", "vstart", "vend")

    def __init__(self, key, op, value, start, end, vstart, vend):
        self.key = key
        self.op = op
        self.value = value
        self.start = start
        self.end = end
        self.vstart = vstart  # start of value (for blocks: just after '{')
        self.vend = vend      # end of value (for blocks: position of '}')

    def is_block(self):
        return isinstance(self.value, list)

    def __repr__(self):
        return "Node(%r %s %r)" % (self.key, self.op, self.value if not self.is_block() else "{...}")


def tokenize(text):
    out = []
    for m in _TOKEN_RE.finditer(text):
        tok = m.group(0)
        if tok[0].isspace() or tok[0] == "#":
            continue
        out.append((tok, m.start(), m.end()))
    return out


class ParseError(Exception):
    pass


def parse(text):
    toks = tokenize(text)
    pos = [0]

    def parse_block(closing):
        items = []
        while pos[0] < len(toks):
            tok, s, e = toks[pos[0]]
            if tok == "}":
                if closing:
                    return items, s
                pos[0] += 1  # stray brace at top level; skip
                continue
            key, kstart = tok, s
            pos[0] += 1
            op = None
            if pos[0] < len(toks) and toks[pos[0]][0] in ("=", "<", ">", "<=", ">=", "!="):
                op = toks[pos[0]][0]
                pos[0] += 1
            if op is None:
                # bare value inside a list block (e.g. { A B C })
                items.append(Node(key, None, None, kstart, e, kstart, e))
                continue
            if pos[0] >= len(toks):
                raise ParseError("unexpected EOF after %s" % key)
            vtok, vs, ve = toks[pos[0]]
            if vtok == "{":
                pos[0] += 1
                sub, close_pos = parse_block(True)
                pos[0] += 1  # consume '}'
                items.append(Node(key, op, sub, kstart, close_pos + 1, ve, close_pos))
            else:
                pos[0] += 1
                items.append(Node(key, op, vtok.strip('"') if vtok.startswith('"') else vtok, kstart, ve, vs, ve))
        if closing:
            raise ParseError("missing closing brace")
        return items, len(text)

    items, _ = parse_block(False)
    return items


def get(nodes, key, default=None):
    for n in nodes:
        if n.key == key:
            return n
    return default


def get_all(nodes, key):
    return [n for n in nodes if n.key == key]


def val(nodes, key, default=None):
    n = get(nodes, key)
    if n is None or n.is_block():
        return default
    return n.value


def raw_inner(text, node):
    """Raw text between the braces of a block node."""
    return text[node.vstart:node.vend]
