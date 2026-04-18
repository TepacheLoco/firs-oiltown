# Changes from upstream FIRS

This file records changes made to [upstream FIRS](https://github.com/andythenorth/firs) in this fork (OilTown). Required by GPL v2 §2(a): modified versions must carry prominent notices stating what was changed and the date of change.

Entries are chronological. When modifying an upstream file for the first time, add it here with a short description. Further edits to the same file don't need new entries unless the purpose of the change is different.

## 2026-04-18 — OilTown 0.1

Fork started from FIRS 5.2.0. Target: single-economy (`OIL_TOWN`), single-climate (temperate), oil / petrochemistry focus.

### New files

**Cargos (`src/cargos/`):**
- `treated_water.py` — potable liquid bulk, town-happiness effect
- `ethylene.py` — petrochemical liquid bulk
- `condensate.py` — natural-gas-liquid feedstock
- `lubricants.py`, `bitumen.py`, `fracking_fluid.py` — liquid bulk intermediates

**Industries (`src/industries/`):**
- `desalination_plant.py` — coastal primary, produces treated water (reuses `oil_trading_port.png`)
- `coking_plant.py` — secondary: coal → coke + coal tar (reuses `coke_oven.png`)
- `petrochemical_plant.py` — secondary: naphtha + refinery gas → ethylene + chemicals (reuses `copper_smelter.png`). Display name "Naphtha Cracking Plant"
- `fracking_well.py` — secondary: fracking fluid → raw gas + condensate (reuses `oil_wells.png`)
- `fracking_fluid_plant.py` — secondary: chemicals + treated water → fracking fluid (reuses `tyre_plant.png`)
- `lubricants_plant.py` — secondary: heavy oil + LNG → lubricants (reuses `oil_refinery.png`)
- `bitumen_plant.py` — secondary: heavy oil + coke → bitumen (reuses `lime_kiln.png`)
- `petroleum_fuels_depot.py` — secondary: light oil + chemicals + lubricants → petrol (reuses `oil_refinery.png`)
- `export_terminal.py` — coastal primary port: chemicals + plastics + fertiliser → food (reuses `oil_trading_port.png`)
- `gas_pipeline_terminus.py` — inland black-hole tertiary; display name "Pipeline Terminus" (reuses `gas_processing_plant.png`)
- `coal_power_station.py`, `oil_power_station.py`, `gas_power_station.py` — tertiary town sinks (built-in OpenTTD power-plant sprites)
- `water_tower.py` — in-town tertiary; accepts treated water (reuses `oil_trading_port.png` sphere-tank sprite)

**Root:**
- `README.md` — fork readme with supply-chain diagram
- `CHANGES.md` — this file

### Modified upstream files

**`src/cargos/`**
- `lng.py`, `lpg.py`, `raw_gas.py`, `refinery_gas.py` — added `CC_LIQUID_BULK` to `cargo_classes` so tanker vehicles (not just gas-class vehicles) refit to these cargos
- `__init__.py` — registered new cargos; additionally registered `phosphoric_acid` and `plastics` (upstream cargo files that were unreferenced)

**`src/industries/`**
- `__init__.py` — registered all new industries; additionally registered `plastics_plant` and `fertiliser_plant` (upstream industry files that were unreferenced in the module list)
- `oil_trading_port.py` — in OIL_TOWN, expanded `accept_cargo_types` from `[OIL_, LOIL, HOIL]` to include `PETR`, `LNG_`, `LPG_`
- `oil_refinery.py` — added OIL_TOWN economy variation accepting both `OIL_` and `COND` as alternative feedstocks (either alone yields full production)
- `chemical_plant.py` — added OIL_TOWN economy variation: `ETHY` + `SULP` + `WATR` → `CHEM`
- `plastics_plant.py` — enabled in OIL_TOWN (`ETHY` + `CHEM` → `PLAS`); fixed legacy file so spritelayouts meet the post-2022 `tile=` requirement (upstream file was orphaned / not imported); changed base-economy accept from `C2H4` to `ETHY` (C2H4 label is from a removed cargo)
- `fertiliser_plant.py` — enabled in OIL_TOWN (`LNG_` + `SULP` + `CHEM` → `FERT`); fixed legacy file so spritelayouts have `tile=` kwarg; set `nearby_station_name` (was commented out)
- `supply_yard.py` — enabled in OIL_TOWN with a new recipe: `LUBR` + `BITU` + `COKE` + `ETHY` + `CTAR` → `ENSP`

**`src/economies/oil_town.py`**
- Expanded economy `cargos` list to include every new/used cargo in OIL_TOWN (bitumen, chemicals, coal_tar, coke, condensate, engineering_supplies, ethylene, fertiliser, food, fracking_fluid, lubricants, mail, petrol, plastics, treated_water, and the previously-existing oil chain cargos)

**`src/global_constants.py`**
- Added numeric IDs for all new industries (in previously unused slots). Activated previously-commented `plastics_plant=18` and `fertiliser_plant=106`
- Added tile numeric IDs for new industries

**`src/grf/lang/english.toml`**
- Added strings for all new cargos (name, unit, CID abbreviation) and new industries (name + station name)
- Renamed display strings (internal IDs unchanged):
  - `STR_IND_PLASTICS_PLANT`: "PVC Plant" → "Plastics Plant"
  - `STR_IND_SUPPLY_YARD`: "Supply Yard" → "Engineering Supplies Plant"
  - `STR_IND_GAS_PIPELINE_TERMINUS`: "Gas Pipeline Terminus" → "Pipeline Terminus"
  - `STR_IND_PETROCHEMICAL_PLANT`: "Petrochemical Plant" → "Naphtha Cracking Plant"
- Added `STR_STATION_FERTILISER_PLANT` (was missing)

### Notes

- The FIRS code already supported monkey-patching `industry.get_graphics_file_path` to reuse another industry's PNG. This fork leans heavily on that technique rather than producing new sprite art — see the sprite-sheet attribution notes on each new industry above.
- No changes to the upstream FIRS build system, NML templates, or Game Script other than adding economy data.
