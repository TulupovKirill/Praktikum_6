# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: AuthToAllService.proto
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
    'AuthToAllService.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16\x41uthToAllService.proto\"\x19\n\x0b\x41uthRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"\x1a\n\x08Response\x12\x0e\n\x06status\x18\x01 \x01(\x08\x32/\n\x0cSaveAuthUser\x12\x1f\n\x04Save\x12\x0c.AuthRequest\x1a\t.Responseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'AuthToAllService_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_AUTHREQUEST']._serialized_start=26
  _globals['_AUTHREQUEST']._serialized_end=51
  _globals['_RESPONSE']._serialized_start=53
  _globals['_RESPONSE']._serialized_end=79
  _globals['_SAVEAUTHUSER']._serialized_start=81
  _globals['_SAVEAUTHUSER']._serialized_end=128
# @@protoc_insertion_point(module_scope)
