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
- `petrochemical_plant.py` — secondary: naphtha + refinery gas + coal tar → ethylene + chemicals (reuses `copper_smelter.png`). Display name "Cracking Plant"
- `fracking_well.py` — secondary: fracking fluid → raw gas + condensate (reuses `oil_wells.png`)
- `fracking_fluid_plant.py` — secondary: chemicals + treated water → fracking fluid (reuses `tyre_plant.png`)
- `lubricants_plant.py` — secondary: heavy oil + LNG → lubricants (reuses `oil_refinery.png`)
- `bitumen_plant.py` — secondary: heavy oil + coke → bitumen (reuses `lime_kiln.png`)
- `petroleum_fuels_depot.py` — secondary: light oil + chemicals + lubricants → petrol (reuses `oil_refinery.png`)
- `export_terminal.py` — coastal primary port: chemicals + plastics + fertiliser + bitumen + coal + coke + lubricants → food (reuses `port.png`). Display name "Trading Port"
- `power_station.py` — tertiary town sink; accepts coal, heavy oil, or LNG (built-in OpenTTD power-plant sprites)
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
- `natural_gas_well.py` — swapped building visual: monkey-patched graphics path to `oil_refinery.png` and changed `spriteset_building` coords to oil_refinery's sprite_1. Pumps still use built-in OpenTTD sprites.

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
  - `STR_IND_PETROCHEMICAL_PLANT`: "Petrochemical Plant" → "Cracking Plant"
  - `STR_IND_EXPORT_TERMINAL`: "Export Terminal" → "Trading Port"
  - `STR_IND_OIL_TRADING_PORT`: "Oil Trading Port" → "Fuel Terminal"
  - `STR_IND_PETROLEUM_FUELS_DEPOT`: "Petroleum Fuels Depot" → "Petroleum Refinery"
- Added `STR_STATION_FERTILISER_PLANT` (was missing)

### Notes

- The FIRS code already supported monkey-patching `industry.get_graphics_file_path` to reuse another industry's PNG. This fork leans heavily on that technique rather than producing new sprite art — see the sprite-sheet attribution notes on each new industry above.
- No changes to the upstream FIRS build system, NML templates, or Game Script other than adding economy data.


## 2026-04-21 — OilTown 5.2.0.2

### Visual: secondary industries go dormant when not producing

- **`src/global_constants.py`** — added graphics temp register `var_production_gate_closed=21`.
- **`src/grf/templates/graphics_switches.pynml`** — for every secondary industry (`industry.template == 'industry_secondary.pynml'`), emit a `FEAT_INDUSTRYTILES, PARENT` switch `<industry>_switch_production_gate_closed` that returns `(LOAD_PERM(current_production_ratio) == 0)`. Its result is stored into temp register 21 at the top of `<industry>_switch_graphics`. The same signal covers both semantics: for `require_all_inputs_for_production` economies the hard gate in `produce_secondary.pynml` forces the ratio to 0 when any input is missing; for ungated secondaries the ratio is 0 whenever no accepted cargo has been delivered in the rolling 27-cycle window.
- **`src/grf/templates/spritelayouts_industry.pynml`** — the smoke building block's `hide_sprite` now ORs `LOAD_TEMP(21)` with the existing per-smoke-type expression, so smoke/fire sprites hide while the production gate is closed. Harmless for primary/tertiary industries (register is never written; `LOAD_TEMP` defaults to 0).
- Affects every secondary with smoke — notably the four OIL_TOWN gated secondaries that declare smoke today (bitumen_plant 3 plumes, chemical_plant 9, fertiliser_plant 9, fracking_fluid_plant 2), plus every other secondary across all economies that has smoke_sprites. Ungated secondaries now also stop smoking if no input has arrived in ~3 minutes.

### Cargo icons

- Added a new row of 10 fresh icons in `src/graphics/cargoicons.png` at row 7 and re-pointed 10 fork cargoes so they no longer share placeholder art: treated_water (0,7), ethylene (1,7), fracking_fluid (2,7), heavy_oil (3,7), light_oil (4,7), condensate (5,7), raw_gas (6,7), lng (7,7), lpg (8,7), refinery_gas (9,7). Flipped `sprites_complete=True` on all ten. Cleared animated palette index 228 from the heavy_oil and raw_gas tiles.


