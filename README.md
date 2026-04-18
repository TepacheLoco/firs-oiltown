# FIRS OilTown

A fork of [FIRS](https://github.com/andythenorth/firs) building out an oil / petrochemistry–focused OpenTTD economy (`OIL_TOWN`). Based on FIRS 5.2.0. License: GPL v2.

This fork targets a single climate (temperate) and a single economy — everything non-OilTown upstream is left alone but unused.

## Installation

1. Build the grf (see the upstream FIRS docs for build prerequisites — Python 3, `nmlc`).
2. Drop `generated/firs.grf` into your OpenTTD `newgrf` directory (e.g. `Documents/OpenTTD/newgrf/firs-oiltown.grf`).
3. In OpenTTD's NewGRF settings, enable the grf and set the economy parameter to **OilTown** before starting a new game.

## The OilTown supply chain

```
Tier 1  Extraction (primary)
  Offshore Oil Rig      → crude oil (+ pax byproduct)
  Onshore Oil Wells     → crude oil (+ small raw gas)
  Natural Gas Well      → raw gas
  Coal Mine             → coal
  Desalination Plant    → treated water          [coastal]
  Fracking Well         → raw gas + condensate   [requires fracking fluid]

Tier 2  Primary processing
  Oil Refinery          → crude oil (+ condensate, optional)
                        → light oil + heavy oil + naphtha + refinery gas
  Gas Processing Plant  → raw gas
                        → LNG + LPG + sulphur
  Coking Plant          → coal → coke + coal tar

Tier 3  Petrochemistry
  Naphtha Cracking Plant → naphtha + refinery gas → ethylene + chemicals
  Chemical Plant        → ethylene + sulphur + treated water → chemicals
  Fracking Fluid Plant  → chemicals + treated water → fracking fluid

Tier 4  Processing
  Lubricants Plant      → heavy oil + LNG → lubricants
  Bitumen Plant         → heavy oil + coke → bitumen
  Plastics Plant        → ethylene + chemicals → plastics
  Fertiliser Plant      → LNG + sulphur + chemicals → fertiliser
  Petroleum Fuels Depot → light oil + chemicals + lubricants → petroleum fuels
  Engineering Supplies Plant
                        → lubricants + bitumen + coke + ethylene + coal tar
                        → engineering supplies

Tier 5  Sinks
  Oil Trading Port      [coastal] accepts crude / light / heavy oil, petrol, LNG, LPG
  Export Terminal       [coastal] chem + plastics + fert → food (bonus when all 3 supplied)
  Pipeline Terminus     [inland, rare] same acceptance as Oil Trading Port
  Coal Fired Power Station   → coal   [town-adjacent black hole]
  Oil Fired Power Station    → heavy oil
  Natural Gas Power Station  → LNG
  Water Tower           [in-town] accepts treated water (town delivery sink)
```

## Feedback loop

Delivering **engineering supplies** to any tier-1 extractive (coal mine, oil wells, natural gas well, oil rig) boosts its output by ~+40%. This makes the engineering-supplies chain self-reinforcing: more crude / gas / coal flows back into every downstream industry.

Delivering **fracking fluid** to a fracking well is *required* — unlike the other extraction sites, a fracking well with no fluid delivery produces nothing.

Delivering **treated water** to a town water tower contributes to town happiness (same mechanism the Vulcan game script uses for food in other economies).

## Tanker / tank-wagon refits

Raw gas, LNG, LPG, and refinery gas carry both `CC_GAS_BULK` and `CC_LIQUID_BULK`, so tank wagons and tanker trucks (from vehicle sets that refit to either class) can carry them.

## Credits

- Based on FIRS by andythenorth and contributors — see upstream for the full list.
- All sprite art, code, and economy templating is from upstream FIRS. This fork reuses existing FIRS sprite sheets across the new industries rather than producing new art.
