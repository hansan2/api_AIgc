import yaml


class Handler_YAML(object):

    def __init__(self) -> None:
        pass

    def read_yaml(self, file_path: str):
        with open(file_path, "r", encoding="utf-8") as f:
            return yaml.load(f)


if __name__ == '__main__':
    yaml1 = Handler_YAML()
    print(yaml1.read_yaml(r"../test_data/aigc_test_zh_cn.yaml"))
