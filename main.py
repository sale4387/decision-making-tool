
from dotenv import load_dotenv
load_dotenv()
from cli import get_cli_args, route_mode, is_valid_log_level, default_route
import logger, logging
from config import LOG_LEVEL

logger = logging.getLogger(__name__)

def main():

    mode, llevel = get_cli_args()
    

    if llevel and not is_valid_log_level(llevel):
        logger.error(f"Invalid log level: {llevel}, using default")
        level = getattr(logging, LOG_LEVEL)
    elif llevel:
        level = getattr(logging, llevel)
    else:
        level = getattr(logging, LOG_LEVEL)

    logging.getLogger().setLevel(level)



    if mode is not None:
        cli_route=route_mode(mode)
        if not cli_route:
            logger.debug(f"{mode} is not correct mode")
            logger.error(f"Wrong mode was selected: {mode}")
            exit(1)
    else:
        default_route("default")

if __name__ == "__main__":
     print("\n========== TEST START ============")
     main()
     print("\n========== TEST END ============\n")








