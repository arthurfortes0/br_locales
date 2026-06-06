# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.0.91] - 2026-06-05

### Added
- Comprehensive module-level docstring
- Detailed docstrings for all classes and methods following Google style
- Type hints in docstring format
- `.flake8` configuration file for code quality standards
- `CONTRIBUTING.md` guide for developers
- `.gitignore` with Python standard patterns
- `tests.py` with comprehensive test suite
- `CHANGELOG.md` for release tracking

### Changed
- **BREAKING**: Import path simplified from `br_locales.base import br_locale_info` to `br_locales import br_locale_info`
- Refactored `base.py` for PEP 8 compliance:
  - Replaced single-letter variable names (`s`, `d`, `u`) with descriptive names
  - Used `with` statement for file operations
  - Changed `!= None` to `is not None` (PEP 8 convention)
  - Improved code formatting and spacing
  - Removed unused variable `this_filename`
  - Removed unused private method `_get_state_by_abbr()`
- Updated `setup.py`:
  - Added `long_description` from README
  - Added `long_description_content_type`
  - Added Python version requirement (`python_requires='>=3.6'`)
  - Added `classifiers` for better PyPI metadata
  - Expanded `keywords` list
  - Added module-level docstring
- Enhanced `README.rst`:
  - Completely restructured for clarity and modern formatting
  - Added badges for Python version and license
  - Improved code examples with proper formatting
  - Added comprehensive API reference section
  - Added "Data Source" section
  - Updated metadata (version, author info)
- Created `__init__.py` with:
  - Module docstring
  - Proper exports of public API
  - Version information
  - `__all__` definition for explicit public interface

### Fixed
- Incorrect handling of return values in `list_cities()` - now properly returns `None` instead of empty response
- Resource handling: file objects now properly closed via context manager
- UTF-8 encoding explicitly specified for JSON file loading

### Improved
- Code readability and maintainability
- Documentation quality for IDE integration and code completion
- Package metadata for better discoverability on PyPI
- Developer experience with contribution guidelines

### Technical Details
- Data verified: 27 states/federal entities, 5,570 municipalities
- All data from IBGE with municipalities through 2022
- No breaking changes to functionality, only import path
- Full backward compatibility with exception of import statement

## [0.0.90] - Previous Release
- Initial release with basic functionality
