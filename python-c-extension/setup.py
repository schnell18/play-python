from setuptools import setup
from setuptools import Extension

module = Extension('cputs', sources=['src/fputs.c'])
setup(name='cputs', ext_modules=[module])

# from distutils.core import setup
# from distutils.core import Extension
#
#
# def main():
#     setup(
#         name="fputs",
#         # version="1.0.0",
#         description="Python interface for the fputs C library function",
#         author="Justin Zhang",
#         author_email="schnell18@gmail.com",
#         ext_modules=[Extension("fputs", ["src/fputs.c"])],
#     )
#
#
# if __name__ == "__main__":
#     main()
