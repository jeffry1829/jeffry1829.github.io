from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'mine_grass',
        {
            'title': '除草機',
            'desc': '破壞雜草數量',
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:mined','minecraft:grass']),
            mcstats.StatReader(['minecraft:mined','minecraft:tall_grass']),
        ])
    ))
