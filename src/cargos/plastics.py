from cargo import Cargo

cargo = Cargo(
    id="plastics",
    type_name="string(STR_CARGO_NAME_PLASTICS)",
    unit_name="string(STR_CARGO_NAME_PLASTICS)",
    type_abbreviation="string(STR_CID_PLASTICS)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_PIECE_GOODS", "CC_COVERED_BULK", "CC_NON_POTABLE"],
    cargo_label="PLAS",
    units_of_cargo="TTD_STR_LITERS",
    items_of_cargo="string(STR_CARGO_UNIT_PLASTICS)",
    penalty_lowerbound="50",
    single_penalty_length="255",
    capacity_multiplier="1",
    price_factor=105,
    icon_indices=(6, 4),
    sprites_complete=True,
    market_volatility=0.125,
    market_lag_months=12,
)
