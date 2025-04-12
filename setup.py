
from setuptools import setup

setup(
    name='twentykn',
    version='1.0.0',
    description='20KN: Twenty Kilo Numeric System (CJK-based 20,000-radix encoding)',
    author='blueradiance',
    author_email='noreply@example.com',
    py_modules=['twentykn'],
    license='Other/Proprietary License',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: Other/Proprietary License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
