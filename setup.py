import setuptools

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

with open('README.md') as fh:
    long_description = fh.read()

setuptools.setup(
    name="pollination-handlers",
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    author="Pollination",
    author_email="info@ladybug.tools",
    description="Handlers to process Pollination recipes inputs and outputs.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pollination/handlers-python",
    packages=setuptools.find_packages(exclude=["tests"]),
    include_package_data=True,
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent"
    ],
    license="AGPL-3.0"
)
