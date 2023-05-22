from setuptools import setup, find_packages

setup(
    name='process_monitoring_package',
    version='0.0.1',
    description='A package to monitor a process and send email notifications',
    packages=find_packages(),
    author="Chengran",
    license="MIT",
    install_requires=[
        'psutil',
        'requests',
        'tqdm'
    ],
)