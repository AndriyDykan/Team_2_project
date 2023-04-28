from setuptools import setup, find_namespace_packages

setup(name='bot', 
      version='0.0.8',
      description='bot',
      url='https://github.com/melser68/materials_for_project',
      author='melser68',
      author_email='msprivate68@gmail.com',
      license='MIT',
      packages=find_namespace_packages(),
      entry_points={'console_scripts': [
          'bot = bot_folder.bot:main']}
      )
