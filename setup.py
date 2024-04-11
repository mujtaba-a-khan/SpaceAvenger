from setuptools import setup, find_packages

setup(
    name="space_avenger",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        'pygame',
    ],
    entry_points={
        'console_scripts': [
            'space_avenger=space_avenger.main:main',  # Adjust the path as needed
        ],
    },
    package_data={
        'space_avenger': ['assets/*'],  # Ensure all your game assets are included
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
