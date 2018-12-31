#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2018年10月24日

@author: yangxu
'''
from django.conf.urls import url
from task import OptList,OptAudit,OptDelete
from task import ScriptList,ScriptAdd,ScriptDelete,get_script_content,\
ScriptUpdate,ScriptExecute,ScriptExecuteResult,script_copy
from task import AnsibleList,AnsibleAdd,ansible_upload_file,ansible_save,AnsibleUpdate,\
del_upload_file,AnsibleDelete,ansible_copy,AnsibleExecute,get_playbook_result
from task import FileList,FileDistribute,\
file_distribute_upload,file_distribute_delete,\
file_distribute_save,file_distribute_send,file_task_name_validate

urlpatterns = [
    url(r'^optlog/list/$',OptList.as_view(),name='OptList'),
    url(r'^optlog/delete/$',OptDelete,name='OptDelete'),
    url(r'^optlog/audit/(?P<pk>.+)$',OptAudit.as_view(),name='OptAudit'),
    url(r'^script/list/$',ScriptList.as_view(),name='ScriptList'),
    url(r'^script/add/$',ScriptAdd.as_view(),name='ScriptAdd'),
    url(r'^script/add/copy/$',script_copy),
    url(r'^script/execute/result/$',ScriptExecuteResult.as_view(),name='ScriptExecuteResult'),
    url(r'^script/execute/$',ScriptExecute,name='ScriptExecute'),
    url(r'^script/add/content/$',get_script_content),
    url(r'^script/update/(?P<pk>.+)$',ScriptUpdate.as_view(),name='ScriptUpdate'),
    url(r'^script/delete/(?P<pk>.+)$',ScriptDelete.as_view(),name='ScriptDelete'),
    url(r'^ansible/list/$',AnsibleList.as_view(),name='AnsibleList'),
    url(r'^ansible/add/$',AnsibleAdd.as_view(),name='AnsibleAdd'),
    url(r'^ansible/add/save/$',ansible_save),
    url(r'^ansible/add/copy/$',ansible_copy),
    url(r'^ansible/add/file/$',ansible_upload_file),
    url(r'^ansible/delete/file/$',del_upload_file),
    url(r'^ansible/update/(?P<pk>.+)$',AnsibleUpdate.as_view(),name='AnsibleUpdate'),
    url(r'^ansible/delete/(?P<pk>.+)$',AnsibleDelete.as_view(),name='AnsibleDelete'),
    url(r'^ansible/execute/$',AnsibleExecute.as_view()),
    url(r'^ansible/execute/result/$',get_playbook_result),
    url(r'^file/list/$',FileList.as_view(),name='FileList'),
    url(r'^file/add/$',FileDistribute.as_view(),name='FileAdd'),
    url(r'^file/add/upload/$',file_distribute_upload),
    url(r'^file/add/delete/$',file_distribute_delete),
    url(r'^file/add/validate/$',file_task_name_validate),
    url(r'^file/add/save/$',file_distribute_save),
    url(r'^file/add/send/$',file_distribute_send),
    ]