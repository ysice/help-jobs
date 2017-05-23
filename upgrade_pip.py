# -*- coding: utf-8 -*-


import pip
from subprocess import call

for dist in pip.get_installed_distributions():
	call("python3 -m pip install --upgrade " + dist.project_name + " -i https://pypi.douban.com/simple" , shell=True)
