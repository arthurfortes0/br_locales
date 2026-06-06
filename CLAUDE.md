# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository contains `br_locales`, a Python library providing Brazilian cities and states data based on IBGE (Brazilian Institute of Geography and Statistics) information. It is a pure-Python package with no runtime dependencies — all data is bundled as a JSON file.

## Commands

**Install for development:**
```bash
pip install -e .
```

**Build distribution:**
```bash
python setup.py sdist bdist_wheel
```

**Run the library interactively:**
```bash
python -c "from br_locales.base import br_locale_info; print(br_locale_info.list_states)"
```

**Bump version before publishing:** update `version` in [setup.py](setup.py).

## Architecture

The entire library is a single module at [br_locales/br_locales/base.py](br_locales/br_locales/base.py). The `BrazilLocations` class loads [br_locales/br_locales/states_and_cities_10_22.json](br_locales/br_locales/states_and_cities_10_22.json) at instantiation and exposes a module-level singleton `br_locale_info`.

The JSON data structure is an `OrderedDict` keyed by state name, where each value has `abbr` (2-letter code), `code` (IBGE integer), `name` (full name), and `cities` (list of objects with `name` and IBGE city code).

Public API surface:
- `br_locale_info.list_states` — sorted list of state abbreviations
- `br_locale_info.list_all_cities` — flat list of all city names across all states
- `br_locale_info.dict_states` — dict mapping abbreviation → `{code, name}`
- `br_locale_info.list_cities(abbr='XX')` / `list_cities(code=NN)` — cities for one state
- `br_locale_info.get_city(name='...')` — find a city object by name (case-insensitive)


## Regras
- Não usar bibliotecas externas sem autorização