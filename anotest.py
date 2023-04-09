import glob


class Annotest:

    ANOT_LABELS = ["aa", "ee", "uu", "oo", "bb", "ii", "xx"]
    ALL_FILES = []

    def __init__(self, dataset_path: str) -> None:
        ALL_FILES = glob.glob(f"{dataset_path}/*/pnoistor_*")

        print(ALL_FILES)
