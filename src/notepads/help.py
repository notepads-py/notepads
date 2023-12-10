print('''
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
```''')
