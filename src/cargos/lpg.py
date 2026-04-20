from cargo import Cargo

cargo = Cargo(
    id="lpg",
    type_name="string(STR_CARGO_NAME_LPG)",
    unit_name="string(STR_CARGO_NAME_LPG)",
    type_abbreviation="string(STR_CID_LPG)",
    sprite="NEW_CARGO_SPRITE",
    weight="0.5",
    is_freight="1",
    cargo_classes=["CC_GAS_BULK", "CC_LIQUID_BULK", "CC_NON_POTABLE"],
    cargo_label="LPG_",
    units_of_cargo="TTD_STR_LITERS",
    items_of_cargo="string(STR_CARGO_UNIT_LPG)",
    penalty_lowerbound="15",
    single_penalty_length="75",
    price_factor=120,
    capacity_multiplier="1",
    icon_indices=(4, 4),
    sprites_complete=False,
)
