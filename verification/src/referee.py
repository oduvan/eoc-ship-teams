from checkio_referee import RefereeRank, ENV_NAME



import settings_env
from tests import TESTS


class Referee(RefereeRank):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "two_teams"
    FUNCTION_NAMES = {
        "python_3": "two_teams",
        "js_node": "twoTeams"
    }
    ENV_COVERCODE = {
        
    }