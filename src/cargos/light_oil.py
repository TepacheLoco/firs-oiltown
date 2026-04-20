from cargo import Cargo

cargo = Cargo(
    id="light_oil",
    type_name="string(STR_CARGO_NAME_LIGHT_OIL)",
    unit_name="string(STR_CARGO_NAME_LIGHT_OIL)",
    type_abbreviation="string(STR_CID_LIGHT_OIL)",
    sprite="NEW_CARGO_SPRITE",
    weight="0.8",
    is_freight="1",
    cargo_classes=["CC_LIQUID_BULK", "CC_NON_POTABLE"],
    cargo_label="LOIL",
    units_of_cargo="TTD_STR_LITERS",
    items_of_cargo="string(STR_CARGO_UNIT_LIGHT_OIL)",
    penalty_lowerbound="15",
    single_penalty_length="75",
    price_factor=108,
    capacity_multiplier="1",
    icon_indices=(12, 1),
    sprites_complete=False,
)
