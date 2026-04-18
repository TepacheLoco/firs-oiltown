from cargo import Cargo

cargo = Cargo(
    id="fracking_fluid",
    type_name="string(STR_CARGO_NAME_FRACKING_FLUID)",
    unit_name="string(STR_CARGO_NAME_FRACKING_FLUID)",
    type_abbreviation="string(STR_CID_FRACKING_FLUID)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.1",
    is_freight="1",
    cargo_classes=["CC_LIQUID_BULK", "CC_PIECE_GOODS", "CC_NON_POTABLE"],
    cargo_label="FFLD",
    units_of_cargo="TTD_STR_LITERS",
    items_of_cargo="string(STR_CARGO_UNIT_FRACKING_FLUID)",
    penalty_lowerbound="16",
    single_penalty_length="200",
    price_factor=180,
    capacity_multiplier="1",
    icon_indices=(15, 5),
    sprites_complete=False,
)
