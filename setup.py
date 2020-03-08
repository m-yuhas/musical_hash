"""Setup script for the musical_hash package."""


from os import path
from setuptools import setup


LONG_DESCRIPTION = ''
with open(
        path.join(
            path.abspath(
                path.dirname(__file__)), 'README.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()


setup(
    name='musical_hash',
    version='0.1.3',
    author='m-yuhas',
    author_email='m-yuhas@qq.com',
    maintainer='m-yuhas',
    url='https://github.com/m-yuhas/musical_hash',
    description='like random-art, but with music',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    license='MIT',
    classifiers=[
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'Operating System :: Microsoft :: Windows :: Windows 7',
        'Operating System :: Microsoft :: Windows :: Windows 8',
        'Operating System :: Microsoft :: Windows :: Windows 8.1',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Artistic Software',
        'Topic :: Multimedia',
        'Topic :: Multimedia :: Sound/Audio',
        'Topic :: Multimedia :: Sound/Audio :: Sound Synthesis'],
    packages=['musical_hash'],
    include_package_data=False,
    install_requires=['numpy', 'wavio'])
