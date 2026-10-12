"""Генерирует простые PNG-иконки (синий круг) без внешних зависимостей."""
import struct, zlib, os

def png(size):
    rows = []
    c = (size - 1) / 2
    for y in range(size):
        row = bytearray([0])
        for x in range(size):
            inside = (x - c) ** 2 + (y - c) ** 2 <= (size / 2 - 1) ** 2
            row += bytes((10, 132, 255, 255)) if inside else bytes((0, 0, 0, 0))
        rows.append(bytes(row))
    raw = b''.join(rows)
    def chunk(t, d):
        return struct.pack('>I', len(d)) + t + d + struct.pack('>I', zlib.crc32(t + d) & 0xffffffff)
    return (b'\x89PNG\r\n\x1a\n' + chunk(b'IHDR', struct.pack('>IIBBBBB', size, size, 8, 6, 0, 0, 0))
            + chunk(b'IDAT', zlib.compress(raw)) + chunk(b'IEND', b''))

out = os.path.join(os.path.dirname(__file__), '..', 'docs')
for s in (32, 64):
    with open(os.path.join(out, f'icon-{s}.png'), 'wb') as f:
        f.write(png(s))
