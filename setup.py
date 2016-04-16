from setuptools import setup

setup(name = "Collatz Sequence Toolkit",
      version = "1.0",
      description = "Mathematical tool for playing with the Collatz conjecture.",
      author = "Troy P. Kling",
      author_email = "troykling1308@gmail.com",
      url = "https://gitlab.com/CoronalRain/Collatz",
	  py_modules = ["collatz"],
	  install_requires=[
		"csv",
		"time",
		"docopt"
	  ],
     )