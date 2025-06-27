from src.config import config

def test_read_config():
    log_folder = config.get_config("log_folder", section="Logging", default="")
    log_filename = config.get_config("log_filename", section="Logging", default="")
    log_level = config.get_config("log_level", section="Logging", default="")
    log_format = config.get_config("log_format", section="Logging", default="")
    log_encoding = config.get_config("log_encoding", section="Logging", default="")

    print("Read 'Logging'")
    print(log_encoding)
    print(log_filename)
    print(log_folder)
    print(log_format)
    print(log_level)

    """ 
    assert log_folder == "logs"
    assert log_filename == "app.log"
    assert log_level == "DEBUG"
    assert log_format == "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    assert log_encoding == "utf-8"
    """

def main():
    test_read_config()

if __name__ == "__main__":
    main()