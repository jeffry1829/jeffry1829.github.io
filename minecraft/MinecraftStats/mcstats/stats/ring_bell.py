from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'ring_bell',
        {
            'title': '叮叮叮',
            'desc': '撞鐘次數',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:bell_ring']),
        1907 # bells added in 18w44a
    ))
