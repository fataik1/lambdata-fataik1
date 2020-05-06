from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lambdata-fataik1", # the name that you will install via pip
    version="1.1",
    author="Fatai King",
    author_email="kinggy89@gmail.com",
    description="Helper Functions",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/fataik1/lambdata-fataik1",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)
