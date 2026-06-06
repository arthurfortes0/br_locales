``br_locales`` - Brazilian Cities and States Data Library
===========================================================

.. image:: https://img.shields.io/badge/python-3.6+-blue.svg
   :target: https://www.python.org/downloads/
.. image:: https://img.shields.io/badge/license-MIT-green.svg
   :target: LICENSE


Overview
--------

A lightweight Python library providing comprehensive information about Brazilian cities and states
based on official IBGE (Brazilian Institute of Geography and Statistics) data. Contains all 27
states/federal entities and 5,570 municipalities with their official names, abbreviations, and
IBGE codes. **Zero external dependencies.**


Installation
------------

Install from PyPI::

    pip install br_locales

Or for development::

    pip install -e .


Quick Start
-----------

.. code-block:: python

    from br_locales import br_locale_info

    # Get all states
    print(br_locale_info.list_states)
    # Output: ['AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', ...]

    # Get all cities
    cities = br_locale_info.list_all_cities
    print(len(cities))  # 5570

    # Get cities for a state
    sp_cities = br_locale_info.list_cities(abbr='SP')
    print(len(sp_cities))  # 645

    # Find a city by name
    city = br_locale_info.get_city('São Paulo')
    print(city)  # {'code': 3550308, 'name': 'São Paulo', 'state': 'SP'}


API Reference
-------------

**Properties:**

* ``list_states`` - Returns a sorted list of state abbreviations (27 items)
* ``list_all_cities`` - Returns a flat list of all city names (5,570 items)
* ``dict_states`` - Returns a dict mapping state abbreviations to state info (code, name)

**Methods:**

* ``list_cities(abbr=None, code=None)`` - Get all cities for a state by abbreviation or IBGE code
* ``get_city(name)`` - Find a city by name (case-insensitive search)


Examples
--------

List all states::

    from br_locales import br_locale_info

    states = br_locale_info.list_states
    print(states)

Get state information::

    state_info = br_locale_info.dict_states
    print(state_info['SP'])
    # Output: {'code': 35, 'name': 'São Paulo'}

List cities by state abbreviation::

    cities = br_locale_info.list_cities(abbr='RJ')
    print(cities[:3])
    # Output: ['Angra dos Reis', 'Aperibé', 'Araçatuba', ...]

List cities by IBGE state code::

    cities = br_locale_info.list_cities(code=35)
    print(len(cities))  # 645 (São Paulo)

Find a city by name::

    city = br_locale_info.get_city('rio de janeiro')
    print(city)
    # Output: {'code': 3304557, 'name': 'Rio de Janeiro', 'state': 'RJ'}


Data Source
-----------

Data is based on official IBGE (Brazilian Institute of Geography and Statistics) information
and includes municipalities created up to 2022. The data is embedded as JSON and requires
no network calls or external data sources.


Contributing
------------

To report bugs, suggest features, or contribute improvements, please open an issue or
pull request on the project repository.


License
-------

MIT License - See LICENSE file for details


Authors
-------

Arthur Fortes

Data Version: 2022 (5,570 municipalities)

