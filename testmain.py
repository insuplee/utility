#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Insup Lee <islee94@korea.ac.kr>
# Mar 2020


import os
import configparser as cp

_DEBUG = True
if _DEBUG:
    def debug_print(args_tuple):
        print(args_tuple)
else:
    def debug_print(args_tuple):
        pass


# 200309 : managing python global variables (co-related variables)
def get_all_path_dict(data_name="test_data"):
    # extract specific path from abspath
    home_dir = "\\".join(os.path.dirname(os.path.abspath(__file__)).split("\\")[:-2])

    path_1 = os.path.join(home_dir, data_name)
    path_2 = os.path.join(path_1, "tmp_dir")

    all_path_dict = {
        "PATH_1": path_1,
        "PATH_2": path_2
    }

    return all_path_dict


def manage_changeable_g_variables():
    print("[!] manage_changeable_g_variables")
    debug_print(get_all_path_dict(data_name="ADFA-LD"))
    debug_print(get_all_path_dict(data_name="ADFA-LD_10"))


# 200310 : os library test
def use_os_lib():
    print("[!] use_os_lib")
    user_dir = os.environ['USERPROFILE']  # C:\Users\user
    debug_print(user_dir)


# 200310 :
def use_config(filename, keyword):
    print("[!] use_config")
    config = cp.ConfigParser()
    config.read(filename)

    conf_dict = config[keyword.upper()]
    for key in conf_dict:
        debug_print((key, conf_dict[key]))


def main():
    print("[!] TestMain")


if __name__ == "__main__":
    manage_changeable_g_variables()
    use_config(filename="setting.conf", keyword="KEY1")
