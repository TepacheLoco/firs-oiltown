from cargo import Cargo

cargo = Cargo(
    id="oil",
    type_name="string(STR_CARGO_NAME_CRUDE_OIL)",
    unit_name="string(STR_CARGO_NAME_CRUDE_OIL)",
    type_abbreviation="string(STR_CID_CRUDE_OIL)",
    sprite="NEW_CARGO_SPRITE",
    weight="0.9",
    is_freight="1",
    cargo_classes = ["CC_LIQUID_BULK", "CC_NON_POTABLE"],
    cargo_label="OIL_",
    units_of_cargo="TTD_STR_LITERS",
    items_of_cargo="string(STR_CARGO_UNIT_CRUDE_OIL)",
    penalty_lowerbound="50",
    single_penalty_length="255",
    price_factor=101,
    capacity_multiplier="1",
    icon_indices=(3, 0),
    sprites_complete=True,
    market_volatility=1.5,
)
