import math
import random
import string

DEBUG = False
USE_ENCRYPTION = False

COMMANDER = "FrederickGeek8"
PREFIX=COMMANDER[:2]

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

# USERNAME = id_generator()
USERNAME = PREFIX+"_bot"+id_generator()
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 25565

PROTOCOL_VERSION = 51  # minecraft version 1.4.1
CONNECTION_MAX_DELAY = 5
CONNECTION_INITIAL_DELAY = 0.1

WORLD_HEIGHT = 256
CHUNK_SIDE_LEN = 16

PLAYER_HEIGHT = 1.8
PLAYER_EYELEVEL = 1.62
PLAYER_BODY_EXTEND = 0.3
PLAYER_BODY_DIAMETER = 0.6

MAX_JUMP_HEIGHT = 1.25
MAX_STEP_HEIGHT = 0.5
MAX_WATER_JUMP_HEIGHT = 0.67
MAX_VINE_JUMP_HEIGHT = 0.35
G = 27.0
# or 0.08 block/tick - drag 0.02 blk/tick (used as final multiply by 0.98)

BLOCK_FALL = 0.08
DRAG = 0.98
SPEED_ON_GROUND = 0.1
SPEED_IN_AIR = 0.02
SPEED_JUMP = 0.42
SPEED_LIQUID_JUMP = 0.03999999910593033
SPEED_CLIMB = 0.2

TIME_STEP = 0.05

COST_JUMP = 1.1
COST_LADDER = 0.21 / \
    0.15  # common speed on ground / max speed on ladder
COST_FALL = 1.1
COST_DIRECT = 1
COST_DIAGONAL = math.sqrt(2) * COST_DIRECT
PATHFIND_LIMIT = 100  # roughly in blocks
HORIZONTAL_MOVE_DISTANCE_LIMIT = 2.83
