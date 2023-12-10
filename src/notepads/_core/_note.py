class NotepadsNoteHandler(object):
    def __init__(self):
        self.notes = []
        self.all = {}

notepad: NotepadsNoteHandler = NotepadsNoteHandler()

class NotepadsNote(object):
    def __init__(self, name, content, *, author=None):
        self.name: str = name
        self.author: str = author
        self.content: str = content
        
        notepad.notes.append(self)
        notepad.all[self.name] = self

    def __repr__(self):
        return f'Note(author={self.author}, name={self.name}, content={self.content})'

    def __str__(self):
        return self.__repr__()

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
