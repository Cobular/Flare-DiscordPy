from setuptools import setup
from __about__ import __version__


with open("README.md") as rdme:
    long_description = rdme.read()

setup(
    name="flare-discord.py",
    version=__version__,
    description="Provides a simple, single import cog to add a checkable page to your bot for uptime status monitoring",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://github.com/JakeCover/Flare",
    author="Cobular",
    author_email="python@cobular.com",
    license="MIT",
    packages=["flare"],
    install_requires=["discord.py>=1.5.0,<1.7.0"],
    zip_safe=False,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: System :: Monitoring',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
    keywords=[
        "Discord",
        "Discord.py",
        "Uptime",
        "Monitoring",
        "Flare",
        "Discord Uptime Monitoring",
        "UptimeRobot"
    ],
)