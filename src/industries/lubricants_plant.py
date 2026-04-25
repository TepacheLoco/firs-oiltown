from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="lubricants_plant",
    accept_cargos_with_input_ratios=[
        ("HOIL", 5),
        ("LNG_", 3),
    ],
    prod_cargo_types_with_output_ratios=[],
    prob_in_game="3",
    prob_map_gen="5",
    map_colour="191",
    colour_scheme_name="scheme_1_elton",
    special_flags=["IND_FLAG_MILITARY_AIRPLANE_CAN_EXPLODE"],
    fund_cost_multiplier="180",
    name="string(STR_IND_LUBRICANTS_PLANT)",
    nearby_station_name="string(STR_STATION_LUBRICANTS_PLANT)",
    location_checks=dict(
        same_type_distance=96,
    ),
    sprites_complete=True,
    animated_tiles_fixed=False,
)


def _reuse_oil_refinery_graphics(terrain=None, construction_state_num=None):
    return '"src/graphics/industries/oil_refinery.png"'


industry.get_graphics_file_path = _reuse_oil_refinery_graphics

industry.enable_in_economy(
    "OIL_TOWN",
    prob_in_game="1",
    prob_map_gen="2",
    prod_cargo_types_with_output_ratios=[("LUBR", 8)],
    require_all_inputs_for_production=True,
)

industry.add_tile(
    id="lubricants_plant_tile_1",
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

spriteset_ground = industry.add_spriteset(
    type="asphalt",
)
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 66, -31, -35)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 10, 64, 128, -31, -96)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 10, 64, 128, -31, -96)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 10, 64, 128, -31, -96)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(290, 10, 64, 66, -31, -35)],
)

industry.add_spritelayout(
    id="lubricants_plant_spritelayout_1",
    tile="lubricants_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_1],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="lubricants_plant_spritelayout_2",
    tile="lubricants_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_2],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="lubricants_plant_spritelayout_3",
    tile="lubricants_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_3],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="lubricants_plant_spritelayout_4",
    tile="lubricants_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_4],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="lubricants_plant_spritelayout_5",
    tile="lubricants_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_5],
    fences=["nw", "ne", "se", "sw"],
)

industry.add_industry_layout(
    id="lubricants_plant_industry_layout_1",
    layout=[
        (0, 0, "lubricants_plant_spritelayout_1"),
        (0, 1, "lubricants_plant_spritelayout_1"),
        (0, 2, "lubricants_plant_spritelayout_3"),
        (0, 3, "lubricants_plant_spritelayout_2"),
        (1, 0, "lubricants_plant_spritelayout_1"),
        (1, 1, "lubricants_plant_spritelayout_4"),
        (1, 2, "lubricants_plant_spritelayout_3"),
        (1, 3, "lubricants_plant_spritelayout_5"),
        (2, 0, "lubricants_plant_spritelayout_1"),
        (2, 1, "lubricants_plant_spritelayout_4"),
        (2, 2, "lubricants_plant_spritelayout_2"),
        (2, 3, "lubricants_plant_spritelayout_5"),
    ],
)
industry.add_industry_layout(
    id="lubricants_plant_industry_layout_2",
    layout=[
        (0, 0, "lubricants_plant_spritelayout_2"),
        (0, 1, "lubricants_plant_spritelayout_3"),
        (0, 2, "lubricants_plant_spritelayout_4"),
        (1, 0, "lubricants_plant_spritelayout_2"),
        (1, 1, "lubricants_plant_spritelayout_4"),
        (1, 2, "lubricants_plant_spritelayout_2"),
        (2, 0, "lubricants_plant_spritelayout_5"),
        (2, 1, "lubricants_plant_spritelayout_1"),
        (2, 2, "lubricants_plant_spritelayout_1"),
        (3, 1, "lubricants_plant_spritelayout_5"),
        (3, 2, "lubricants_plant_spritelayout_1"),
    ],
)
