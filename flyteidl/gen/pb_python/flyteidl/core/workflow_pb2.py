# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flyteidl/core/workflow.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from flyteidl.core import condition_pb2 as flyteidl_dot_core_dot_condition__pb2
from flyteidl.core import execution_pb2 as flyteidl_dot_core_dot_execution__pb2
from flyteidl.core import identifier_pb2 as flyteidl_dot_core_dot_identifier__pb2
from flyteidl.core import interface_pb2 as flyteidl_dot_core_dot_interface__pb2
from flyteidl.core import literals_pb2 as flyteidl_dot_core_dot_literals__pb2
from flyteidl.core import tasks_pb2 as flyteidl_dot_core_dot_tasks__pb2
from flyteidl.core import types_pb2 as flyteidl_dot_core_dot_types__pb2
from flyteidl.core import security_pb2 as flyteidl_dot_core_dot_security__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x66lyteidl/core/workflow.proto\x12\rflyteidl.core\x1a\x1d\x66lyteidl/core/condition.proto\x1a\x1d\x66lyteidl/core/execution.proto\x1a\x1e\x66lyteidl/core/identifier.proto\x1a\x1d\x66lyteidl/core/interface.proto\x1a\x1c\x66lyteidl/core/literals.proto\x1a\x19\x66lyteidl/core/tasks.proto\x1a\x19\x66lyteidl/core/types.proto\x1a\x1c\x66lyteidl/core/security.proto\x1a\x1egoogle/protobuf/duration.proto\"{\n\x07IfBlock\x12>\n\tcondition\x18\x01 \x01(\x0b\x32 .flyteidl.core.BooleanExpressionR\tcondition\x12\x30\n\tthen_node\x18\x02 \x01(\x0b\x32\x13.flyteidl.core.NodeR\x08thenNode\"\xd4\x01\n\x0bIfElseBlock\x12*\n\x04\x63\x61se\x18\x01 \x01(\x0b\x32\x16.flyteidl.core.IfBlockR\x04\x63\x61se\x12,\n\x05other\x18\x02 \x03(\x0b\x32\x16.flyteidl.core.IfBlockR\x05other\x12\x32\n\telse_node\x18\x03 \x01(\x0b\x32\x13.flyteidl.core.NodeH\x00R\x08\x65lseNode\x12,\n\x05\x65rror\x18\x04 \x01(\x0b\x32\x14.flyteidl.core.ErrorH\x00R\x05\x65rrorB\t\n\x07\x64\x65\x66\x61ult\"A\n\nBranchNode\x12\x33\n\x07if_else\x18\x01 \x01(\x0b\x32\x1a.flyteidl.core.IfElseBlockR\x06ifElse\"\x97\x01\n\x08TaskNode\x12>\n\x0creference_id\x18\x01 \x01(\x0b\x32\x19.flyteidl.core.IdentifierH\x00R\x0breferenceId\x12>\n\toverrides\x18\x02 \x01(\x0b\x32 .flyteidl.core.TaskNodeOverridesR\toverridesB\x0b\n\treference\"\xa6\x01\n\x0cWorkflowNode\x12\x42\n\x0elaunchplan_ref\x18\x01 \x01(\x0b\x32\x19.flyteidl.core.IdentifierH\x00R\rlaunchplanRef\x12\x45\n\x10sub_workflow_ref\x18\x02 \x01(\x0b\x32\x19.flyteidl.core.IdentifierH\x00R\x0esubWorkflowRefB\x0b\n\treference\"/\n\x10\x41pproveCondition\x12\x1b\n\tsignal_id\x18\x01 \x01(\tR\x08signalId\"\x90\x01\n\x0fSignalCondition\x12\x1b\n\tsignal_id\x18\x01 \x01(\tR\x08signalId\x12.\n\x04type\x18\x02 \x01(\x0b\x32\x1a.flyteidl.core.LiteralTypeR\x04type\x12\x30\n\x14output_variable_name\x18\x03 \x01(\tR\x12outputVariableName\"G\n\x0eSleepCondition\x12\x35\n\x08\x64uration\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationR\x08\x64uration\"\xc5\x01\n\x08GateNode\x12;\n\x07\x61pprove\x18\x01 \x01(\x0b\x32\x1f.flyteidl.core.ApproveConditionH\x00R\x07\x61pprove\x12\x38\n\x06signal\x18\x02 \x01(\x0b\x32\x1e.flyteidl.core.SignalConditionH\x00R\x06signal\x12\x35\n\x05sleep\x18\x03 \x01(\x0b\x32\x1d.flyteidl.core.SleepConditionH\x00R\x05sleepB\x0b\n\tcondition\"\xbf\x01\n\tArrayNode\x12\'\n\x04node\x18\x01 \x01(\x0b\x32\x13.flyteidl.core.NodeR\x04node\x12 \n\x0bparallelism\x18\x02 \x01(\rR\x0bparallelism\x12%\n\rmin_successes\x18\x03 \x01(\rH\x00R\x0cminSuccesses\x12,\n\x11min_success_ratio\x18\x04 \x01(\x02H\x00R\x0fminSuccessRatioB\x12\n\x10success_criteria\"\xce\x01\n\x0cNodeMetadata\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x33\n\x07timeout\x18\x04 \x01(\x0b\x32\x19.google.protobuf.DurationR\x07timeout\x12\x36\n\x07retries\x18\x05 \x01(\x0b\x32\x1c.flyteidl.core.RetryStrategyR\x07retries\x12&\n\rinterruptible\x18\x06 \x01(\x08H\x00R\rinterruptibleB\x15\n\x13interruptible_value\"/\n\x05\x41lias\x12\x10\n\x03var\x18\x01 \x01(\tR\x03var\x12\x14\n\x05\x61lias\x18\x02 \x01(\tR\x05\x61lias\"\x9f\x04\n\x04Node\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x37\n\x08metadata\x18\x02 \x01(\x0b\x32\x1b.flyteidl.core.NodeMetadataR\x08metadata\x12.\n\x06inputs\x18\x03 \x03(\x0b\x32\x16.flyteidl.core.BindingR\x06inputs\x12*\n\x11upstream_node_ids\x18\x04 \x03(\tR\x0fupstreamNodeIds\x12;\n\x0eoutput_aliases\x18\x05 \x03(\x0b\x32\x14.flyteidl.core.AliasR\routputAliases\x12\x36\n\ttask_node\x18\x06 \x01(\x0b\x32\x17.flyteidl.core.TaskNodeH\x00R\x08taskNode\x12\x42\n\rworkflow_node\x18\x07 \x01(\x0b\x32\x1b.flyteidl.core.WorkflowNodeH\x00R\x0cworkflowNode\x12<\n\x0b\x62ranch_node\x18\x08 \x01(\x0b\x32\x19.flyteidl.core.BranchNodeH\x00R\nbranchNode\x12\x36\n\tgate_node\x18\t \x01(\x0b\x32\x17.flyteidl.core.GateNodeH\x00R\x08gateNode\x12\x39\n\narray_node\x18\n \x01(\x0b\x32\x18.flyteidl.core.ArrayNodeH\x00R\tarrayNodeB\x08\n\x06target\"\xfc\x02\n\x10WorkflowMetadata\x12M\n\x12quality_of_service\x18\x01 \x01(\x0b\x32\x1f.flyteidl.core.QualityOfServiceR\x10qualityOfService\x12N\n\non_failure\x18\x02 \x01(\x0e\x32/.flyteidl.core.WorkflowMetadata.OnFailurePolicyR\tonFailure\x12=\n\x04tags\x18\x03 \x03(\x0b\x32).flyteidl.core.WorkflowMetadata.TagsEntryR\x04tags\x1a\x37\n\tTagsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"Q\n\x0fOnFailurePolicy\x12\x14\n\x10\x46\x41IL_IMMEDIATELY\x10\x00\x12(\n$FAIL_AFTER_EXECUTABLE_NODES_COMPLETE\x10\x01\"@\n\x18WorkflowMetadataDefaults\x12$\n\rinterruptible\x18\x01 \x01(\x08R\rinterruptible\"\xa2\x03\n\x10WorkflowTemplate\x12)\n\x02id\x18\x01 \x01(\x0b\x32\x19.flyteidl.core.IdentifierR\x02id\x12;\n\x08metadata\x18\x02 \x01(\x0b\x32\x1f.flyteidl.core.WorkflowMetadataR\x08metadata\x12;\n\tinterface\x18\x03 \x01(\x0b\x32\x1d.flyteidl.core.TypedInterfaceR\tinterface\x12)\n\x05nodes\x18\x04 \x03(\x0b\x32\x13.flyteidl.core.NodeR\x05nodes\x12\x30\n\x07outputs\x18\x05 \x03(\x0b\x32\x16.flyteidl.core.BindingR\x07outputs\x12\x36\n\x0c\x66\x61ilure_node\x18\x06 \x01(\x0b\x32\x13.flyteidl.core.NodeR\x0b\x66\x61ilureNode\x12T\n\x11metadata_defaults\x18\x07 \x01(\x0b\x32\'.flyteidl.core.WorkflowMetadataDefaultsR\x10metadataDefaults\"K\n\x11TaskNodeOverrides\x12\x36\n\tresources\x18\x01 \x01(\x0b\x32\x18.flyteidl.core.ResourcesR\tresourcesB\xad\x01\n\x11\x63om.flyteidl.coreB\rWorkflowProtoP\x01Z4github.com/flyteorg/flyteidl/gen/pb-go/flyteidl/core\xa2\x02\x03\x46\x43X\xaa\x02\rFlyteidl.Core\xca\x02\rFlyteidl\\Core\xe2\x02\x19\x46lyteidl\\Core\\GPBMetadata\xea\x02\x0e\x46lyteidl::Coreb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'flyteidl.core.workflow_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\021com.flyteidl.coreB\rWorkflowProtoP\001Z4github.com/flyteorg/flyteidl/gen/pb-go/flyteidl/core\242\002\003FCX\252\002\rFlyteidl.Core\312\002\rFlyteidl\\Core\342\002\031Flyteidl\\Core\\GPBMetadata\352\002\016Flyteidl::Core'
  _WORKFLOWMETADATA_TAGSENTRY._options = None
  _WORKFLOWMETADATA_TAGSENTRY._serialized_options = b'8\001'
  _globals['_IFBLOCK']._serialized_start=318
  _globals['_IFBLOCK']._serialized_end=441
  _globals['_IFELSEBLOCK']._serialized_start=444
  _globals['_IFELSEBLOCK']._serialized_end=656
  _globals['_BRANCHNODE']._serialized_start=658
  _globals['_BRANCHNODE']._serialized_end=723
  _globals['_TASKNODE']._serialized_start=726
  _globals['_TASKNODE']._serialized_end=877
  _globals['_WORKFLOWNODE']._serialized_start=880
  _globals['_WORKFLOWNODE']._serialized_end=1046
  _globals['_APPROVECONDITION']._serialized_start=1048
  _globals['_APPROVECONDITION']._serialized_end=1095
  _globals['_SIGNALCONDITION']._serialized_start=1098
  _globals['_SIGNALCONDITION']._serialized_end=1242
  _globals['_SLEEPCONDITION']._serialized_start=1244
  _globals['_SLEEPCONDITION']._serialized_end=1315
  _globals['_GATENODE']._serialized_start=1318
  _globals['_GATENODE']._serialized_end=1515
  _globals['_ARRAYNODE']._serialized_start=1518
  _globals['_ARRAYNODE']._serialized_end=1709
  _globals['_NODEMETADATA']._serialized_start=1712
  _globals['_NODEMETADATA']._serialized_end=1918
  _globals['_ALIAS']._serialized_start=1920
  _globals['_ALIAS']._serialized_end=1967
  _globals['_NODE']._serialized_start=1970
  _globals['_NODE']._serialized_end=2513
  _globals['_WORKFLOWMETADATA']._serialized_start=2516
  _globals['_WORKFLOWMETADATA']._serialized_end=2896
  _globals['_WORKFLOWMETADATA_TAGSENTRY']._serialized_start=2758
  _globals['_WORKFLOWMETADATA_TAGSENTRY']._serialized_end=2813
  _globals['_WORKFLOWMETADATA_ONFAILUREPOLICY']._serialized_start=2815
  _globals['_WORKFLOWMETADATA_ONFAILUREPOLICY']._serialized_end=2896
  _globals['_WORKFLOWMETADATADEFAULTS']._serialized_start=2898
  _globals['_WORKFLOWMETADATADEFAULTS']._serialized_end=2962
  _globals['_WORKFLOWTEMPLATE']._serialized_start=2965
  _globals['_WORKFLOWTEMPLATE']._serialized_end=3383
  _globals['_TASKNODEOVERRIDES']._serialized_start=3385
  _globals['_TASKNODEOVERRIDES']._serialized_end=3460
# @@protoc_insertion_point(module_scope)