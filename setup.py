from setuptools import setup

# OPTIONS = {'iconfile': './u2b.icns'}
OPTIONS = {}
setup(
    app=["kvm.py"],
    setup_requires=["py2app"],
    options={'py2app': OPTIONS}
)