# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: RequestAboutNewUser.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'RequestAboutNewUser.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19RequestAboutNewUser.proto\",\n\x10InfoAboutNewUser\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\" \n\x0eReportResponce\x12\x0e\n\x06status\x18\x01 \x01(\x08\x32=\n\rCreateNewUser\x12,\n\x06\x43reate\x12\x11.InfoAboutNewUser\x1a\x0f.ReportResponceb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'RequestAboutNewUser_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_INFOABOUTNEWUSER']._serialized_start=29
  _globals['_INFOABOUTNEWUSER']._serialized_end=73
  _globals['_REPORTRESPONCE']._serialized_start=75
  _globals['_REPORTRESPONCE']._serialized_end=107
  _globals['_CREATENEWUSER']._serialized_start=109
  _globals['_CREATENEWUSER']._serialized_end=170
# @@protoc_insertion_point(module_scope)
