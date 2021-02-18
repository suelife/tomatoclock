import setuptools


setuptools.setup(
    name="tomatoclock", # Replace with your own username
    version="0.0.1",
    author="Wind Kuo",
    author_email="suelife@gmail.com",
    description="A small example package",
    # long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/suelife/tomatoclock",
    packages=setuptools.find_packages(),
    classifiers=['Intended Audience :: Science/Research',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: MIT License',
                 "Programming Language :: Python",
                 'Topic :: Software Development',
                 'Topic :: Scientific/Engineering',
                 'Operating System :: Microsoft :: Windows',
                 'Operating System :: POSIX',
                 'Operating System :: Unix',
                 'Operating System :: MacOS'],
    python_requires='>=3.6',
)