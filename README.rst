CnUniversityMap
==========

CnUniversityMap is a Python package that provides a simple University class to store and manage university information.

Download
----

You can download the latest version of the University package from PyPI:

.. code-block:: bash

   pip install cnuniversitymap

Alternatively, you can get the source code from GitHub:

.. code-block:: bash

   git clone https://github.com/robot-2233/cnuni.git

Contact me
--------

If you have any questions or feedback, please contact me through the following methods:

- email: frundles@qq.com
- wechat: zgndshkwxh

Usage examples
--------

Here are some basic examples using the University package:


Get university information
~~~~~~~~~~~~

.. code-block:: python

   print(university.cn_name)  # output: 北京大学
   print(university.en_name)  # output: Beijing University
   print(university.code)     # output: 4111010001

Get specific university from dict
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   print(universities_dict.get('清华大学'))

