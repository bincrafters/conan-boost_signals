#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.68.0@bincrafters/stable")

class BoostSignalsConan(base.BoostBaseConan):
    name = "boost_signals"
    url = "https://github.com/bincrafters/conan-boost_signals"
    lib_short_names = ["signals"]
    options = {"shared": [True, False]}
    default_options = "shared=False"
    b2_requires = [
        "boost_any",
        "boost_config",
        "boost_core",
        "boost_function",
        "boost_iterator",
        "boost_mpl",
        "boost_optional",
        "boost_smart_ptr",
        "boost_type_traits",
        "boost_utility"
    ]
