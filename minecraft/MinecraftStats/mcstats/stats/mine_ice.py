from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'mine_ice',
        {
            'title': '冰塊破壞者',
            'desc': '破壞的冰塊總量',
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:mined','minecraft:ice']),
            mcstats.StatReader(['minecraft:mined','minecraft:packed_ice']),
            mcstats.StatReader(['minecraft:mined','minecraft:blue_ice']),
            mcstats.StatReader(['minecraft:mined','minecraft:frosted_ice']),
        ])
    ))
