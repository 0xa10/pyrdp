#!/usr/bin/env python
# coding=utf-8

from distutils.core import setup, Extension

setup(name='rdpy',
    version='1.3.2',
    description='Remote Desktop Protocol in Python',
    long_description="""
    This is a Python implementation of the RDP protocol. This started as a fork of https://github.com/citronneur/rdpy,
    but ended up being a major reimplementation as we started changing the type / parsing systems. Still, part of the
    code comes from the original rdpy implementation, especially the packages related to encoding, Qt and
    cryptography.
    """,
    author='Émilio Gonzalez, Francis Labelle',
    author_email='egonzalez@gosecure.ca, flabelle@gosecure.ca',
    url='https://github.com/GoSecure/rdpy',
    packages=[
        'rdpy',
        'rdpy.core',
        'rdpy.crypto',
        'rdpy.security',
        'rdpy.ui',

        'rdpy.enum',
        'rdpy.enum.virtual_channel',
        'rdpy.enum.virtual_channel.clipboard',
        'rdpy.layer',
        'rdpy.layer.rdp',
        'rdpy.layer.rdp.virtual_channel',
        'rdpy.layer.rdp.virtual_channel.clipboard',
        'rdpy.mcs',
        'rdpy.mitm',
        'rdpy.mitm.virtual_channel',
        'rdpy.mitm.virtual_channel.clipboard',
        'rdpy.parser',
        'rdpy.parser.rdp',
        'rdpy.parser.rdp.virtual_channel',
        'rdpy.parser.rdp.virtual_channel.clipboard',
        'rdpy.pdu',
        'rdpy.pdu.rdp',
        'rdpy.pdu.rdp.virtual_channel',
        'rdpy.pdu.rdp.virtual_channel.clipboard',
        'rdpy.recording',
    ],
    ext_modules=[Extension('rle', ['ext/rle.c'])],
    scripts=[
            'bin/rdpy-rdpmitm.py',
            'bin/rdpy-player.py'
    ],
    install_requires=[
            'twisted',
            'pyopenssl',
            'service_identity',
            'qt4reactor',
            'rsa',
            'pyasn1',
            'notify2',
            'Crypto',
            'appdirs'
    ],
)
