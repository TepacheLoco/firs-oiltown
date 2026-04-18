from cargo import Cargo

cargo = Cargo(
    id="lng",
    type_name="string(STR_CARGO_NAME_LNG)",
    unit_name="string(STR_CARGO_NAME_LNG)",
    type_abbreviation="string(STR_CID_LNG)",
    sprite="NEW_CARGO_SPRITE",
    weight="0.4",
    is_freight="1",
    cargo_classes=["CC_GAS_BULK", "CC_LIQUID_BULK", "CC_NON_POTABLE"],
    cargo_label="LNG_",
    units_of_cargo="TTD_STR_LITERS",
    items_of_cargo="string(STR_CARGO_UNIT_LNG)",
    penalty_lowerbound="12",
    single_penalty_length="180",
    price_factor=130,
    capacity_multiplier="1",
    icon_indices=(4, 4),
    sprites_complete=False,
)
