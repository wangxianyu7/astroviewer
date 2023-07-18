from setuptools import setup

setup(
    name='astroviewer',
    version='0.1.0',
    py_modules=['astroviewer'],
    install_requires=[
        'numpy',
        'matplotlib',
    ],
    entry_points={
        'console_scripts': [
            'astroviewer=astroviewer:main',
        ],
    },
)
