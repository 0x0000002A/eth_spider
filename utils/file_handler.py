import os,sys
import settings


class FileHandler():
    def __init__(self,file_location,file_name,file_type=None):
        self.file_content = ""
        self.file_content_list = []
        self.file_location = file_location
        self.file_name = file_name
        self.file_type = settings.DEFAULT_WRITE_FILE_TYPE
        if file_type is not None:
            self.file_type = file_type
    
    def file_path(self):
        return self.file_location + self.file_name + "."  + self.file_type

    def file_open(self, mode='r'):
        #set read-only mode by default
        self.file = open(FileHandler.file_path(self), mode)

    def file_read(self, read_filter=None):
        if read_filter is None:
            filter_flg = True

        for line in self.file.readlines():
            if not filter_flg:
                line = read_filter(line)
            if not len(line) or filter_flg:
                self.file_content_list.append(line)
                continue
    
    def file_open_write(self, mode='w'):
        with open(FileHandler.file_path(self), mode) as self.file:
            self.file.write(self.file_content)

    def file_write(self):
        self.file.write(self.file_content)
    
    def file_close(self):
        self.file.close()
    
    def file_exists(self):
        pass
    
    def directory_exists(self):
        pass
    
    def IO_check(self):
        pass

