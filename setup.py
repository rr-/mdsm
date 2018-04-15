from setuptools import setup, find_packages

setup(
    author='Marcin Kurczewski',
    author_email='rr-@sakuya.pl',
    name='mdsm',
    long_description='Send e-mails directly into local maildir',
    version='0.1',
    url='https://github.com/rr-/mdsm',
    packages=find_packages(),

    entry_points={
        'console_scripts': [
            'mdsm = mdsm.__main__:main'
        ]
    },

    install_requires=[
        'xdg',
        'configargparse',
    ],

    classifiers=[
        'Environment :: Console',
        'Development Status :: 4 - Beta',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Communications :: Email :: Email Clients (MUA)',
    ]
)
