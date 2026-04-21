from cargo import Cargo

cargo = Cargo(
    id="ethylene",
    type_name="string(STR_CARGO_NAME_ETHYLENE)",
    unit_name="string(STR_CARGO_NAME_ETHYLENE)",
    type_abbreviation="string(STR_CID_ETHYLENE)",
    sprite="NEW_CARGO_SPRITE",
    weight="0.6",
    is_freight="1",
    cargo_classes=["CC_GAS_BULK", "CC_LIQUID_BULK", "CC_NON_POTABLE"],
    cargo_label="ETHY",
    units_of_cargo="TTD_STR_LITERS",
    items_of_cargo="string(STR_CARGO_UNIT_ETHYLENE)",
    penalty_lowerbound="5",
    single_penalty_length="20",
    price_factor=118,
    capacity_multiplier="1",
    icon_indices=(1, 7),
    sprites_complete=True,
)
