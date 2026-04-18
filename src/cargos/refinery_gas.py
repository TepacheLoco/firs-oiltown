from cargo import Cargo

cargo = Cargo(
    id="refinery_gas",
    type_name="string(STR_CARGO_NAME_REFINERY_GAS)",
    unit_name="string(STR_CARGO_NAME_REFINERY_GAS)",
    type_abbreviation="string(STR_CID_REFINERY_GAS)",
    sprite="NEW_CARGO_SPRITE",
    weight="0.3",
    is_freight="1",
    cargo_classes=["CC_GAS_BULK", "CC_NON_POTABLE"],
    cargo_label="RGAS",
    units_of_cargo="TTD_STR_LITERS",
    items_of_cargo="string(STR_CARGO_UNIT_REFINERY_GAS)",
    penalty_lowerbound="10",
    single_penalty_length="180",
    price_factor=60,
    capacity_multiplier="1",
    icon_indices=(4, 4),
    sprites_complete=False,
)
