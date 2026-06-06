"""Tests for br_locales module."""

from br_locales import BrazilLocations, br_locale_info


class TestBrazilLocations:
    """Test suite for BrazilLocations class."""

    def test_instance_initialization(self):
        """Test that BrazilLocations can be instantiated."""
        locations = BrazilLocations()
        assert locations is not None

    def test_list_states(self):
        """Test list_states property returns correct number of states."""
        states = br_locale_info.list_states
        assert len(states) == 27
        assert isinstance(states, list)
        assert 'SP' in states
        assert 'AC' in states
        # Verify it's sorted
        assert states == sorted(states)

    def test_dict_states(self):
        """Test dict_states property."""
        states_dict = br_locale_info.dict_states
        assert len(states_dict) == 27
        assert 'SP' in states_dict
        assert 'code' in states_dict['SP']
        assert 'name' in states_dict['SP']
        assert states_dict['SP']['code'] == 35
        assert states_dict['SP']['name'] == 'São Paulo'

    def test_list_all_cities(self):
        """Test list_all_cities property."""
        cities = br_locale_info.list_all_cities
        assert len(cities) == 5570
        assert isinstance(cities, list)
        assert 'São Paulo' in cities

    def test_list_cities_by_abbr(self):
        """Test list_cities with abbreviation."""
        cities = br_locale_info.list_cities(abbr='SP')
        assert isinstance(cities, list)
        assert len(cities) > 0
        assert 'São Paulo' in cities

    def test_list_cities_by_code(self):
        """Test list_cities with IBGE code."""
        cities = br_locale_info.list_cities(code=35)
        assert isinstance(cities, list)
        assert len(cities) > 0
        assert 'São Paulo' in cities

    def test_list_cities_abbr_case_insensitive(self):
        """Test that list_cities abbr parameter is case-insensitive."""
        cities_upper = br_locale_info.list_cities(abbr='SP')
        cities_lower = br_locale_info.list_cities(abbr='sp')
        assert cities_upper == cities_lower

    def test_list_cities_no_params(self):
        """Test list_cities returns None when no parameters provided."""
        result = br_locale_info.list_cities()
        assert result is None

    def test_list_cities_invalid_abbr(self):
        """Test list_cities with invalid abbreviation."""
        result = br_locale_info.list_cities(abbr='XX')
        assert result == 'Not found'

    def test_list_cities_invalid_code(self):
        """Test list_cities with invalid code."""
        result = br_locale_info.list_cities(code=999)
        assert result == 'Not found'

    def test_get_city(self):
        """Test get_city method."""
        city = br_locale_info.get_city('São Paulo')
        assert city is not None
        assert city['name'] == 'São Paulo'
        assert city['state'] == 'SP'
        assert 'code' in city

    def test_get_city_case_insensitive(self):
        """Test get_city is case-insensitive."""
        city_lower = br_locale_info.get_city('são paulo')
        city_upper = br_locale_info.get_city('SÃO PAULO')
        city_mixed = br_locale_info.get_city('São Paulo')
        
        assert city_lower == city_upper == city_mixed

    def test_get_city_not_found(self):
        """Test get_city returns None when city not found."""
        result = br_locale_info.get_city('CityDoesNotExist123')
        assert result is None

    def test_get_city_none_param(self):
        """Test get_city returns None when name is None."""
        result = br_locale_info.get_city(None)
        assert result is None

    def test_data_consistency(self):
        """Test that all cities in list_all_cities exist in states."""
        all_cities = br_locale_info.list_all_cities
        for city_name in all_cities:
            city_obj = br_locale_info.get_city(city_name)
            assert city_obj is not None, f"City {city_name} not found via get_city"


def _run_tests():
    import inspect

    all_tests = [
        getattr(TestBrazilLocations(), attr)
        for attr in dir(TestBrazilLocations)
        if attr.startswith('test_')
    ]

    failures = 0
    for test in all_tests:
        try:
            test()
            print(f'✓ {test.__name__}')
        except AssertionError as exc:
            failures += 1
            print(f'✗ {test.__name__}: {exc}')

    if failures:
        raise SystemExit(f'{failures} test(s) failed')


if __name__ == '__main__':
    _run_tests()
