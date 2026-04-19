from cargo import Cargo

cargo = Cargo(
    id="lubricants",
    type_name="string(STR_CARGO_NAME_LUBRICANTS)",
    unit_name="string(STR_CARGO_NAME_LUBRICANTS)",
    type_abbreviation="string(STR_CID_LUBRICANTS)",
    sprite="NEW_CARGO_SPRITE",
    weight="0.9",
    is_freight="1",
    cargo_classes=["CC_LIQUID_BULK", "CC_PIECE_GOODS", "CC_NON_POTABLE"],
    cargo_label="LUBR",
    units_of_cargo="TTD_STR_LITERS",
    items_of_cargo="string(STR_CARGO_UNIT_LUBRICANTS)",
    penalty_lowerbound="10",
    single_penalty_length="22",
    price_factor=122,
    capacity_multiplier="1",
    icon_indices=(13, 1),
    sprites_complete=False,
)
