from setuptools import setup, find_packages
import pathlib

path_absolute: pathlib.Path = pathlib.Path(__file__).parent.absolute()

setup(
    name='notepads',
    version='5.7.7',
    description=' ㅤ ',
    long_description=pathlib.Path(f"{path_absolute}/README.md").read_text(encoding="utf-8"),
    long_description_content_type='text/markdown',
    url='https://github.com/notepads-py',
    author='notepads',
    author_email='notepads.py@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Development Status :: 2 - Pre-Alpha',
        'Development Status :: 3 - Alpha',
        'Development Status :: 4 - Beta',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='notes, notepad, notepads, np, nps',
    project_urls={
        'Source Code': 'https://github.com/notepads-py/notepads',
        'Issues': 'https://github.com/notepads-py/notepads/issues',
        'Download': 'https://pypi.org/project/notepads/',
    },
    include_package_data=True,
    packages=find_packages(exclude=['tests', 'tests.*'])
),
