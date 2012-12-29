

import logbot
import blocks
import config
import fops
import utils
from axisbox import AABB


log = logbot.getlogger("GRIDSPACE")


class NodeState(object):
    NO = 1
    FREE = 2
    YES = 3


def neighbours_of(grid, coords):
    x = coords.x
    y = coords.y
    z = coords.z
    for i, j in utils.adjacency:
        state = compute_state(grid, x + i, y, z + j)
        if state == NodeState.YES:
            yield x + i, y, z + j
        elif state == NodeState.NO:
            state = compute_state(grid, x + i, y + 1, z + j)
            if state == NodeState.YES:
                yield x + i, y + 1, z + j
        elif state == NodeState.FREE:
            for k in [-1, -2, -3]:
                state = compute_state(grid, x + i, y + k, z + j)
                if state == NodeState.YES:
                    yield x + i, y + k, z + j
                    break
                elif state == NodeState.NO:
                    break
    state = compute_state(grid, x, y + 1, z)
    if state == NodeState.YES:
        yield x, y + 1, z
    state = compute_state(grid, x, y - 1, z)
    if state == NodeState.YES:
        yield x, y - 1, z


def compute_state(grid, x, y, z):
    block_1 = grid.get_block(x, y, z)
    if block_1.is_cube:
        return NodeState.NO
    block_2 = grid.get_block(x, y + 1, z)
    if block_2.is_cube:
        return NodeState.NO
    block_0 = grid.get_block(x, y - 1, z)
    if block_0.is_cube:
        if block_1.is_free and block_2.is_free:
            return NodeState.YES
    if block_0.is_free and block_1.is_free and block_2.is_free:
        return NodeState.FREE
    return GridState(grid, block_0, block_1, block_2).state


def can_go(grid, from_coords, to_coords):
    return True


def can_stand(grid, x, y, z):
    return compute_state(grid, x, y, z) == NodeState.YES


class GridState(object):

    def __init__(self, grid, block_0, block_1, block_2):
        self.grid = grid
        self.under = block_0
        self.block = block_1
        self.over = block_2
        self.state = self.compute_state()

    def compute_state(self):
        if not over.is_fall_through:
            return NO
        if block.can_stand_in:
            if block.is_stairs:
                pass
            elif under.is_fence and block.fence_overlap:
                if over2.is_fall_through or over2.min_y > block.y + 0.5 + PLAYER_HEIGHT:
                    return YES
                else:
                    return NO
            elif block.stand_in_over2:
                if over2.is_fall_through or over2.min_y > block.max_y + PLAYER_HEIGHT:
                    return YES
                else:
                    return NO
            else:
                return YES
        elif under.can_stand_on:
            if under.is_fall_through and block.is_fall_through:
                return FREE
            else:
                return YES
        elif block.is_fall_through:
            return FREE
        else:
            return NO
