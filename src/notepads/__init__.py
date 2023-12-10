'''
```
notepads: V5.7.3
```

## Installing
```shell
# Linux/macOS
python3 pip install -U notepads

# Windows
py -3 -m pip install -U notepads
```

### Supports TypeHints

Create runtime only directory
    [1] -> Make folders
    [2] -> Make files
    [3] -> Make notes for code

========================================

```python
# View Directory:

notepads.directory
notepads.dir
notepads.source
notepads.src
```

# Directory Example Layout:
```ruby
Directory["/notepads/"]
  🗀  examples
   ↳ 🗎  example.py
  🗎  main.py
```

========================================


# Usage  <h6>100ms | (Average)</h6>
```python
import notepads

notepads.note \
    (name="introduction",

    content="""Create runtime only directory 
    [1] -> Make folders 
    [2] -> Make files 
    [3] -> Make notes for code""",

    author = "'notepads.py' Team")

print(notepads.get_note('introduction').content)

"""
Lets create a file `nps.txt` and a folder `examples` in the directory.
"""

notepads.folder \
    (name="examples",
    description="Examples of using notepads.",
    version="0.1.0",
    author="'notepads.py' Team",
    some_random_kwarg='hi there!')

#   folder.some_random_kwarg
#   >>> hi there!

"""
Any other kwarg you pass in will be saved as a variable for you to access later.
"""

notepads.file \
    (name="nps.txt",
    description="This is a file.",
    version="0.1.0",
    author="'notepads.py' Team")

print(notepads.directory) # notepads.dir | notepads.source | notepads.src

"""
Output:

Directory["/notepads/"]
  🗀  examples
  🗎  nps.txt
"""

"""
Lets add a file `test.py` to the `examples` folder.
"""

notepads.file \
    (name="test.py",
    parent='examples')

print(notepads.directory) # notepads.dir | notepads.source | notepads.src

"""
Output:

Directory["/notepads/"]
  🗀  examples
   ↳ 🗎  test.py
  🗎  nps.txt
"""

"""
Now lets write to some files!
"""

nps_file = notepads.get('nps.txt')
test_file = notepads.get('examples').get('test.py')

nps_file.write("Hello, World!")
test_file.write("print('Hello, World!')")

print(nps_file.read())
print(test_file.read())

"""
nps.txt:

Hello, World!

test.py:
print('Hello, World!')
"""

nps_file.wipe()

print(nps_file.read())

"""
Output:


"""
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

    if not parent: directory.files.append((file.name, file))
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
__version__ = '5.7.3'
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
