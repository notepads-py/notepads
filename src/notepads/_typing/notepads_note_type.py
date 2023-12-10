class Note(object):
    def __repr__():
        return 'notepads.Note[object]'

    def __class_getitem__(self, item, *args, **kwargs):
        return item

class NoteName(object):
    def __repr__():
        return 'notepads.NoteName[object]'

    def __class_getitem__(self, item, *args, **kwargs):
        return item

class NoteContent(object):
    def __repr__():
        return 'notepads.NoteContent[object]'

    def __class_getitem__(self, item, *args, **kwargs):
        return item

class NoteAuthor(object):
    def __repr__():
        return 'notepads.NoteAuthor[object]'

    def __class_getitem__(self, item, *args, **kwargs):
        return item
