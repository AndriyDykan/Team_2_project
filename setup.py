from setuptools import setup, find_namespace_packages

setup(name='bot', 
      version='0.0.5',
      description='bot',
      url='https://github.com/melser68/materials_for_project',
      author='melser68',
      author_email='msprivate68@gmail.com',
      license='MIT',
      packages=find_namespace_packages(),
      install_requires=['py7zr'],
      entry_points={'console_scripts': [
          'bot = bot_folder.bot:main']}
      )
