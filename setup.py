from setuptools import setup, find_packages

version = "0.1"

setup(
    name="newzope",
    version=version,
    description="Make it easier to create and run Plone buildouts.",
    long_description="""\
""",
    classifiers=[],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords="",
    author="Alex Clark",
    author_email="aclark@aclark.net",
    url="http://svn.plone.org/svn/collective/newzope/trunk/",
    license="",
    packages=find_packages(exclude=["ez_setup", "examples", "tests"]),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points="""
      # -*- Entry points: -*-
      """,
)
