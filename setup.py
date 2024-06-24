from setuptools import setup, find_packages

setup(
    name='weather_project',
    version='0.1.0',
    author='Yusk03',
    packages=find_packages(),
    install_requires=[
        'requests',
        'python-dotenv',
    ],
    entry_points={
        'console_scripts': [
            'weather_project=main:main',
        ],
    },
)