## 2026-04-20 — OilTown 5.2.0.1

### New gameplay: "all inputs required" secondary industries

- **`src/industry.py`** — added `require_all_inputs_for_production` property on `IndustryProperties`. When set on a secondary industry (per-economy), production is gated: the ratio stores zero unless every input's `supplied_cycles_remaining_cargo_N` register is > 0.
- **`src/grf/templates/produce_secondary.pynml`** — emits a chained-ternary gate after the existing ratio accumulator; emits conditional consumption in the `produce` callback so gated industries buffer up to 32 units per input while blocked (cargo above the cap is wasted), letting the truck that completes the set feed a real batch of output.
- **`src/grf/templates/extra_text_secondary.pynml`** — per-gated-economy sub-switch picks "resume" vs "maintain" text from runtime supplied-cycle state.
- **`src/grf/lang/english.toml`** — added `STR_EXTRA_TEXT_SECONDARY_GATED_BOTH`, `STR_EXTRA_TEXT_SECONDARY_GATED_ALL`, `STR_EXTRA_TEXT_SECONDARY_MAINTAIN_BOTH`, `STR_EXTRA_TEXT_SECONDARY_MAINTAIN_ALL`.
- Flag set in the OIL_TOWN economy variation for: `bitumen_plant`, `chemical_plant`, `fertiliser_plant`, `fracking_fluid_plant`, `lubricants_plant`, `petroleum_fuels_depot`, `plastics_plant`, `supply_yard`. Oil refinery and cracking plant deliberately left linear.

### Cargo payment-curve retuning (OIL_TOWN)

Three-tier spread applied across all OIL_TOWN cargos in `src/cargos/*.py`:

- **Stable** (`penalty_lowerbound=50, single_penalty_length=255`): oil, condensate, heavy_oil, sulphur, coke, coal_tar, treated_water, fertiliser, engineering_supplies, bitumen, plastics.
- **Medium** (`15, 75`): light_oil, raw_gas, refinery_gas, lng, lpg, lubricants, fracking_fluid, petrol, chemicals.
- **Volatile** (`5, 20`): ethylene, naphtha.

`price_factor` adjusted where the curve change shifted expected payout substantially: engineering_supplies 178→115, plastics 133→105, bitumen 110→90, fertiliser 123→105, naphtha 103→130.

### Industry behaviour

- **`src/industries/oil_trading_port.py`** (Fuel Terminal) — reclassified from `IndustryPrimaryPort` to `IndustryTertiary`. Pure sink, no production multipliers, no return cargo. Accepts crude, light oil, heavy oil, petrol, LNG, LPG.
- **`src/industries/desalination_plant.py`** — reclassified from `IndustryPrimaryPort` to `IndustryPrimaryExtractive` so ENSP deliveries drive the standard supply-requirements production boost. Auto-accepts ENSP via the base class.
- **`src/industries/oil_refinery.py`** — OIL_TOWN economy variation accepts crude oil and condensate as alternative inputs at 8/8 ratios each (either alone yields full production); explicitly not gated.
- **`src/industries/petrol_pump.py`** — added OIL_TOWN economy variation, accepts `PETR` only. In-town tertiary sink.
- **`src/industries/supply_yard.py`** — OIL_TOWN recipe updated: swapped `ETHY` for `PLAS` (ratios unchanged; sum still 8).
- **`src/industries/gas_processing_plant.py`** — added `("RGAS", 8)` alongside `("NGAS", 8)` as alternative feedstock. Either alone caps the ratio at 8 → full production (same pattern as Oil Refinery's OIL_/COND).

### Cargo classes

- **`src/cargos/sulphur.py`** — restored `CC_COVERED_BULK` alongside `CC_OPEN_BULK` and `CC_NON_POTABLE` so covered-hopper bulk trucks refit to sulphur.
