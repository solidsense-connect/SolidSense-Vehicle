# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: OBD_Service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='OBD_Service.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x11OBD_Service.proto\"\x18\n\tStart_OBD\x12\x0b\n\x03MAC\x18\x01 \x01(\t\"\x9d\x01\n\rOBD_CMD_value\x12\x0b\n\x03\x63md\x18\x01 \x01(\t\x12\'\n\x04type\x18\x02 \x01(\x0e\x32\x19.OBD_CMD_value.value_type\x12\x0b\n\x01\x66\x18\x04 \x01(\x02H\x00\x12\x0b\n\x01s\x18\x05 \x01(\tH\x00\x12\x0c\n\x04unit\x18\n \x01(\t\"%\n\nvalue_type\x12\x0c\n\x08Quantity\x10\x00\x12\t\n\x05Other\x10\x01\x42\x07\n\x05value\"s\n\nOBD_Result\x12\x11\n\tconnected\x18\x01 \x01(\x08\x12\x11\n\tengine_on\x18\x02 \x01(\x08\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x10\n\x08obd_time\x18\x04 \x01(\t\x12\x1e\n\x06values\x18\x05 \x03(\x0b\x32\x0e.OBD_CMD_value\"\x7f\n\x07OBD_cmd\x12\'\n\x07request\x18\x01 \x01(\x0e\x32\x16.OBD_cmd.RequestResult\x12\x10\n\x08\x63ommands\x18\x02 \x01(\t\x12\r\n\x05rules\x18\x04 \x01(\t\"*\n\rRequestResult\x12\x0b\n\x07\x44\x65\x66\x61ult\x10\x00\x12\x0c\n\x08Specific\x10\x01\"$\n\x11OBD_StatusRequest\x12\x0f\n\x07request\x18\x01 \x01(\t\"\x87\x01\n\nOBD_status\x12\x11\n\tconnected\x18\x01 \x01(\x08\x12\x11\n\tengine_on\x18\x02 \x01(\x08\x12\x13\n\x0b\x61utoconnect\x18\x03 \x01(\x08\x12\r\n\x05state\x18\x07 \x01(\t\x12\x10\n\x08protocol\x18\x04 \x01(\t\x12\x0b\n\x03MAC\x18\x05 \x01(\t\x12\x10\n\x08\x63ommands\x18\x06 \x01(\t2\x9c\x01\n\x0bOBD_Service\x12)\n\x06Status\x12\x12.OBD_StatusRequest\x1a\x0b.OBD_status\x12\"\n\x07\x43onnect\x12\n.Start_OBD\x1a\x0b.OBD_Result\x12\x1f\n\x04Read\x12\x08.OBD_cmd\x1a\x0b.OBD_Result0\x01\x12\x1d\n\x04Stop\x12\x08.OBD_cmd\x1a\x0b.OBD_Resultb\x06proto3')
)



_OBD_CMD_VALUE_VALUE_TYPE = _descriptor.EnumDescriptor(
  name='value_type',
  full_name='OBD_CMD_value.value_type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Quantity', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Other', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=159,
  serialized_end=196,
)
_sym_db.RegisterEnumDescriptor(_OBD_CMD_VALUE_VALUE_TYPE)

_OBD_CMD_REQUESTRESULT = _descriptor.EnumDescriptor(
  name='RequestResult',
  full_name='OBD_cmd.RequestResult',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Default', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Specific', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=409,
  serialized_end=451,
)
_sym_db.RegisterEnumDescriptor(_OBD_CMD_REQUESTRESULT)


_START_OBD = _descriptor.Descriptor(
  name='Start_OBD',
  full_name='Start_OBD',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='MAC', full_name='Start_OBD.MAC', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=21,
  serialized_end=45,
)


_OBD_CMD_VALUE = _descriptor.Descriptor(
  name='OBD_CMD_value',
  full_name='OBD_CMD_value',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cmd', full_name='OBD_CMD_value.cmd', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='OBD_CMD_value.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='f', full_name='OBD_CMD_value.f', index=2,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='s', full_name='OBD_CMD_value.s', index=3,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unit', full_name='OBD_CMD_value.unit', index=4,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _OBD_CMD_VALUE_VALUE_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='value', full_name='OBD_CMD_value.value',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=48,
  serialized_end=205,
)


_OBD_RESULT = _descriptor.Descriptor(
  name='OBD_Result',
  full_name='OBD_Result',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='connected', full_name='OBD_Result.connected', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='engine_on', full_name='OBD_Result.engine_on', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='OBD_Result.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='obd_time', full_name='OBD_Result.obd_time', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='values', full_name='OBD_Result.values', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=207,
  serialized_end=322,
)


_OBD_CMD = _descriptor.Descriptor(
  name='OBD_cmd',
  full_name='OBD_cmd',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request', full_name='OBD_cmd.request', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='commands', full_name='OBD_cmd.commands', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rules', full_name='OBD_cmd.rules', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _OBD_CMD_REQUESTRESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=324,
  serialized_end=451,
)


_OBD_STATUSREQUEST = _descriptor.Descriptor(
  name='OBD_StatusRequest',
  full_name='OBD_StatusRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request', full_name='OBD_StatusRequest.request', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=453,
  serialized_end=489,
)


