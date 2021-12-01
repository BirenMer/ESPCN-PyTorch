import os

# Prepare dataset
os.system("python ./prepare_dataset.py --inputs_dir ../data/T91/original --output_dir ../data/T91/ESPCN")

# Split train and valid
os.system("python ./split_train_valid_dataset.py --images_dir ../data/T91/ESPCN")

# Create LMDB database file
os.system("python ./create_lmdb_database.py --images_dir ../data/T91/ESPCN/train --lmdb_path ../data/train_lmdb/ESPCN/T91_HR_lmdb --upscale_factor 1")
os.system("python ./create_lmdb_database.py --images_dir ../data/T91/ESPCN/train --lmdb_path ../data/train_lmdb/ESPCN/T91_LRbicx3_lmdb --upscale_factor 3")

os.system("python ./create_lmdb_database.py --images_dir ../data/T91/ESPCN/valid --lmdb_path ../data/valid_lmdb/ESPCN/T91_HR_lmdb --upscale_factor 1")
os.system("python ./create_lmdb_database.py --images_dir ../data/T91/ESPCN/valid --lmdb_path ../data/valid_lmdb/ESPCN/T91_LRbicx3_lmdb --upscale_factor 3")
