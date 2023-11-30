from setuptools import setup


setup(
    name="beancount_format",
    version="0.0.1",
    py_modules=["beancount_format"],
    install_requires=["beancount==2.3.4", "click>=8.0"],
    entry_points={
        "console_scripts": ["beancount_format=beancount_format:main"],
    },
)
