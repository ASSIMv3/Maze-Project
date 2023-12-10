from settings import *

text_map = [
    '21111111111111111111',
    '2......111..1...1..1',
    '2..111....2....2...1',
    '2....1..222.11.....1',
    '2..1....1......1...1',
    '22.1...111..1.2....1',
    '2....2.....2..2....1',
    '22222222222222222222'
]

world_map = {}
mini_map = set()
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char != '.':
            mini_map.add((i * MAP_TILE, j * MAP_TILE))
            if char == '1':
                world_map[(i * TILE, j * TILE)] = '1'
            elif char == '2':
                world_map[(i * TILE, j * TILE)] = '2'