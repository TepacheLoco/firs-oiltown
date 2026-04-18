from cargo import Cargo

cargo = Cargo(
    id="treated_water",
    type_name="string(STR_CARGO_NAME_TREATED_WATER)",
    unit_name="string(STR_CARGO_NAME_TREATED_WATER)",
    type_abbreviation="string(STR_CID_TREATED_WATER)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes=["CC_LIQUID_BULK", "CC_PIECE_GOODS", "CC_POTABLE"],
    cargo_label="WATR",
    units_of_cargo="TTD_STR_LITERS",
    items_of_cargo="string(STR_CARGO_UNIT_TREATED_WATER)",
    penalty_lowerbound="20",
    single_penalty_length="255",
    price_factor=80,
    capacity_multiplier="1",
    icon_indices=(7, 1),
    vulcan_town_effect="VTE_HAPPINESS",
    sprites_complete=False,
)
