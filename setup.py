from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()


"""
cheat sheet reminder for myself because I'm dumb

python setup.py sdist bdist_wheel
python -m twine upload dist/*
"""


setup(name='maragi-camera',
      version='0.1.0',
      description='Microservices Architecture for Robotics and Artificial General Intelligence',
      url='https://maragi.io',
      long_description=long_description,
      long_description_content_type="text/markdown",
      author='David Shapiro',
      author_email='daveshap37@gmail.com',
      install_requires=['opencv-python',],
      license='MIT',
      packages=['maragi-camera'],
      zip_safe=False)
