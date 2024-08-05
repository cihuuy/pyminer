import os
from setuptools import setup, Extension

# Fetch and process CFLAGS from environment
cflags = os.environ.get('CFLAGS', '').strip()
extra_compile_args = cflags.split() if cflags else (
    ['-O3', '-funroll-loops', '-fomit-frame-pointer']
    if os.environ.get('PLATFORM', '') == 'arm'
    else ['-O3']
)

# Define the scrypt extension module
scrypt_module = Extension(
    'scrypt',
    sources=[
        './algos/scrypt/scryptmodule.c',
        './algos/scrypt/scrypt.c'
    ],
    extra_compile_args=extra_compile_args,
    include_dirs=['./algos/scrypt']
)

# Define the yescrypt extension module
yescrypt_module = Extension(
    'yescrypt',
    sources=['./algos/yescrypt/yescrypt.c'],
    extra_compile_args=extra_compile_args,
    include_dirs=['./algos/yescrypt']
)

# Setup for scrypt module
setup(
    name='scrypt',
    version='1.0',
    description='Bindings for scrypt proof of work',
    ext_modules=[scrypt_module]
)

# Setup for yescrypt module
setup(
    name='yescrypt',
    version='1.0',
    description='Bindings for yescrypt proof of work',
    ext_modules=[yescrypt_module]
)
