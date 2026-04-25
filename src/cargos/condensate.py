from cargo import Cargo

cargo = Cargo(
    id="condensate",
    type_name="string(STR_CARGO_NAME_CONDENSATE)",
    unit_name="string(STR_CARGO_NAME_CONDENSATE)",
    type_abbreviation="string(STR_CID_CONDENSATE)",
    sprite="NEW_CARGO_SPRITE",
    weight="0.7",
    is_freight="1",
    cargo_classes=["CC_LIQUID_BULK", "CC_PIECE_GOODS", "CC_NON_POTABLE"],
    cargo_label="COND",
    units_of_cargo="TTD_STR_LITERS",
    items_of_cargo="string(STR_CARGO_UNIT_CONDENSATE)",
    penalty_lowerbound="50",
    single_penalty_length="255",
    price_factor=95,
    capacity_multiplier="1",
    icon_indices=(5, 7),
    sprites_complete=True,
    market_volatility=0.5,
    market_lag_months=6,
)
