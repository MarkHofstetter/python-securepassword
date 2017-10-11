from distutils.core import setup
setup(
    name = "securepassword",
    packages = ["securepassword"],
    version = "1.0.0",
    description = "Create and check passwords using user suppplied/default rules",
    author = "Mark Hofstetter",
    author_email = "mark@hofstetter.at",
    url = "https://github.com/MarkHofstetter/python-securepassword",
    download_url = "https://github.com/MarkHofstetter/python-securepassword.git",
    keywords = ["password", "security", "password rules"],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Security",
        ],
    long_description = """\
This version requires Python 3 or later
"""
)
