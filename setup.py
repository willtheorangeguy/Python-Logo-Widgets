from setuptools import setup, find_packages

def readme():
    with open('README.md') as f:
        return f.read()

setup(
	name='Python-Logo-Widgets',
	version='2.2.2',
    description='A group of widgets showing the Python logos, that can easily be added to your Python GUI code!',
    long_description=readme(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Widget Sets',
    ],
    keywords='logo powered widgets gui',
    url='https://github.com/willtheorangeguy/Python-Logo-Widgets',
    author='willtheorangeguy',
    packages=find_packages(where="imgs"),
    package_dir={"": "imgs"},
    include_package_data=True,
    py_modules = ['length', 'width', 'logo', 'main'],
    entry_points={
        'console_scripts': [
            'python-logo-widgets=main:main'
        ]
    },
)
