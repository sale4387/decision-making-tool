
from cli import get_mode, route_mode, default_route
from logger import logger

def main():
    mode = get_mode()

    if mode is not None:
            cli_route=route_mode(mode)
            if not cli_route:
                logger.error("Wrong mode selected")
                exit(1)
    else:
        default_route()
    

if __name__ == "__main__":
     main()








