# -*- coding: utf-8 -*-

# Resource object code
#
# Created by: The Resource Compiler for PyQt5 (Qt v5.15.2)
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore

qt_resource_data = b"\
\x00\x00\x01\x90\
\x0d\
\x0a\x51\x57\x69\x64\x67\x65\x74\x20\x7b\x0d\x0a\x20\x20\x20\x20\
\x62\x61\x63\x6b\x67\x72\x6f\x75\x6e\x64\x2d\x63\x6f\x6c\x6f\x72\
\x3a\x20\x22\x23\x34\x35\x34\x35\x34\x35\x22\x3b\x0d\x0a\x20\x20\
\x20\x20\x63\x6f\x6c\x6f\x72\x3a\x20\x22\x77\x68\x69\x74\x65\x22\
\x3b\x0d\x0a\x7d\x0d\x0a\x51\x50\x75\x73\x68\x42\x75\x74\x74\x6f\
\x6e\x20\x7b\x0d\x0a\x20\x20\x20\x20\x66\x6f\x6e\x74\x2d\x73\x69\
\x7a\x65\x3a\x20\x31\x36\x70\x78\x3b\x0d\x0a\x20\x20\x20\x20\x62\
\x61\x63\x6b\x67\x72\x6f\x75\x6e\x64\x2d\x63\x6f\x6c\x6f\x72\x3a\
\x20\x22\x64\x61\x72\x6b\x67\x72\x65\x79\x22\x3b\x0d\x0a\x20\x20\
\x20\x20\x63\x6f\x6c\x6f\x72\x3a\x20\x22\x62\x6c\x61\x63\x6b\x22\
\x3b\x0d\x0a\x7d\x0d\x0a\x20\x51\x4c\x69\x6e\x65\x45\x64\x69\x74\
\x20\x7b\x0d\x0a\x20\x20\x20\x20\x62\x61\x63\x6b\x67\x72\x6f\x75\
\x6e\x64\x2d\x63\x6f\x6c\x6f\x72\x3a\x20\x22\x77\x68\x69\x74\x65\
\x22\x3b\x0d\x0a\x20\x20\x20\x20\x63\x6f\x6c\x6f\x72\x3a\x20\x22\
\x62\x6c\x61\x63\x6b\x22\x3b\x0d\x0a\x7d\x0d\x0a\x51\x43\x6f\x6d\
\x62\x6f\x42\x6f\x78\x20\x7b\x0d\x0a\x20\x20\x20\x20\x62\x61\x63\
\x6b\x67\x72\x6f\x75\x6e\x64\x2d\x63\x6f\x6c\x6f\x72\x3a\x20\x22\
\x77\x68\x69\x74\x65\x22\x3b\x0d\x0a\x20\x20\x20\x20\x63\x6f\x6c\
\x6f\x72\x3a\x20\x22\x62\x6c\x61\x63\x6b\x22\x3b\x0d\x0a\x7d\x0d\
\x0a\x51\x4c\x61\x62\x65\x6c\x20\x7b\x0d\x0a\x20\x20\x20\x20\x66\
\x6f\x6e\x74\x2d\x73\x69\x7a\x65\x3a\x20\x33\x32\x70\x78\x3b\x0d\
\x0a\x20\x20\x20\x20\x62\x61\x63\x6b\x67\x72\x6f\x75\x6e\x64\x2d\
\x63\x6f\x6c\x6f\x72\x3a\x20\x22\x74\x72\x61\x6e\x73\x70\x61\x72\
\x65\x6e\x74\x22\x3b\x0d\x0a\x20\x20\x20\x20\x63\x6f\x6c\x6f\x72\
\x3a\x20\x22\x77\x68\x69\x74\x65\x22\x3b\x0d\x0a\x7d\x0d\x0a\
"

qt_resource_name = b"\
\x00\x09\
\x00\x28\xbf\x23\
\x00\x73\
\x00\x74\x00\x79\x00\x6c\x00\x65\x00\x2e\x00\x63\x00\x73\x00\x73\
"

qt_resource_struct_v1 = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
"

qt_resource_struct_v2 = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01\x89\x4a\x47\x34\xa3\
"

qt_version = [int(v) for v in QtCore.qVersion().split('.')]
if qt_version < [5, 8, 0]:
    rcc_version = 1
    qt_resource_struct = qt_resource_struct_v1
else:
    rcc_version = 2
    qt_resource_struct = qt_resource_struct_v2

def qInitResources():
    QtCore.qRegisterResourceData(rcc_version, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(rcc_version, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