_OBD_STATUS = _descriptor.Descriptor(
  name='OBD_status',
  full_name='OBD_status',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='connected', full_name='OBD_status.connected', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='engine_on', full_name='OBD_status.engine_on', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='autoconnect', full_name='OBD_status.autoconnect', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='OBD_status.state', index=3,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='protocol', full_name='OBD_status.protocol', index=4,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='MAC', full_name='OBD_status.MAC', index=5,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='commands', full_name='OBD_status.commands', index=6,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=492,
  serialized_end=627,
)

_OBD_CMD_VALUE.fields_by_name['type'].enum_type = _OBD_CMD_VALUE_VALUE_TYPE
_OBD_CMD_VALUE_VALUE_TYPE.containing_type = _OBD_CMD_VALUE
_OBD_CMD_VALUE.oneofs_by_name['value'].fields.append(
  _OBD_CMD_VALUE.fields_by_name['f'])
_OBD_CMD_VALUE.fields_by_name['f'].containing_oneof = _OBD_CMD_VALUE.oneofs_by_name['value']
_OBD_CMD_VALUE.oneofs_by_name['value'].fields.append(
  _OBD_CMD_VALUE.fields_by_name['s'])
_OBD_CMD_VALUE.fields_by_name['s'].containing_oneof = _OBD_CMD_VALUE.oneofs_by_name['value']
_OBD_RESULT.fields_by_name['values'].message_type = _OBD_CMD_VALUE
_OBD_CMD.fields_by_name['request'].enum_type = _OBD_CMD_REQUESTRESULT
_OBD_CMD_REQUESTRESULT.containing_type = _OBD_CMD
DESCRIPTOR.message_types_by_name['Start_OBD'] = _START_OBD
DESCRIPTOR.message_types_by_name['OBD_CMD_value'] = _OBD_CMD_VALUE
DESCRIPTOR.message_types_by_name['OBD_Result'] = _OBD_RESULT
DESCRIPTOR.message_types_by_name['OBD_cmd'] = _OBD_CMD
DESCRIPTOR.message_types_by_name['OBD_StatusRequest'] = _OBD_STATUSREQUEST
DESCRIPTOR.message_types_by_name['OBD_status'] = _OBD_STATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Start_OBD = _reflection.GeneratedProtocolMessageType('Start_OBD', (_message.Message,), dict(
  DESCRIPTOR = _START_OBD,
  __module__ = 'OBD_Service_pb2'
  # @@protoc_insertion_point(class_scope:Start_OBD)
  ))
_sym_db.RegisterMessage(Start_OBD)

OBD_CMD_value = _reflection.GeneratedProtocolMessageType('OBD_CMD_value', (_message.Message,), dict(
  DESCRIPTOR = _OBD_CMD_VALUE,
  __module__ = 'OBD_Service_pb2'
  # @@protoc_insertion_point(class_scope:OBD_CMD_value)
  ))
_sym_db.RegisterMessage(OBD_CMD_value)

OBD_Result = _reflection.GeneratedProtocolMessageType('OBD_Result', (_message.Message,), dict(
  DESCRIPTOR = _OBD_RESULT,
  __module__ = 'OBD_Service_pb2'
  # @@protoc_insertion_point(class_scope:OBD_Result)
  ))
_sym_db.RegisterMessage(OBD_Result)

OBD_cmd = _reflection.GeneratedProtocolMessageType('OBD_cmd', (_message.Message,), dict(
  DESCRIPTOR = _OBD_CMD,
  __module__ = 'OBD_Service_pb2'
  # @@protoc_insertion_point(class_scope:OBD_cmd)
  ))
_sym_db.RegisterMessage(OBD_cmd)

OBD_StatusRequest = _reflection.GeneratedProtocolMessageType('OBD_StatusRequest', (_message.Message,), dict(
  DESCRIPTOR = _OBD_STATUSREQUEST,
  __module__ = 'OBD_Service_pb2'
  # @@protoc_insertion_point(class_scope:OBD_StatusRequest)
  ))
_sym_db.RegisterMessage(OBD_StatusRequest)

OBD_status = _reflection.GeneratedProtocolMessageType('OBD_status', (_message.Message,), dict(
  DESCRIPTOR = _OBD_STATUS,
  __module__ = 'OBD_Service_pb2'
  # @@protoc_insertion_point(class_scope:OBD_status)
  ))
_sym_db.RegisterMessage(OBD_status)



_OBD_SERVICE = _descriptor.ServiceDescriptor(
  name='OBD_Service',
  full_name='OBD_Service',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=630,
  serialized_end=786,
  methods=[
  _descriptor.MethodDescriptor(
    name='Status',
    full_name='OBD_Service.Status',
    index=0,
    containing_service=None,
    input_type=_OBD_STATUSREQUEST,
    output_type=_OBD_STATUS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Connect',
    full_name='OBD_Service.Connect',
    index=1,
    containing_service=None,
    input_type=_START_OBD,
    output_type=_OBD_RESULT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Read',
    full_name='OBD_Service.Read',
    index=2,
    containing_service=None,
    input_type=_OBD_CMD,
    output_type=_OBD_RESULT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Stop',
    full_name='OBD_Service.Stop',
    index=3,
    containing_service=None,
    input_type=_OBD_CMD,
    output_type=_OBD_RESULT,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_OBD_SERVICE)

DESCRIPTOR.services_by_name['OBD_Service'] = _OBD_SERVICE

# @@protoc_insertion_point(module_scope)
