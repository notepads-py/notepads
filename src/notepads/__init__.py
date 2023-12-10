'''
```
notepads: V5.7.1
```

## Installing
```shell
# Linux/macOS
python3 pip install -U notepads

# Windows
py -3 -m pip install -U notepads
```

Create runtime only directory
    [1] -> Make folders
    [2] -> Make files
    [3] -> Make notes for code

========================================

# Directory Example Layout:
```ruby
Directory["/notepads/"]
  🗀  examples
   ↳ 🗎  example.py
  🗎  main.py
```

========================================

# Create note:
```python
notepads.note(name='notename', content='notecontent', author='OPTIONAL_noteauthor')
```
# Find note
```python
notepads.get_note(name='notename')

# or

notepads.notes()[<index>]
```
========================================

# Create folder:
```python
notepads.folder(name='foldername', version='OPTIONAL_0.0.0', description='OPTIONAL_a test folder', author='OPTIONAL_test author'))

# name, *, version=None, description=None, author=None
```

# Find folder:
```python
notepads.get(name='foldername')
```

# Update folder:
```python
folder.update(name='newfoldername', version='0.0.1', description='a new test folder', author='test author')
```

# Delete folder:
```python
folder.delete()
```

========================================

# Create file:
```python
notepads.file(name='filename', description='OPTIONAL_a test file', author='OPTIONAL_test author', parent='OPTIONAL_folder name')

# name, *, version=None, description=None, author=None, parent: NotepadsFolder=None
```

# Find file:
```python
notepads.get(name='filename')
```

# Update file:
```python
file.update(name='newfilename', description='a new test file', author='test author)
```

# Load file:
```python
file.load()
```

# Write file:
```python
file.write(content='newfilecontent')
```

# Delete file:
```python
file.delete()
```
'''

from .typing import *

from .utils import (
    pickle,
    dump,
    load,
    read,
    write,
    lines,
    words,
    chars,
    ints,
    floats,
    join,
    split,
    replace,
    strip,
    lstrip,
    rstrip,
    capitalize,
    lower,
    upper,
    title,
    swapcase,
    islower,
    isupper,    
    isdigit,
    isnumeric,
    isdecimal,
    isalpha,
    isalnum,
    isidentifier,
    isspace,
    isprintable,
    isascii,
    istitle,
)

from ._core._directory import NotepadsDirectory
from ._core._file import NotepadsFile
from ._core._folder import NotepadsFolder
from ._core._note import NotepadsNote, notepad

directory: NotepadsDirectory = NotepadsDirectory()
dir: NotepadsDirectory = directory
source: NotepadsDirectory = directory
src: NotepadsDirectory = directory

def note(name, content, *, author=None):
    return NotepadsNote(name, content, author=author)

def notes():
    return notepad.notes

def get_note(name):
    return notepad.all.get(name)

def files():
    return directory.files

def folders():
    return directory.folders

def all():
    return directory.all

def file(name, *, version=None, description=None, author=None, parent: NotepadsFolder=None):
    if parent:
        if len(directory.folders) > 0:
            if parent not in [folder[0] for folder in directory.folders]:
                parent: NotepadsFolder = folder(name=parent, version=None, description=None, author=None)
                parent.directory = directory
                directory.folders.append((parent.name, parent))
                directory.all[parent.name] = parent
            else:
                parent = directory.all[parent]
            
    file: NotepadsFile = NotepadsFile(name, version=version, description=description, author=author, parent=parent)
    file.directory = directory
    
    directory.files.append((file.name, file))
    if parent:
        directory.all[parent.name].files[file.name] = file
    else:
        directory.all[file.name] = file
    return file

def folder(name, *, version=None, description=None, author=None):
    folder: NotepadsFolder = NotepadsFolder(name, version=version, description=description, author=author)
    folder.directory = directory
    directory.folders.append((folder.name, folder))
    directory.all[folder.name] = folder
    return folder

def get(name):
    return directory.all[name]

__all__ = [
    'directory',
    'dir',
    'source',
    'src',
    'note',
    'notes',
    'get_note',
    'files',
    'folders',
    'all',
    'file',
    'folder',
    'get',
    'Directory',
    'Dir',
    'Source',
    'Src',
    'File',
    'FileAuthor',
    'FileVersion',
    'FileDesc',
    'FileParent',
    'FileContent',
    'Folder',
    'FolderAuthor',
    'FolderVersion',
    'FolderDesc',
    'FolderFile',
    'Note',
    'NoteName',
    'NoteContent',
    'NoteAuthor',
    'Any',
    'Callable',
    'Dict',
    'List',
    'Optional',
    'Tuple',
    'Union',
    'pickle',
    'dump',
    'load',
    'read',
    'write',
    'lines',
    'words',
    'chars',
    'ints',
    'floats',
    'join',
    'split',
    'replace',
    'strip',
    'lstrip',
    'rstrip',
    'capitalize',
    'lower',
    'upper',
    'title',
    'swapcase',
    'islower',
    'isupper',
    'isdigit',
    'isnumeric',
    'isdecimal',
    'isalpha',
    'isalnum',
    'isidentifier',
    'isspace',
    'isprintable',
    'isascii',
    'istitle',
]
__version__ = '5.7.1'
__author__ = 'notepads'
__license__ = 'MIT'
__copyright__ = 'Copyright (c) 2023 notepads'
__credits__ = ['notepads']
__maintainer__ = 'notepads'
__email__ = 'notepads.py@gmail.com'
__status__ = 'Development Status :: 5 - Production/Stable'
__python_version__ = '3.7'
__name__ = 'notepads'
__description__ = 'Create runtime folders, files, and code notes. All stored in notepads environment.'
__desc__ = __description__
__github__ = 'https://github.com/py-notepads'
__repo__ = 'https://github.com/py-notepads/notepads'
__url__ = __github__
