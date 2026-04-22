from cargo import Cargo

cargo = Cargo(
    id="bitumen",
    type_name="string(STR_CARGO_NAME_BITUMEN)",
    unit_name="string(STR_CARGO_NAME_BITUMEN)",
    type_abbreviation="string(STR_CID_BITUMEN)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes=["CC_LIQUID_BULK", "CC_PIECE_GOODS", "CC_NON_POTABLE"],
    cargo_label="BITU",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_BITUMEN)",
    penalty_lowerbound="50",
    single_penalty_length="255",
    price_factor=90,
    capacity_multiplier="1",
    icon_indices=(1, 3),
    sprites_complete=True,
)
