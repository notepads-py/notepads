import notepads

notepads.Source \
    .src='''  (Demo) Using notepads V5.7.5  '''


# Creating a file `test.txt`.

notepads.file \
    (name="test.txt")

print(notepads.src)

'''
Output:

Directory["/notepads/"]
  🗎  test.txt
'''

#Creating a folder `examples`.

notepads.folder \
    (name="examples")

print(notepads.src)

'''
Output:

Directory["/notepads/"]
  🗀  examples
  🗎  test.txt
'''

# Move `test.txt` to `examples`.

notepads.get('test.txt').move('examples')

print(notepads.src)

'''
Output:

Directory["/notepads/"]
  🗀  examples
   ↳ 🗎  test.txt
'''

# Create a file `main.py`.

notepads.file \
    (name="main.py")

print(notepads.src)

'''
Output:

Directory["/notepads/"]
  🗀  examples
   ↳ 🗎  test.txt
  🗎  main.py
'''

# Write simple program to file `main.py`

main_py = notepads.get('main.py')

main_py.write \
('''
print("Hello World!")

for i in range(10):
    print(i)
''')

print(main_py.read())

'''
Output:

print("Hello World!")

for i in range(10):
    print(i)
'''
