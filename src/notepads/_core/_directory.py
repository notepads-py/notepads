class NotepadsDirectory(object):
    def __init__(self):
        self.folders: list = []
        self.files: list = []
        self.all: dict = {}
        self.path = '/notepads/'

    def get(self, name):
        return self.all.get(name)

    def delete(self, name):
        if name in self.folders:
            self.folders.remove(name)

        elif name in self.files:
            self.files.remove(name)

        if name in self.all:
            del self.all[name]

        return self
    
    def __repr__(self):
        folder_icon = '🗀'
        file_icon = '🗎'
        directory_layout = f'Directory["{self.path}"]\n'

        sorted_folders = sorted(self.folders, key=lambda x: x[0])
        sorted_files = []
        for folder in sorted_folders:
            directory_layout += f'  {folder_icon}  {folder[0]}\n'
            sorted_files = sorted(folder[1].files, key=lambda x: x[0])
            directory_layout += ''.join([f'   ↳ {file_icon}  {file}\n' for file in sorted_files])

        sorted_dir_files = sorted(self.files, key=lambda x: x[0])
        directory_layout += ''.join([f'  {file_icon}  {file[0]}\n' for file in sorted_dir_files if file[0] not in sorted_files])

        return directory_layout

    def __str__(self):
        return self.__repr__()

    def __int__(self):
        return len(self.all)

    def __len__(self):
        return self.__int__()

    def __contains__(self, name):
        return name in self.all

    def __getitem__(self, name):
        return self.all[name]

    def __setitem__(self, name, value):
        self.all[name] = value

    def __delitem__(self, name):
        del self.all[name]

    def __iter__(self):
        return iter(self.all)
