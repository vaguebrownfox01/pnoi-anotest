import os
import glob
import json
import pandas as pd

mkdir = lambda p: 0 if os.path.exists(p) else (os.mkdir(p), 1)[1]

# DATA Path
DATA_PATH = "DATA"

GLOB_PATH = f"{DATA_PATH}/pnoistor_*/*/*"

REPORT_PATH = "./report"; mkdir(REPORT_PATH)

FILE_PARTS = ["app-version-code", "subject-ID", "file-class", "file-ID", "file-comment", "file-format", "file-name", "file-path"]
SEP="-"; META_SEP="_"; COL_SEP = "--"
#-----------------------------------------------------------------------------------#

# GET All files from data dump

def process_file_info(file_path: str) -> dict:

    file_name: str = os.path.basename(file_path)
    file_name_parts = file_name.replace(".", SEP).split(sep=SEP)
    file_name_parts += [file_name, file_path]

    file_info_dict = { p:file_name_parts[i] for i, p in enumerate(FILE_PARTS) }

    return file_info_dict

# Export All file info CSV
ALL_FILE_INFO_EXPORT_PATH = "all_data_files.csv"
all_data_files: list = glob.glob(GLOB_PATH)
all_data_files_DF = pd.DataFrame([process_file_info(f) for f in all_data_files])
all_data_files_DF.to_csv(f"{REPORT_PATH}/{ALL_FILE_INFO_EXPORT_PATH}", index=False) 


#-----------------------------------------------------------------------------------#

all_data_files_DF = pd.read_csv(f"{REPORT_PATH}/{ALL_FILE_INFO_EXPORT_PATH}")
all_subjects = pd.unique(all_data_files_DF[FILE_PARTS[1]])
FILE_TYPES = pd.unique(all_data_files_DF.loc[:, FILE_PARTS[2]])
DATASET_COLUMNS = set([fp.replace("file", f"{ft}{COL_SEP}file") for fp in FILE_PARTS for ft in FILE_TYPES])

