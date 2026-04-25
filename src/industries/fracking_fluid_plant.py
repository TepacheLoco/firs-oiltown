from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="fracking_fluid_plant",
    accept_cargos_with_input_ratios=[
        ("CHEM", 5),
        ("WATR", 3),
    ],
    prod_cargo_types_with_output_ratios=[],
    prob_in_game="3",
    prob_map_gen="5",
    map_colour="143",
    colour_scheme_name="scheme_3_hendrix",
    location_checks=dict(
        same_type_distance=72,
    ),
    name="string(STR_IND_FRACKING_FLUID_PLANT)",
    nearby_station_name="string(STR_STATION_FRACKING_FLUID_PLANT)",
    fund_cost_multiplier="160",
    intro_year=1975,
    pollution_and_squalor_factor=1,
    sprites_complete=True,
    animated_tiles_fixed=True,
)


def _reuse_tyre_plant_graphics(terrain=None, construction_state_num=None):
    return '"src/graphics/industries/tyre_plant.png"'


industry.get_graphics_file_path = _reuse_tyre_plant_graphics

industry.enable_in_economy(
    "OIL_TOWN",
    prob_in_game="1",
    prob_map_gen="2",
    prod_cargo_types_with_output_ratios=[("FFLD", 8)],
    require_all_inputs_for_production=True,
)

industry.add_tile(
    id="fracking_fluid_plant_tile_1",
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)
industry.add_tile(
    id="fracking_fluid_plant_tile_2",
    animation_length=71,
    animation_looping=True,
    animation_speed=2,
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

spriteset_ground = industry.add_spriteset(
    type="asphalt",
)
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 90, -31, -58)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 10, 64, 90, -31, -58)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 10, 64, 90, -31, -58)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 10, 64, 90, -31, -58)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(290, 10, 64, 64, -31, -32)],
)
spriteset_6 = industry.add_spriteset(
    sprites=[(360, 10, 64, 64, -31, -32)],
    always_draw=True,
)
sprite_smoke_1 = industry.add_smoke_sprite(
    smoke_type="white_smoke_small",
    xoffset=-3,
    yoffset=0,
    zoffset=54,
)
sprite_smoke_2 = industry.add_smoke_sprite(
    smoke_type="white_smoke_small",
    xoffset=-3,
    yoffset=-3,
    zoffset=54,
)

industry.add_spritelayout(
    id="fracking_fluid_plant_spritelayout_silos",
    tile="fracking_fluid_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_1],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="fracking_fluid_plant_spritelayout_building_large_door",
    tile="fracking_fluid_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_2],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="fracking_fluid_plant_spritelayout_building_roof_chimneys",
    tile="fracking_fluid_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_3],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="fracking_fluid_plant_spritelayout_boilerhouse",
    tile="fracking_fluid_plant_tile_2",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_4],
    smoke_sprites=[sprite_smoke_1, sprite_smoke_2],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="fracking_fluid_plant_spritelayout_horizontal_tanks",
    tile="fracking_fluid_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_5],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="fracking_fluid_plant_spritelayout_gatehouse",
    tile="fracking_fluid_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=None,
    building_sprites=[spriteset_6],
    fences=["nw", "ne", "se", "sw"],
)

industry.add_industry_layout(
    id="fracking_fluid_plant_industry_layout_1",
    layout=[
        (0, 0, "fracking_fluid_plant_spritelayout_building_roof_chimneys"),
        (0, 1, "fracking_fluid_plant_spritelayout_building_roof_chimneys"),
        (0, 2, "fracking_fluid_plant_spritelayout_boilerhouse"),
        (1, 0, "fracking_fluid_plant_spritelayout_building_large_door"),
        (1, 1, "fracking_fluid_plant_spritelayout_building_large_door"),
        (1, 2, "fracking_fluid_plant_spritelayout_horizontal_tanks"),
        (2, 0, "fracking_fluid_plant_spritelayout_building_roof_chimneys"),
        (2, 1, "fracking_fluid_plant_spritelayout_silos"),
        (2, 2, "fracking_fluid_plant_spritelayout_gatehouse"),
    ],
)
industry.add_industry_layout(
    id="fracking_fluid_plant_industry_layout_2",
    layout=[
        (0, 0, "fracking_fluid_plant_spritelayout_building_large_door"),
        (0, 1, "fracking_fluid_plant_spritelayout_building_large_door"),
        (0, 2, "fracking_fluid_plant_spritelayout_boilerhouse"),
        (1, 0, "fracking_fluid_plant_spritelayout_building_roof_chimneys"),
        (1, 1, "fracking_fluid_plant_spritelayout_building_roof_chimneys"),
        (1, 2, "fracking_fluid_plant_spritelayout_horizontal_tanks"),
        (2, 0, "fracking_fluid_plant_spritelayout_silos"),
        (2, 1, "fracking_fluid_plant_spritelayout_building_large_door"),
        (2, 2, "fracking_fluid_plant_spritelayout_gatehouse"),
    ],
)
