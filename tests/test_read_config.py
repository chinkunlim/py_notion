from src.config import config

def test_read_config():
    print("Read 'Logging' ")
    print(f"log_folder   : {config.get_config("log_folder", section="Logging", default="")}")
    print(f"log_filename : {config.get_config("log_filename", section="Logging", default="")}")
    print(f"log_level.   : {config.get_config("log_level", section="Logging", default="")}")
    print(f"log_format   : {config.get_config("log_format", section="Logging", default="")}")
    print(f"log_encoding : {config.get_config("log_encoding", section="Logging", default="")}")

if __name__ == "__main__":
    test_read_config()