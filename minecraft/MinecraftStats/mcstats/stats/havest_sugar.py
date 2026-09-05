from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'harvest_sugar',
        {
            'title': '蔗糖廠',
            'desc': '製造的糖的數量',
            'unit': 'int',
        },
        mcstats.StatDiffReader(
            mcstats.StatReader(['minecraft:picked_up','minecraft:sugar_cane']),
            mcstats.StatReader(['minecraft:used','minecraft:sugar_cane'])
        )
    ))
