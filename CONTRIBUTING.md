# Development Guide

## Setup for Development

1. Clone the repository to a new remote or open your local copy.

2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install in development mode:
   ```bash
   pip install -e .
   ```

4. Install development dependencies (optional):
   ```bash
   pip install flake8
   ```

## Code Quality

### PEP 8 Compliance

The project follows PEP 8 style guidelines. To check code style:

```bash
flake8 br_locales/
```

Configuration is in `.flake8`.

### Type Hints and Documentation

All functions and classes include:
- Docstrings following Google style
- Type hints in docstrings
- Clear parameter and return value documentation

## Testing

Run basic functional tests:

```bash
python3 -c "
from br_locales import br_locale_info

# Verify data integrity
assert len(br_locale_info.list_states) == 27
assert len(br_locale_info.list_all_cities) == 5570
assert br_locale_info.get_city('São Paulo') is not None
print('✅ All basic tests passed!')
"
```

## Building Distribution

```bash
python setup.py sdist bdist_wheel
```

## Releasing

1. Update version in `setup.py` and `__init__.py`
2. Update CHANGELOG if applicable
3. Build distribution
4. Upload to PyPI

## Code Style Notes

- Use meaningful variable names (avoid single letters like `s`, `d`, `u`)
- Use `with` for file operations
- Use `is None` instead of `== None`
- Keep lines under 100 characters (configured in `.flake8`)
- Include docstrings for all public methods and classes
