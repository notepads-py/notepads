print('''
```
notepads: V5.7.7
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
```''')
