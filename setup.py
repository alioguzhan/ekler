from setuptools import setup, find_packages


classifiers = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3',
    'Topic :: Utilities'
]

setup(
    name='ekler',
    version='0.3',
    packages=find_packages(include=['ekler'],
                           exclude=['tests*', '.vscode', 'venv', '__*', ]),
    classifiers=classifiers,
    py_modules=["ekler"],
    python_requires='>=3',
    keywords="turkish, turkce, isim, ekler",
    license='MIT',
    description='Turkce kelimelerin sonuna fonetik yapilarina uygun ekleri ekleyen module.',
    long_description=open('README.md').read(),
    url='https://github.com/alioguzhan/ekler',
    author='Ali Oguzhan Yildiz',
    author_email='aoguzhanyildiz@gmail.com'
)
