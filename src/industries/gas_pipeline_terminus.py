from industry import IndustryTertiary, TileLocationChecks

industry = IndustryTertiary(
    id="gas_pipeline_terminus",
    accept_cargo_types=["OIL_", "LOIL", "HOIL", "PETR", "LNG_", "LPG_"],
    prod_cargo_types=[],
    prob_in_game="1",
    prob_map_gen="2",
    prod_multiplier="[0, 0]",
    map_colour="168",
    colour_scheme_name="scheme_1_elton",
    life_type="IND_LIFE_TYPE_BLACK_HOLE",
    town_industry_for_cargoflow=False,
    special_flags=["IND_FLAG_MILITARY_AIRPLANE_CAN_EXPLODE"],
    prospect_chance="0.75",
    location_checks=dict(same_type_distance=64),
    name="string(STR_IND_GAS_PIPELINE_TERMINUS)",
    nearby_station_name="string(STR_STATION_GAS_PIPELINE_TERMINUS)",
    fund_cost_multiplier="170",
    sprites_complete=True,
    animated_tiles_fixed=True,
)


def _reuse_gas_processing_plant_graphics(terrain=None, construction_state_num=None):
    return '"src/graphics/industries/gas_processing_plant.png"'


industry.get_graphics_file_path = _reuse_gas_processing_plant_graphics

industry.enable_in_economy("OIL_TOWN")

industry.add_tile(
    id="gas_pipeline_terminus_tile_1",
    animation_length=7,
    animation_looping=True,
    animation_speed=3,
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

spriteset_ground = industry.add_spriteset(
    type="asphalt",
)
spriteset_1 = industry.add_spriteset(
    sprites=[(500, 10, 64, 66, -31, -35)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(570, 10, 64, 66, -31, -35)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(710, 10, 64, 66, -31, -35)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(80, 10, 64, 88, -31, -58)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(150, 10, 64, 88, -31, -59)],
)
spriteset_6 = industry.add_spriteset(
    sprites=[(220, 10, 64, 88, -31, -64)],
)
spriteset_7 = industry.add_spriteset(
    sprites=[(360, 10, 64, 73, -31, -45)],
)
spriteset_8 = industry.add_spriteset(
    sprites=[(430, 10, 64, 66, -31, -38)],
)
sprite_smoke_1 = industry.add_smoke_sprite(
    smoke_type="white_smoke_big",
    xoffset=1,
    yoffset=0,
    zoffset=62,
    animation_frame_offset=1,
)
sprite_smoke_2 = industry.add_smoke_sprite(
    smoke_type="white_smoke_big", xoffset=1, yoffset=-3, zoffset=62
)

industry.add_spritelayout(
    id="gas_pipeline_terminus_spritelayout_1",
    tile="gas_pipeline_terminus_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_1],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="gas_pipeline_terminus_spritelayout_2",
    tile="gas_pipeline_terminus_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_2],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="gas_pipeline_terminus_spritelayout_3",
    tile="gas_pipeline_terminus_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_3],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="gas_pipeline_terminus_spritelayout_4",
    tile="gas_pipeline_terminus_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_4],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="gas_pipeline_terminus_spritelayout_5",
    tile="gas_pipeline_terminus_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_5],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="gas_pipeline_terminus_spritelayout_6_anim",
    tile="gas_pipeline_terminus_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_6],
    smoke_sprites=[sprite_smoke_2, sprite_smoke_1],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="gas_pipeline_terminus_spritelayout_7",
    tile="gas_pipeline_terminus_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_7],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="gas_pipeline_terminus_spritelayout_8",
    tile="gas_pipeline_terminus_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_8],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="gas_pipeline_terminus_spritelayout_empty",
    tile="gas_pipeline_terminus_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[],
    fences=["nw", "ne", "se", "sw"],
)

industry.add_industry_layout(
    id="gas_pipeline_terminus_industry_layout_1",
    layout=[
        (0, 0, "gas_pipeline_terminus_spritelayout_empty"),
        (0, 1, "gas_pipeline_terminus_spritelayout_2"),
        (0, 2, "gas_pipeline_terminus_spritelayout_1"),
        (1, 0, "gas_pipeline_terminus_spritelayout_8"),
        (1, 1, "gas_pipeline_terminus_spritelayout_4"),
        (1, 2, "gas_pipeline_terminus_spritelayout_5"),
        (2, 0, "gas_pipeline_terminus_spritelayout_7"),
        (2, 1, "gas_pipeline_terminus_spritelayout_6_anim"),
        (2, 2, "gas_pipeline_terminus_spritelayout_3"),
    ],
)
industry.add_industry_layout(
    id="gas_pipeline_terminus_industry_layout_2",
    layout=[
        (0, 0, "gas_pipeline_terminus_spritelayout_8"),
        (0, 1, "gas_pipeline_terminus_spritelayout_4"),
        (0, 2, "gas_pipeline_terminus_spritelayout_5"),
        (0, 3, "gas_pipeline_terminus_spritelayout_6_anim"),
        (1, 0, "gas_pipeline_terminus_spritelayout_7"),
        (1, 1, "gas_pipeline_terminus_spritelayout_empty"),
        (1, 2, "gas_pipeline_terminus_spritelayout_3"),
        (1, 3, "gas_pipeline_terminus_spritelayout_1"),
        (2, 0, "gas_pipeline_terminus_spritelayout_empty"),
        (2, 1, "gas_pipeline_terminus_spritelayout_2"),
        (2, 2, "gas_pipeline_terminus_spritelayout_1"),
        (2, 3, "gas_pipeline_terminus_spritelayout_2"),
    ],
)
