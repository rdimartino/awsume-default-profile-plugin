from setuptools import setup

setup(
    name="awsume-default-profile-plugin",
    version="0.0.1",
    entry_points={"awsume": ["default_profile = default_profile"]},
    author="Robert DiMartino",
    author_email="robert@dimartino.dev",
    py_modules=["default_profile"],
)
