from pathlib import Path

if __name__ == "__main__":
    
    data_directory = "./05/exercise/data"
    data_directory_path = Path(data_directory).resolve()
    print(data_directory_path)

    dir_list = list(data_directory_path.glob("*"))
    for dir in dir_list:
        print(dir)

    file_list = []
    for dir in dir_list:
        file_path_list = list(dir.glob("*"))
        file_list += file_path_list
    print(len(file_list))