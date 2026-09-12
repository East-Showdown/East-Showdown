"""Read/write typed Clausewitz binary trees, preserving property order."""
from pathlib import Path
import struct


class Node:
    def __init__(self, name, **properties):
        self.name, self.props, self.children = name, properties, []

    def add(self, name, **properties):
        child = Node(name, **properties)
        self.children.append(child)
        return child

    def child(self, name):
        return next(c for c in self.children if c.name == name)

    def get(self, name):
        return self.props[name][1]


def encode(node, depth=0):
    data = bytearray(b'@@b@' if depth == 0 else b'['*depth + node.name.encode('latin1') + b'\0')
    for key, (kind, values) in node.props.items():
        data += b'!' + bytes([len(key)]) + key.encode('latin1')
        data += kind.encode() + struct.pack('<i', len(values))
        if kind == 's':
            assert len(values) == 1
            text = values[0].encode('latin1') + b'\0'
            data += struct.pack('<i', len(text)) + text
        else:
            data += struct.pack('<' + kind*len(values), *values)
    for child in node.children:
        data += encode(child, depth+1)
    return bytes(data)


def read(path):
    data = Path(path).read_bytes()
    assert data[:4] == b'@@b@'
    root = Node('File')
    stack, pos = [root], 4
    while pos < len(data):
        if data[pos] == 91:
            start = pos
            while data[pos] == 91:
                pos += 1
            depth = pos-start
            end = data.index(0, pos)
            stack = stack[:depth]
            stack.append(stack[-1].add(data[pos:end].decode('latin1')))
            pos = end+1
        elif data[pos] == 33:
            size = data[pos+1]
            key = data[pos+2:pos+2+size].decode('latin1')
            pos += 2+size
            kind, count = chr(data[pos]), struct.unpack_from('<i', data, pos+1)[0]
            pos += 5
            if kind == 's':
                assert count == 1
                size = struct.unpack_from('<i', data, pos)[0]
                pos += 4
                values = [data[pos:pos+size].rstrip(b'\0').decode('latin1')]
                pos += size
            else:
                assert kind in ('f', 'i')
                values = list(struct.unpack_from('<'+kind*count, data, pos))
                pos += 4*count
            stack[-1].props[key] = (kind, values)
        else:
            raise ValueError(f'Unexpected token at byte {pos}')
    return root
