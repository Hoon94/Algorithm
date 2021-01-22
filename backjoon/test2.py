import logging

if __name__ == '__main__':
    logger = logging.getLogger("main")
    logging.basicConfig(level=logging.DEBUG)
    # logger.setLevel(logging.INFO)

    # steam_handler = logging.FileHandler("my.log", mode = "a", encoding="utf8")
    # logging.addHandler(steam_handler)

    logger.debug("틀렸어")
    logger.info("확인해")
    logger.warning("조심해")
    logger.error("에러났어")
    logger.critical("망했다")
