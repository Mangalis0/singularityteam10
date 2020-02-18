from setuptools import setup, find_packages

setup(
    name='powermetrics',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description="Processes and Analyses Eskom's Numeric and Text Data",
    long_description=open('README.md').read(),
    install_requires=['numpy', 'pandas'],
    url='https://github.com/Mangalis0/singularityteam10.git',
    author='Mangaliso Makhoba, Zanele Gwamanda, Nkululeko Mthembu, Letlhogile Mothoagae, Bryan Green',
    author_email='makhoba808@gmail.com, zanelegwamanda99@gmail.com, nsm.branding@gmail.com, lot.mothoagae@gmail.com, bryangreen290@gmail.com'
)
