from setuptools import setup, find_packages

setup(
    name='smart-resume-skill-gap-analyzer',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # List your project's dependencies here
        # 'numpy',
        # 'pandas',
    ],
    entry_points={
        'console_scripts': [
            'skill-gap-analyzer=your_module.main:main_function',
        ],
    },
    author='Shivani Singh Rajawat',
    author_email='your_email@example.com',
    description='A package for analyzing skill gaps in resumes',
    url='https://github.com/ShivaniSinghRajawat/smart-resume-skill-gap-analyzer',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)