# -*- coding: utf-8 -*-
"""
config: Load application configuration and return an object representation.

Allows accessing configuration using "dot-notation" for supported configuration
file formats.

Supported formats are:
  * yml
  * TODO: ini
  * TODO: json
"""
import os
import yaml

from enum import Enum


Formats = Enum('Formats', names=[('yml', 1), ('ini', 2)])


def repr_fx(self):
    """
    Object representation. Function gets added as a method
    to generated classes.

    :return: string object representation
    """
    return yaml.dump(self)


def str_fx(self):
    """
    String representation. Function gets added as a method
    to generated classes.

    :return: string object representation
    """
    return yaml.dump(self, default_flow_style=False)


def get_fx(self, key, default=None):
    """
    Allow for c.get(foo) invocation.

    :param self: Config object
    :param key: config key to look for
    :param default: value if key is missing
    :return:
    """
    key_exists = hasattr(self, key)
    if key_exists:
        return get_item_fx(self, key)
    elif default:
        return default
    else:
        raise KeyError


def get_item_fx(self, key):
    """
    Function to implement __getitem__

    :param self:
    :param key:
    :return:
    """
    if hasattr(self, key):
        return getattr(self, key)
    else:
        raise KeyError


def __validate():
    """
    Hook to validate config.

    :return:
    """
    # TODO: implement


def __determine_config_type(path):
    """
    Find out the type of the configuration file.
    :param path: File path with extension
    :return: format type
    """
    # TODO: determine based on file extension for now
    ext = os.path.splitext(path)[1]
    if not ext:
        # TODO: no extension, need to figure out based on content
        ext = ''

    # TODO: configurate - so we can change order of heuristic checks
    if ext.lower() == '.yml' or ext.lower() == '.yaml':
        return 'yaml'
    elif ext.lower() == '.ini':
        return 'ini'
    else:
        # check based on content
        if __is_yaml():
            return 'yml'
        elif __is_ini():
            return 'ini'
    # TODO: raise
    raise ConfigException(message='Can not determine file type',
                          reason=path)


# TODO: implement
def __is_yaml():
    """

    :return:
    """


# TODO: implement
def __is_ini():
    """
    Try to determine if file is ini, either by extension or by loading.
    :return:
    """


# TODO: support
def __is_json():
    """

    :return:
    """


class Config(object):
    """
    The configuration object that will be populated.
    """
    pass


Config.__repr__ = repr_fx
Config.__str__ = str_fx
Config.__getitem__ = get_item_fx
Config.get = get_fx


def __construct(config, conf_dict):
    """
    Recursive function to construct an object corresponding to given value.

    Adds elements from the input yaml or ini to the configuration object in
    the first argument. For complex value types recursively instantiates new
     objects and attaches them into the configuration tree.

    The intent is to be able to access the yaml/ini config using dot notation -
    e.g. config.a.b.c.

    :param config: The config object to populate.
    :param yml: The yaml corresponding to the conf parameter.
    """

    for key in conf_dict:
        if type(conf_dict[key]) == dict:
            # create an object for the subsection
            klass = type(key, (), {})
            klass.__repr__ = repr_fx
            klass.__str__ = str_fx
            klass.__getitem__ = get_item_fx
            klass.get = get_fx
            obj = klass()
            __construct(obj, conf_dict[key])
            setattr(config, key, obj)
        else:
            # just set simple value
            setattr(config, key, conf_dict[key])


def load(paths):
    """
    Entry point for the config module.

    Load yml config files at specified path and convert to a config object.
    Merges the yaml files specified by the paths parameter - keys in a file
    later in the list override earlier keys.

    :param paths: List of complete paths of config files.
    :return Config object with member properties
    """
    if not paths:
        raise ConfigException(message='No configuration file specified',
                              reason=paths)
    config_dict = {}
    if type(paths) == str:
        paths = [paths]
    # for every filename in list...
    for path in paths:
        # read config file...
        with open(path) as f:

            # figure out format based on extension or content
            le_format = __determine_config_type(path)

            # get yml config as dict...
            if le_format == 'yaml':
                print('format is yaml')
                y = yaml.safe_load(f)
                # and merge into a single yaml dict.
                config_dict.update(y)
            elif le_format == 'ini':
                # TODO: load ini config
                print('format is ini')
                i = {}
                # merge into single ini dict
                config_dict.update(i)
    config = Config()
    # get object for each key and set on the config object
    __construct(config, config_dict)

    return config


class ConfigException(Exception):
    def __init__(self, message, reason):
        self.message = message
        self.reason = reason

    def __str__(self):
        return repr(self.message)
