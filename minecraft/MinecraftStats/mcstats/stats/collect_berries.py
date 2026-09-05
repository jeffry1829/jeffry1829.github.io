from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'collect_berries',
        {
            'title': '莓果採集家',
            'desc': '採集的莓果數量',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:picked_up','minecraft:sweet_berries']),
        1916 # berries introduced in 18w49a
    ))
