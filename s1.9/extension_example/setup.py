#!/usr/bin/env python3

from distutils.core import setup, Extension

# устанавливаем модуль
setup(
	name = "helloworld",
	version = "1.0.0",
    description="my first extension",
	ext_modules = [Extension("helloworld", ["bind.c", "libmypy.c"])]
	)