class NotepadsFolder(object):
    def __init__(self, name, *, version=None, description=None, author=None, **kwargs):
        self.name: str = name
        self.version: str = version
        self.description: str = description
        self.author: str = author
        self.files: dict = {}
        self.directory: object = None
        self.path = f'/notepads/{self.name}/'

        for key, value in kwargs.items():
            try: setattr(self, key, value)
            except: pass

    def __repr__(self):
        return f'Folder["{self.path}"](name={self.name}, version={self.version}, description={self.description}, author={self.author}, len_files={len(self.files)})'

    def __str__(self):
        return self.__repr__()

    def get(self, name):
        try:
            for child in self.files:
                if child == name:
                    return self.files.get(child)

            return 'Unknown File'
        except:
            pass

    def delete(self):
        for folder in self.directory.folders:
            if folder[0] == self.name:
                folder_index: int = self.directory.folders.index(folder)
                del self.directory.folders[folder_index]
                break

        try:
            del self.directory.all[self.name]

        except: pass

    def update(self, *, name=None, version=None, description=None, author=None, **kwargs):
        if name:
            self.name = name
        if version:
            self.version = version
        if description:
            self.description = description
        if author:
            self.author = author

        for key, value in kwargs.items():
            try: setattr(self, key, value)
            except: pass

    def update_file(self, name, *, version=None, description=None, author=None, **kwargs):
        try:
            for child in self.files:
                if child == name:
                    self.files[child].update(name=name, version=version, description=description, author=author, **kwargs)
                    return child

        except:
            pass

    def read_file(self, name):
        try:
            for child in self.files:
                if child == name:
                    return self.files[child].read()

            return 'Unknown File'
        except:
            pass

    def write_file(self, name, content):
        try:
            for child in self.files:
                if child == name:
                    self.files[child].write(content)
                    return self.files[child]

            return 'Unknown File'
        except:
            pass

    def wipe_file(self, name):
        try:
            for child in self.files:
                if child == name:
                    self.files[child].write('')
                    return child[1]

            return 'Unknown File'
        except:
            pass

    def delete_file(self, name):
        try:
            for child in self.files:
                if child[0] == name:
                    self.files[child][1].delete()
                    return self

            return 'Unknown File'
        except:
            pass
