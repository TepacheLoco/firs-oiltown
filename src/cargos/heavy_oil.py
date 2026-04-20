from cargo import Cargo

cargo = Cargo(
    id="heavy_oil",
    type_name="string(STR_CARGO_NAME_HEAVY_OIL)",
    unit_name="string(STR_CARGO_NAME_HEAVY_OIL)",
    type_abbreviation="string(STR_CID_HEAVY_OIL)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes=["CC_LIQUID_BULK", "CC_NON_POTABLE"],
    cargo_label="HOIL",
    units_of_cargo="TTD_STR_LITERS",
    items_of_cargo="string(STR_CARGO_UNIT_HEAVY_OIL)",
    penalty_lowerbound="50",
    single_penalty_length="255",
    price_factor=90,
    capacity_multiplier="1",
    icon_indices=(3, 0),
    sprites_complete=False,
)
