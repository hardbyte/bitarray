import re
from distutils.core import setup, Extension


kwds = {}
try:
    kwds['long_description'] = open('README.md').read()
except IOError:
    pass

# Read version from bitarray/_bitarray.c
pat = re.compile(r'#define\s+BITARRAY_VERSION\s+"(\S+)"', re.M)
data = open('bitarray/_bitarray.c').read()
kwds['version'] = pat.search(data).group(1)


setup(
    name = "bitarray-hardbyte",
    author = "Ilan Schnell",
    author_email = "ilanschnell@gmail.com",
    url = "https://github.com/ilanschnell/bitarray",
    license = "PSF",
    classifiers = [
        "License :: OSI Approved :: Python Software Foundation License",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: C",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Utilities",
    ],
    description = "efficient arrays of booleans -- C extension",
    packages = ["bitarray"],
    ext_modules = [Extension(name = "bitarray._bitarray",
                             sources = ["bitarray/_bitarray.c"]),
                   Extension(name = "bitarray._util",
                             sources = ["bitarray/_util.c"])],
    include_package_data = True,
    **kwds
)
