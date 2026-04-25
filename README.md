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
  Offshore Oil Rig      → crude oil (+ pax byproduct)             [from 1947]
  Onshore Oil Wells     → crude oil (+ small raw gas)
  Natural Gas Well      → raw gas
  Coal Mine             → coal
  Desalination Plant    → treated water          [coastal]
  Fracking Well         → raw gas + condensate   [requires fracking fluid; from 1975]

Tier 2  Primary processing
  Oil Refinery          → crude oil OR condensate (either alone yields full production)
                        → light oil + heavy oil + naphtha + refinery gas
  Gas Processing Plant  → raw gas OR refinery gas (either alone yields full production)
                        → LNG + LPG + sulphur (+ a little condensate)
  Coking Plant          → coal → coke + coal tar

Tier 3  Petrochemistry
  Cracking Plant        → naphtha + refinery gas + coal tar → ethylene + chemicals
  Chemical Plant        → ethylene + sulphur + treated water → chemicals    [gated]
  Fracking Fluid Plant  → chemicals + treated water → fracking fluid        [gated, from 1975]

Tier 4  Processing
  Lubricants Plant      → heavy oil + LNG → lubricants                      [gated]
  Bitumen Plant         → heavy oil + coke → bitumen                        [gated]
  Plastics Plant        → ethylene + chemicals → plastics                   [gated]
  Fertiliser Plant      → LNG + sulphur + chemicals → fertiliser            [gated]
  Petroleum Refinery    → light oil + chemicals + lubricants → petrol       [gated]
  Engineering Supplies Plant
                        → lubricants + bitumen + coke + plastics + coal tar
                        → engineering supplies                              [gated]

Tier 5  Exports & town sinks
  Fuel Terminal         [coastal]  accepts crude / light / heavy oil, petrol, LNG, LPG
  Trading Port          [coastal]  accepts chemicals + plastics + fertiliser + bitumen + coal + coke + lubricants → food
  Power Station         [town-adjacent]  accepts coal / heavy oil / LNG
  Water Tower           [in-town]  accepts treated water (drives town happiness)
  Petrol Pump           [in-town]  accepts petrol
  Hotel                 [in-town]  accepts food + treated water
  General Store         [in-town]  accepts food + treated water
```

## Gated secondaries

Industries marked `[gated]` will only produce output when **every** required input has been delivered within the rolling 27-cycle (~3 minute) supply window. Miss one input, and the entire industry stops producing — and visibly stops smoking — until the missing cargo resumes flowing.

While a gated industry is blocked, in-bound cargo is buffered up to 32 units per input rather than consumed, so the truck that completes the set kicks off a real batch of output. The industry window's extra-text alternates between "To resume production, supply all required cargos at least once every three minutes" (blocked) and "To maintain production, …" (running).

## Fluctuating oil markets

Crude oil and 13 downstream cargoes pay a fluctuating per-unit price that drifts up and down over in-game time — a fast cycle (~5.3 years) layered on top of a slow cycle (~16 years). Volatility is tiered by how far down the chain a cargo sits:

| Tier | Volatility | Lag      | Cargoes |
|------|-----------:|---------:|---------|
| 1    |       1.5  |   0 mo   | crude oil |
| 2    |      0.75  |   3 mo   | heavy oil, light oil |
| 3    |       0.5  |   6 mo   | naphtha, condensate, raw gas |
| 4    |      0.25  |   9 mo   | petrol, LNG, LPG, refinery gas, ethylene, bitumen, lubricants |
| 5    |     0.125  |  12 mo   | plastics |

Crude can swing up to ~+22% above its base payment; plastics ~+2%. The lag means refined-product spikes trail upstream spikes, so a crude price boom rolls through the chain over the following year. The standard time-decay penalty for slow deliveries still applies on top.

## Feedback loop

Delivering **engineering supplies** to any tier-1 extractive (coal mine, oil wells, natural gas well, oil rig, desalination plant, fracking well) boosts its output by ~+40%. This makes the engineering-supplies chain self-reinforcing: more crude / gas / coal / water flows back into every downstream industry.

Delivering **fracking fluid** to a fracking well is *required* — unlike the other extraction sites, a fracking well with no fluid delivery produces nothing.

Delivering **treated water** to a town water tower contributes to town happiness (same mechanism the Vulcan game script uses for food in other economies).

## Tanker / tank-wagon refits

Raw gas, LNG, LPG, and refinery gas carry both `CC_GAS_BULK` and `CC_LIQUID_BULK`, so tank wagons and tanker trucks (from vehicle sets that refit to either class) can carry them.

## Credits

- Based on FIRS by andythenorth and contributors — see upstream for the full list.
- All sprite art, code, and economy templating is from upstream FIRS. This fork reuses existing FIRS sprite sheets across the new industries rather than producing new art.
