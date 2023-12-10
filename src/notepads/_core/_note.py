class NotepadsNoteHandler(object):
    def __init__(self):
        self.notes = []
        self.all = {}

notepad: NotepadsNoteHandler = NotepadsNoteHandler()

class NotepadsNote(object):
    def __init__(self, name, content, *, author=None, **kwargs):
        self.name: str = name
        self.author: str = author
        self.content: str = content
        
        notepad.notes.append(self)
        notepad.all[self.name] = self

        for key, value in kwargs.items():
            try: setattr(self, key, value)
            except: pass

    def __repr__(self):
        return f'Note(author={self.author}, name={self.name}, content={self.content})'

    def __str__(self):
        return self.__repr__()

    def update(self, *, name=None, author=None, content=None, **kwargs):
        if name:
            self.name = name
        if author:
            self.author = author
        if content:
            self.content = content
        for key, value in kwargs.items():
            try: setattr(self, key, value)
            except: pass

    def read(self):
        return self.content

    def write(self, content):
        self.content = content
        return self

    def wipe(self):
        self.content = ''
        return self

    def delete(self):
        try:
            notepad.notes.remove(self)
            del notepad.all[self.name]
            return self
        except:
            return 'Unknown Note'
