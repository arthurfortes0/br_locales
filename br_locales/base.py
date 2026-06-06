"""Module for retrieving Brazilian cities and states information from IBGE data.

This module provides access to a comprehensive database of Brazilian states and
cities based on official IBGE (Brazilian Institute of Geography and Statistics)
information. The data includes state abbreviations, official names, IBGE codes,
and city listings for each state.
"""

import json
import os
from collections import OrderedDict


class BrazilLocations:
    """Manages Brazilian cities and states data from IBGE.

    This class loads Brazilian geographic data from a JSON file and provides
    methods to query states and cities by various criteria including
    abbreviation, code, or name.

    Attributes:
        _locations (OrderedDict): Internal data structure containing all states
            and cities information, keyed by state name.
    """

    def __init__(self):
        """Initialize BrazilLocations and load data from JSON file."""
        current_dir = os.path.dirname(__file__)
        json_path = os.path.join(current_dir, "states_and_cities_10_22.json")
        
        with open(json_path, encoding='utf-8') as f:
            self._locations = json.load(f)

    @property
    def list_states(self):
        """Return a sorted list of state abbreviations.

        Returns:
            list: Sorted list of state abbreviations (e.g., ['AC', 'AL', ...]).
        """
        return sorted([self._locations[state]['abbr'] for state in self._locations])

    @property
    def list_all_cities(self):
        """Return a flat list of all city names across all states.

        Returns:
            list: List containing all city names in Brazil.
        """
        cities = []
        for state in self._locations:
            for city in self._locations[state]['cities']:
                cities.append(city['name'])
        return cities

    @property
    def dict_states(self):
        """Return a dictionary mapping state abbreviations to state info.

        Returns:
            dict: Dictionary with state abbreviations as keys and values
                containing 'code' (IBGE code) and 'name' (full state name).
        """
        states_dict = {}
        for state_key in self._locations:
            state_data = self._locations[state_key]
            states_dict[state_data['abbr']] = {
                'code': state_data['code'],
                'name': state_data['name']
            }
        return states_dict

    def list_cities(self, abbr=None, code=None):
        """List all cities for a given state.

        Args:
            abbr (str, optional): State abbreviation (e.g., 'SP', 'RJ').
            code (int, optional): IBGE state code.

        Returns:
            list: List of city names for the specified state, or
                'Not found' if state is not found or no parameters provided.
        """
        if code is None and abbr is None:
            return None

        cities = 'Not found'
        state_codes = {
            self._locations[state]['code']: state
            for state in self._locations.keys()
        }

        if code is not None:
            if code in state_codes:
                state_key = state_codes[code]
                cities = [
                    city['name']
                    for city in self._locations[state_key]['cities']
                ]

        if abbr is not None:
            abbr_upper = abbr.upper()
            if abbr_upper in self._locations.keys():
                cities = [
                    city['name']
                    for city in self._locations[abbr_upper]['cities']
                ]

        return cities

    def get_city(self, name=None):
        """Find a city by name (case-insensitive).

        Args:
            name (str, optional): City name to search for.

        Returns:
            dict: City object containing name, state, and IBGE code,
                or None if city not found or name is None.
        """
        if name is None:
            return None

        name_upper = name.upper()
        for state in self._locations:
            for city in self._locations[state]['cities']:
                if city['name'].upper() == name_upper:
                    return city

        return None


# Module-level singleton instance for convenient access
br_locale_info = BrazilLocations()
