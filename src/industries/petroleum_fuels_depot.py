from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="petroleum_fuels_depot",
    accept_cargos_with_input_ratios=[
        ("LOIL", 5),
        ("CHEM", 2),
        ("LUBR", 1),
    ],
    prod_cargo_types_with_output_ratios=[],
    prob_in_game="3",
    prob_map_gen="5",
    map_colour="191",
    colour_scheme_name="scheme_1_elton",
    special_flags=["IND_FLAG_MILITARY_AIRPLANE_CAN_EXPLODE"],
    fund_cost_multiplier="180",
    name="string(STR_IND_PETROLEUM_FUELS_DEPOT)",
    nearby_station_name="string(STR_STATION_PETROLEUM_FUELS_DEPOT)",
    location_checks=dict(
        near_at_least_one_of_these_keystone_industries=[["oil_refinery"], 96],
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
    prod_cargo_types_with_output_ratios=[("PETR", 8)],
    require_all_inputs_for_production=True,
)

industry.add_tile(
    id="petroleum_fuels_depot_tile_1",
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
    id="petroleum_fuels_depot_spritelayout_1",
    tile="petroleum_fuels_depot_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_1],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="petroleum_fuels_depot_spritelayout_2",
    tile="petroleum_fuels_depot_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_2],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="petroleum_fuels_depot_spritelayout_3",
    tile="petroleum_fuels_depot_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_3],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="petroleum_fuels_depot_spritelayout_4",
    tile="petroleum_fuels_depot_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_4],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="petroleum_fuels_depot_spritelayout_5",
    tile="petroleum_fuels_depot_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_5],
    fences=["nw", "ne", "se", "sw"],
)

industry.add_industry_layout(
    id="petroleum_fuels_depot_industry_layout_1",
    layout=[
        (0, 0, "petroleum_fuels_depot_spritelayout_2"),
        (0, 1, "petroleum_fuels_depot_spritelayout_3"),
        (0, 2, "petroleum_fuels_depot_spritelayout_3"),
        (1, 0, "petroleum_fuels_depot_spritelayout_2"),
        (1, 1, "petroleum_fuels_depot_spritelayout_4"),
        (1, 2, "petroleum_fuels_depot_spritelayout_5"),
        (2, 0, "petroleum_fuels_depot_spritelayout_1"),
        (2, 1, "petroleum_fuels_depot_spritelayout_1"),
        (2, 2, "petroleum_fuels_depot_spritelayout_1"),
    ],
)
industry.add_industry_layout(
    id="petroleum_fuels_depot_industry_layout_2",
    layout=[
        (0, 0, "petroleum_fuels_depot_spritelayout_2"),
        (0, 1, "petroleum_fuels_depot_spritelayout_4"),
        (1, 0, "petroleum_fuels_depot_spritelayout_3"),
        (1, 1, "petroleum_fuels_depot_spritelayout_5"),
        (2, 0, "petroleum_fuels_depot_spritelayout_1"),
        (2, 1, "petroleum_fuels_depot_spritelayout_1"),
        (3, 0, "petroleum_fuels_depot_spritelayout_1"),
        (3, 1, "petroleum_fuels_depot_spritelayout_1"),
    ],
)
