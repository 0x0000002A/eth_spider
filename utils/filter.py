import json
import os
import settings
#todo move to file*.py

class FilterAppendRule(object):
    # decoder encoder todo
    # switch selector/parser automatically todo

    def json_dict_parse(self, string):
        #from json to dict
        return json.loads(string)

    def dict_selector(self, current_dict, element_list):
        selected_dict = dict
        if len(element_list) != 0:
            selected_dict = dict((key, current_dict[key]) for key in element_list if key in current_dict)
            current_dict = selected_dict
        return selected_dict
    
    def html_selector(self, html, elements):
        pass
    
    def dict_value_to_string_parse(self,current_dict,sep=","):
        value_list = []
        for key,value in current_dict.items():
            value_list.append(value)
        return sep.join(value_list)
    
    def dict_key_to_string_parse(self,current_dict,sep=","):
        key_list = []
        for key,value in current_dict.items():
            key_list.append(key)
        return sep.join(key_list)
    

class ImplFilter:
    def __init__(self, content):
        self.append_rule = FilterAppendRule
        #input content
        self.content_raw = content 
        self.selected_elements = []

    def eth_api_reponse_filter(self):
        # todo to create a eth_api layer 
        self.content_dict = self.append_rule.json_dict_parse(self.append_rule, self.content_raw)
        self.append_rule.dict_selector(self.append_rule, self.content_dict, ["result"])
        # todo should be adaptable for multiple types of "result"
        self.content_result_list = self.content_dict["result"]
        if type(self.content_result_list) != list:
            pass #exception
        if type(self.content_result_list[0]) != dict:
            pass # raise "error"
        for line in self.content_result_list:
            self.append_rule.dict_selector(self.append_rule, line, self.selected_elements)

    def eth_api_response_storage_filter(self):
        # todo move to filter combining the file/storage type
        if type(self.content_result_list) != list:
            pass #exception
        if type(self.content_result_list[0]) != dict:
            pass # raise "error"

        # todo combining file type
        self.file_content = ""
        line = ""
        header = ""
        if len(self.content_result_list) > 0:
            header = self.append_rule.dict_key_to_string_parse(self.append_rule, self.content_result_list[0])
            for line_dict in self.content_result_list:
                line = self.append_rule.dict_value_to_string_parse(self.append_rule, line_dict)
                self.file_content = self.file_content + line + settings.LINESEP
            self.file_content = header + settings.LINESEP + self.file_content 
    
