from setuptools import setup, find_packages


with open('README.rst') as _readme_file:
    readme = _readme_file.read()


setup(
    name='timecube',
    url='https://github.com/bwhmather/python-timecube',
    version='0.1.0',
    author='Ben Mather',
    author_email='bwhmather@bwhmather.com',
    maintainer='',
    license='MIT License',
    description=(
        "A library for generating plausible prose"
    ),
    long_description=readme,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=[
    ],
    tests_require=[
    ],
    packages=find_packages(),
    package_data={
        '': ['*.pyi'],
    },
    entry_points={
        'console_scripts': [
        ],
    },
    test_suite='timecube.tests.suite',
)
