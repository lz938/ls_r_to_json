import sys

class LsRtoJson:
    def __init__(self):
        print("lsRtoJson::__init__")
        self.folder_dict = {}


    @staticmethod
    def read_file(file_path):
        data = [line.strip() for line in open(file_path, 'r')]
        return data

    def process_folder(self, line):
        folders = line.split('/')
        iter_folder = iter(folders)

        starting_folder = next(iter_folder)
        if len(starting_folder) > 0:
            print(f"Path {line} does not start from root", file=sys.stderr)
            return

        root_folder = next(iter_folder)
        if root_folder not in self.folder_dict:
            self.folder_dict[root_folder] = []

        cur_folder = self.folder_dict[root_folder]      # Used to iterate

        for folder in iter_folder:
            folder_dict = {folder: []}
            if folder_dict not in cur_folder:
                cur_folder.append(folder_dict)
            # endif
            cur_folder = folder_dict

        return cur_folder

    def process_file(self, line):
        return

    def create_json(self, lines, skip_lines=0):
        iterlines = iter(lines)
        for i in range(skip_lines):
            next(iterlines)

        for line in iterlines:
            if line.endswith(':'):      # This is a folder
                self.process_folder(line)
            else:
                self.process_file(line)